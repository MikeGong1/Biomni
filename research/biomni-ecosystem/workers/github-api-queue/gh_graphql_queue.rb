#!/usr/bin/env ruby
# frozen_string_literal: true

require "digest"
require "fileutils"
require "json"
require "net/http"
require "open3"
require "securerandom"
require "time"
require "timeout"
require "uri"

Encoding.default_external = Encoding::UTF_8
Encoding.default_internal = Encoding::UTF_8

STATE_DIR = ENV.fetch("BIOMNI_GITHUB_QUEUE_STATE", "/private/tmp/biomni-github-api-queue")
GLOBAL_REQUESTS_PER_MINUTE = 60
AGENT_REQUESTS_PER_MINUTE = 6
CONCURRENT_SLOTS = 4
GRAPHQL_HEADROOM = 0.80
MAX_SINGLE_SLEEP_SECONDS = 55.0
MAX_RETRIES = 2
CACHE_MAX_AGE_SECONDS = ENV.fetch("BIOMNI_GITHUB_GRAPHQL_CACHE_SECONDS", "300").to_i
RATE_BUCKET_ID = "authenticated"

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
        { "GIT_TERMINAL_PROMPT" => "0" }, "git", "credential", "fill",
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

def credential_fingerprint(token)
  Digest::SHA256.hexdigest(token)
end

def ensure_credential_scope(fingerprint)
  matches = with_state do |state|
    existing = state["credential_fingerprint"]
    if existing && existing != fingerprint
      false
    else
      state["credential_fingerprint"] = fingerprint
      true
    end
  end
  return if matches

  warn "queue state belongs to a different GitHub credential"
  exit 77
end

def write_json_private(path, value)
  temporary = "#{path}.#{Process.pid}.#{SecureRandom.hex(4)}"
  File.open(temporary, File::WRONLY | File::CREAT | File::TRUNC, 0o600) do |file|
    file.write(JSON.generate(value))
  end
  File.rename(temporary, path)
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

def reserve_request(agent, estimated_cost, bucket_id)
  reservation_id = SecureRandom.hex(12)
  loop do
    now = Time.now.to_f
    decision = with_state do |state|
      state["global"] = prune(state["global"], now - 60)
      state["agents"] ||= {}
      state["agents"][agent] = prune(state["agents"][agent], now - 60)
      state["graphql_buckets"] ||= {}
      bucket = state["graphql_buckets"][bucket_id] ||= {}
      bucket["points"] = Array(bucket["points"]).select do |entry|
        entry["time"].to_f > now - 3600
      end

      waits = []
      global_cooldown = state.fetch("cooldown_until", 0).to_f
      waits << global_cooldown - now if global_cooldown > now
      cooldown = bucket.fetch("cooldown_until", 0).to_f
      waits << cooldown - now if cooldown > now
      waits << state["global"].first + 60 - now if state["global"].length >= GLOBAL_REQUESTS_PER_MINUTE
      if state["agents"][agent].length >= AGENT_REQUESTS_PER_MINUTE
        waits << state["agents"][agent].first + 60 - now
      end

      limit = bucket.fetch("limit", 0).to_i
      remaining = bucket.fetch("remaining", limit).to_i
      reset = bucket.fetch("reset", 0).to_i
      if limit.positive?
        reserve_points = limit - (limit * GRAPHQL_HEADROOM).floor
        waits << reset + 1 - now if remaining - estimated_cost < reserve_points && reset > now
        used_window = bucket["points"].map { |entry| entry["cost"].to_i }.inject(0, :+)
        cap = (limit * GRAPHQL_HEADROOM).floor
        if used_window + estimated_cost > cap && bucket["points"].any?
          waits << bucket["points"].first["time"].to_f + 3600 - now
        end
      end

      wait = waits.select { |value| value.positive? }.max.to_f
      if wait <= 0
        state["global"] << now
        state["agents"][agent] << now
        bucket["points"] << { "id" => reservation_id, "time" => now, "cost" => estimated_cost }
        bucket["remaining"] = [remaining - estimated_cost, 0].max if limit.positive?
        { "reserved" => true, "wait" => 0 }
      else
        { "reserved" => false, "wait" => wait }
      end
    end
    return reservation_id if decision["reserved"]
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

def request_once(payload, token)
  uri = URI("https://api.github.com/graphql")
  http = Net::HTTP.new(uri.host, uri.port)
  http.use_ssl = true
  http.open_timeout = 15
  http.read_timeout = 90
  request = Net::HTTP::Post.new(uri.request_uri)
  request["Accept"] = "application/vnd.github+json"
  request["Content-Type"] = "application/json"
  request["User-Agent"] = "biomni-ecosystem-audit"
  request["Authorization"] = "Bearer #{token}"
  request.body = JSON.generate({ "query" => payload.fetch("query"), "variables" => payload.fetch("variables", {}) })
  http.request(request)
end

def update_graphql_state(response, parsed, bucket_id, reservation_id)
  rate = parsed.dig("data", "rateLimit") || {}
  actual_cost = rate["cost"]&.to_i
  with_state do |state|
    state["graphql_buckets"] ||= {}
    bucket = state["graphql_buckets"][bucket_id] ||= {}
    header_limit = response["x-ratelimit-limit"]&.to_i
    header_remaining = response["x-ratelimit-remaining"]&.to_i
    header_reset = response["x-ratelimit-reset"]&.to_i
    limit = rate["limit"]&.to_i || header_limit
    remaining = rate["remaining"]&.to_i || header_remaining
    reset = rate["resetAt"] ? Time.parse(rate["resetAt"]).to_i : header_reset
    point_entry = Array(bucket["points"]).find { |entry| entry["id"] == reservation_id }
    point_entry["cost"] = actual_cost if point_entry && actual_cost
    stored_reset = bucket.fetch("reset", 0).to_i
    unless reset && reset < stored_reset
      bucket["limit"] = limit if limit
      if remaining
        if reset && stored_reset == reset && bucket["remaining"]
          bucket["remaining"] = [bucket["remaining"].to_i, remaining].min
        else
          bucket["remaining"] = remaining
        end
      end
      bucket["reset"] = reset if reset
      if limit && remaining && reset && remaining <= limit - (limit * GRAPHQL_HEADROOM).floor
        bucket["cooldown_until"] = [bucket.fetch("cooldown_until", 0).to_f, reset + 1].max
      end
    end
    retry_after = response["retry-after"]
    if retry_after
      state["cooldown_until"] = [state.fetch("cooldown_until", 0).to_f, Time.now.to_f + retry_after.to_f].max
    end
  end
  actual_cost
end

token, auth_source = credential
bucket_id = RATE_BUCKET_ID if token && !token.empty?
credential_fingerprint_value = credential_fingerprint(token) if token && !token.empty?
if ARGV == ["--status"]
  state = with_state { |value| JSON.parse(JSON.generate(value)) }
  bucket = bucket_id ? state.dig("graphql_buckets", bucket_id) || {} : {}
  pinned_fingerprint = state["credential_fingerprint"]
  puts JSON.pretty_generate({
    "auth_source" => auth_source,
    "authenticated" => !bucket_id.nil?,
    "authenticated_bucket_available" => !bucket.empty?,
    "credential_matches_state" => !bucket_id.nil? && pinned_fingerprint == credential_fingerprint_value,
    "authenticated_primary_state_shared" => true,
    "credential_cache_isolation" => true,
    "concurrent_slots" => CONCURRENT_SLOTS,
    "global_requests_per_minute" => GLOBAL_REQUESTS_PER_MINUTE,
    "agent_requests_per_minute" => AGENT_REQUESTS_PER_MINUTE,
    "graphql_headroom" => GRAPHQL_HEADROOM,
    "graphql_limit" => bucket["limit"],
    "graphql_remaining" => bucket["remaining"],
    "graphql_reset" => bucket["reset"],
    "recent_graphql_reserved_or_actual_points" => Array(bucket["points"]).map { |entry| entry["cost"].to_i }.inject(0, :+),
    "primary_cooldown_until" => bucket["cooldown_until"],
    "global_cooldown_until" => state["cooldown_until"]
  })
  exit 0
end

unless ARGV.length == 3
  warn "usage: gh_graphql_queue.rb AGENT_ID QUERY_JSON OUTPUT_JSON | --status"
  exit 64
end
agent, query_path, output_path = ARGV
unless agent.match?(/\A[a-zA-Z0-9_-]+\z/)
  warn "invalid agent id"
  exit 64
end
unless token && !token.empty?
  warn "authenticated GitHub credential required for GraphQL"
  exit 77
end

payload = JSON.parse(File.read(query_path))
query = payload.fetch("query")
variables = payload.fetch("variables", {})
estimated_cost = payload.fetch("estimated_cost", 1).to_i
unless estimated_cost.between?(1, 100)
  warn "estimated_cost must be 1..100"
  exit 64
end
unless query.include?("rateLimit")
  warn "query must include top-level rateLimit { limit cost remaining resetAt }"
  exit 64
end
first_values = query.scan(/\bfirst\s*:\s*(\d+)/).flatten.map(&:to_i)
unless first_values.all? { |value| value.between?(1, 100) }
  warn "every first: value must be 1..100"
  exit 64
end
if JSON.generate({ "query" => query, "variables" => variables }).bytesize > 100_000
  warn "GraphQL request body too large"
  exit 64
end

expanded_output = File.expand_path(output_path)
allowed_roots = ["/private/tmp/", "/private/var/folders/", "/var/folders/"]
unless allowed_roots.any? { |root| expanded_output.start_with?(root) }
  warn "output must be under a temporary directory"
  exit 64
end
ensure_credential_scope(credential_fingerprint_value)
meta_path = "#{expanded_output}.meta.json"
input_sha = Digest::SHA256.hexdigest(JSON.generate({
  "query" => query,
  "variables" => variables,
  "credential_fingerprint" => credential_fingerprint_value
}))
if File.exist?(expanded_output) && File.exist?(meta_path)
  meta = JSON.parse(File.read(meta_path))
  if meta["input_sha"] == input_sha && Time.now.to_f - meta.fetch("checked_at_epoch", 0).to_f <= CACHE_MAX_AGE_SECONDS
    puts JSON.generate({ "status" => 200, "cached" => true, "auth_source" => auth_source, "output" => expanded_output })
    exit 0
  end
end

response = nil
parsed = {}
attempt = 0
actual_cost = nil
any_cost_underestimated = false
attempt_costs = []
loop do
  slot = acquire_slot
  begin
    reservation_id = reserve_request(agent, estimated_cost, bucket_id)
    response = request_once(payload, token)
  ensure
    slot.flock(File::LOCK_UN)
    slot.close
  end
  begin
    parsed = JSON.parse(response.body)
  rescue JSON::ParserError
    parsed = {}
  end
  actual_cost = update_graphql_state(response, parsed, bucket_id, reservation_id)
  attempt_underestimated = actual_cost && actual_cost > estimated_cost
  any_cost_underestimated ||= attempt_underestimated
  attempt_costs << {
    "attempt" => attempt + 1,
    "estimated_cost" => estimated_cost,
    "actual_cost" => actual_cost,
    "cost_underestimated" => attempt_underestimated
  }
  retryable = response.code.to_i >= 500 || response.code.to_i == 429 ||
              (response.code.to_i == 403 && response["retry-after"])
  if retryable && attempt < MAX_RETRIES
    attempt += 1
    next
  end
  break
end

FileUtils.mkdir_p(File.dirname(expanded_output))
temporary = "#{expanded_output}.#{Process.pid}.#{SecureRandom.hex(4)}"
File.binwrite(temporary, response.body)
File.chmod(0o600, temporary)
File.rename(temporary, expanded_output)
metadata = {
  "input_sha" => input_sha,
  "checked_at" => Time.now.utc.iso8601,
  "checked_at_epoch" => Time.now.to_f,
  "estimated_cost" => estimated_cost,
  "actual_cost" => actual_cost,
  "cost_underestimated" => any_cost_underestimated,
  "attempt_costs" => attempt_costs
}
write_json_private(meta_path, metadata)

unless response.is_a?(Net::HTTPSuccess)
  warn JSON.generate({ "status" => response.code.to_i, "message" => "GitHub GraphQL request failed", "output" => expanded_output })
  exit 69
end
if parsed["errors"]
  warn JSON.generate({ "status" => response.code.to_i, "message" => "GitHub GraphQL returned errors", "output" => expanded_output })
  exit 65
end
puts JSON.generate({
  "status" => response.code.to_i,
  "cached" => false,
  "auth_source" => auth_source,
  "estimated_cost" => estimated_cost,
  "actual_cost" => actual_cost,
  "cost_underestimated" => any_cost_underestimated,
  "rate_limit" => parsed.dig("data", "rateLimit", "limit"),
  "rate_remaining" => parsed.dig("data", "rateLimit", "remaining"),
  "rate_reset" => parsed.dig("data", "rateLimit", "resetAt"),
  "output" => expanded_output
})
