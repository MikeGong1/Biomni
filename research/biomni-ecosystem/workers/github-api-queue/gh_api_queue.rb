#!/usr/bin/env ruby
# frozen_string_literal: true

require "fileutils"
require "json"
require "net/http"
require "open3"
require "securerandom"
require "timeout"
require "time"
require "uri"

Encoding.default_external = Encoding::UTF_8
Encoding.default_internal = Encoding::UTF_8

STATE_DIR = ENV.fetch("BIOMNI_GITHUB_QUEUE_STATE", "/private/tmp/biomni-github-api-queue")
GLOBAL_REQUESTS_PER_MINUTE = 60
AGENT_REQUESTS_PER_MINUTE = 6
CONCURRENT_SLOTS = 4
PRIMARY_HEADROOM = 0.80
MAX_SINGLE_SLEEP_SECONDS = 55.0
MAX_RETRIES = 2

FileUtils.mkdir_p(STATE_DIR)

def credential
  token = ENV["GITHUB_TOKEN"]
  return [token, "GITHUB_TOKEN"] unless token.nil? || token.empty?
  token = ENV["GH_TOKEN"]
  return [token, "GH_TOKEN"] unless token.nil? || token.empty?

  begin
    output = ""
    Timeout.timeout(5) do
      output, = Open3.capture3(
        { "GIT_TERMINAL_PROMPT" => "0" },
        "git", "credential", "fill",
        stdin_data: "protocol=https\nhost=github.com\n\n"
      )
    end
    password = output.lines.find { |line| line.start_with?("password=") }
    return [password.split("=", 2).last.strip, "git-credential"] if password
  rescue Timeout::Error
    nil
  end
  [nil, "none"]
end

def state_path(name)
  File.join(STATE_DIR, name)
end

def with_state
  File.open(state_path("state.lock"), File::RDWR | File::CREAT, 0o600) do |lock|
    lock.flock(File::LOCK_EX)
    path = state_path("state.json")
    state = File.exist?(path) ? JSON.parse(File.read(path)) : {}
    result = yield(state)
    temporary = "#{path}.#{Process.pid}.#{SecureRandom.hex(4)}"
    File.write(temporary, JSON.generate(state), mode: "w", perm: 0o600)
    File.rename(temporary, path)
    result
  end
end

def prune(values, cutoff)
  Array(values).map(&:to_f).select { |value| value > cutoff }
end

def reserve_request(agent)
  loop do
    now = Time.now.to_f
    decision = with_state do |state|
      state["global"] = prune(state["global"], now - 60)
      state["primary"] = prune(state["primary"], now - 3600)
      state["agents"] ||= {}
      state["agents"][agent] = prune(state["agents"][agent], now - 60)

      waits = []
      cooldown = state.fetch("cooldown_until", 0).to_f
      waits << cooldown - now if cooldown > now
      if state["global"].length >= GLOBAL_REQUESTS_PER_MINUTE
        waits << state["global"].first + 60 - now
      end
      if state["agents"][agent].length >= AGENT_REQUESTS_PER_MINUTE
        waits << state["agents"][agent].first + 60 - now
      end

      primary_limit = state.fetch("primary_limit", 0).to_i
      if primary_limit.positive? && primary_limit <= 60
        primary_cap = [(primary_limit * PRIMARY_HEADROOM).floor, 1].max
        reserve_remaining = primary_limit - primary_cap
        primary_remaining = state.fetch("primary_remaining", primary_limit).to_i
        primary_reset = state.fetch("primary_reset", 0).to_i
        if primary_remaining <= reserve_remaining && primary_reset > now
          waits << primary_reset + 1 - now
        end
        if state["primary"].length >= primary_cap
          waits << state["primary"].first + 3600 - now
        end
      end

      wait = waits.select { |value| value.positive? }.max.to_f
      if wait <= 0
        state["global"] << now
        state["primary"] << now
        state["agents"][agent] << now
        if primary_limit.positive? && primary_limit <= 60 && state["primary_remaining"]
          state["primary_remaining"] = [state["primary_remaining"].to_i - 1, 0].max
        end
        { "reserved" => true, "wait" => 0 }
      else
        { "reserved" => false, "wait" => wait }
      end
    end
    return if decision["reserved"]
    sleep([decision["wait"], MAX_SINGLE_SLEEP_SECONDS].min)
  end
end

def acquire_slot
  loop do
    CONCURRENT_SLOTS.times do |index|
      file = File.open(state_path("slot-#{index}.lock"), File::RDWR | File::CREAT, 0o600)
      return file if file.flock(File::LOCK_EX | File::LOCK_NB)
      file.close
    end
    sleep(0.1)
  end
end

def request_once(uri, token, etag = nil)
  http = Net::HTTP.new(uri.host, uri.port)
  http.use_ssl = true
  http.open_timeout = 15
  http.read_timeout = 60
  request = Net::HTTP::Get.new(uri.request_uri)
  request["Accept"] = "application/vnd.github+json"
  request["X-GitHub-Api-Version"] = "2022-11-28"
  request["User-Agent"] = "biomni-ecosystem-audit"
  request["Authorization"] = "Bearer #{token}" if token && !token.empty?
  request["If-None-Match"] = etag if etag && !etag.empty?
  http.request(request)
end

def update_rate_state(response)
  with_state do |state|
    limit = response["x-ratelimit-limit"]
    remaining = response["x-ratelimit-remaining"]
    reset = response["x-ratelimit-reset"]
    state["primary_limit"] = limit.to_i if limit
    if remaining
      if reset && state["primary_reset"].to_i == reset.to_i && state["primary_remaining"]
        state["primary_remaining"] = [state["primary_remaining"].to_i, remaining.to_i].min
      else
        state["primary_remaining"] = remaining.to_i
      end
    end
    state["primary_reset"] = reset.to_i if reset
    if remaining && remaining.to_i <= 0 && reset
      state["cooldown_until"] = [state.fetch("cooldown_until", 0).to_f, reset.to_i + 1].max
    end
    retry_after = response["retry-after"]
    if retry_after
      state["cooldown_until"] = [state.fetch("cooldown_until", 0).to_f, Time.now.to_f + retry_after.to_f].max
    end
  end
end

def queue_status(auth_source)
  snapshot = with_state { |state| JSON.parse(JSON.generate(state)) }
  now = Time.now.to_f
  output = {
    "auth_source" => auth_source,
    "concurrent_slots" => CONCURRENT_SLOTS,
    "global_requests_per_minute" => GLOBAL_REQUESTS_PER_MINUTE,
    "agent_requests_per_minute" => AGENT_REQUESTS_PER_MINUTE,
    "primary_headroom" => PRIMARY_HEADROOM,
    "observed_primary_limit" => snapshot["primary_limit"],
    "observed_primary_remaining" => snapshot["primary_remaining"],
    "observed_primary_reset" => snapshot["primary_reset"],
    "recent_global_requests" => prune(snapshot["global"], now - 60).length,
    "recent_primary_requests" => prune(snapshot["primary"], now - 3600).length,
    "cooldown_until" => snapshot["cooldown_until"]
  }
  puts JSON.pretty_generate(output)
end

token, auth_source = credential
if ARGV == ["--status"]
  queue_status(auth_source)
  exit 0
end

unless ARGV.length == 3
  warn "usage: gh_api_queue.rb AGENT_ID API_URL OUTPUT_JSON | --status"
  exit 64
end

agent, raw_url, output_path = ARGV
unless agent.match?(/\A[a-zA-Z0-9_-]+\z/)
  warn "invalid agent id"
  exit 64
end
uri = URI.parse(raw_url)
unless uri.is_a?(URI::HTTPS) && uri.host == "api.github.com"
  warn "only https://api.github.com/ URLs are allowed"
  exit 64
end
expanded_output = File.expand_path(output_path)
allowed_roots = ["/private/tmp/", "/private/var/folders/", "/var/folders/"]
unless allowed_roots.any? { |root| expanded_output.start_with?(root) }
  warn "output must be under a temporary directory"
  exit 64
end
meta_path = "#{expanded_output}.meta.json"
cached_meta = if File.exist?(expanded_output) && File.exist?(meta_path)
                JSON.parse(File.read(meta_path))
              else
                {}
              end
etag = cached_meta["url"] == uri.to_s ? cached_meta["etag"] : nil

response = nil
attempt = 0
current_uri = uri
loop do
  reserve_request(agent)
  slot = acquire_slot
  begin
    response = request_once(current_uri, token, current_uri == uri ? etag : nil)
  ensure
    slot.flock(File::LOCK_UN)
    slot.close
  end
  update_rate_state(response)

  if response.is_a?(Net::HTTPRedirection) && response["location"] && attempt < MAX_RETRIES
    redirected = URI.join(current_uri.to_s, response["location"])
    unless redirected.is_a?(URI::HTTPS) && redirected.host == "api.github.com"
      warn "refusing cross-host redirect"
      exit 69
    end
    current_uri = redirected
    attempt += 1
    next
  end

  retryable = response.code.to_i >= 500 || response.code.to_i == 429 ||
              (response.code.to_i == 403 && response["retry-after"])
  if retryable && attempt < MAX_RETRIES
    attempt += 1
    next
  end
  break
end

if response.is_a?(Net::HTTPNotModified) && File.exist?(expanded_output)
  cached_meta["checked_at"] = Time.now.utc.iso8601
  File.write(meta_path, JSON.generate(cached_meta))
  puts JSON.generate({
    "status" => response.code.to_i,
    "cached" => true,
    "auth_source" => auth_source,
    "rate_limit" => response["x-ratelimit-limit"]&.to_i,
    "rate_remaining" => response["x-ratelimit-remaining"]&.to_i,
    "rate_reset" => response["x-ratelimit-reset"]&.to_i,
    "output" => expanded_output
  })
  exit 0
end

unless response.is_a?(Net::HTTPSuccess)
  warn JSON.generate({ "status" => response.code.to_i, "message" => "GitHub API request failed" })
  exit 69
end

FileUtils.mkdir_p(File.dirname(expanded_output))
temporary = "#{expanded_output}.#{Process.pid}.#{SecureRandom.hex(4)}"
File.binwrite(temporary, response.body)
File.rename(temporary, expanded_output)
metadata = {
  "url" => current_uri.to_s,
  "etag" => response["etag"],
  "last_modified" => response["last-modified"],
  "checked_at" => Time.now.utc.iso8601
}
File.write(meta_path, JSON.generate(metadata))
puts JSON.generate({
  "status" => response.code.to_i,
  "cached" => false,
  "auth_source" => auth_source,
  "rate_limit" => response["x-ratelimit-limit"]&.to_i,
  "rate_remaining" => response["x-ratelimit-remaining"]&.to_i,
  "rate_reset" => response["x-ratelimit-reset"]&.to_i,
  "output" => expanded_output
})
