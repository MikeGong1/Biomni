# Research State

last_updated_utc: 2026-08-22T21:04:17Z
current_phase: Phase 2 - breadth-first upstream inventory
current_entity: snap-stanford/Biomni PR authors
current_batch: pr-author-normalization-001
current_page_or_cursor: exhausted for 182 PRs
completed_units:
- recovered existing research branch from origin
- verified branch ancestry against MikeGong1/Biomni main
- initialized bounded methodology and machine-readable database
- froze snap-stanford/Biomni main baseline at 400c1f366b96a35ca253e13c9b06c5076af41d65
- verified merged PR inventory page 1 (100 of 111, created ascending)
- verified public fork discovery page 1 (100 of 690, newest first)
- completed and verified open PR inventory (38 of 38; pagination exhausted)
- completed and verified closed-unmerged PR inventory (33 of 33; pagination exhausted)
- completed and verified merged PR inventory (111 of 111; pagination exhausted)
- verified main commit page 1 (100 of 487; newest first)
- verified public fork discovery page 2 (cumulative 200 of 690)
- completed snap-stanford public repository screening (92 of 92; 17 HIGH)
- completed snap-stanford public member inventory (6 of 6)
- completed and verified upstream branch inventory (33 of 33; 29 ahead=0)
- verified 45 contributor endpoint rows and all 487 main-history commits
- verified bounded commercial discovery: 17 grouped behaviors and 11 timeline events
- verified main commit page 2 (cumulative 200 of 487)
- verified public fork discovery page 3 (cumulative 300 of 690)
- verified public fork discovery page 4 (cumulative 400 of 690)
- verified main commit page 3 (cumulative 300 of 487)
- normalized all 182 PR authors into 76 unique logins and canonical people IDs
pending_units:
- inventory open, merged, and closed-unmerged upstream PRs with pagination
- index the complete upstream commit graph
- discover and screen all publicly visible forks
- merge branch-only and substantive-fork-owner accounts into P
- continue official commercial discovery where pagination/indexing permits
- compare verified commercial behaviors against frozen OSS baseline
- assess clean-room reconstruction only after OSS comparison
- inventory public fork pages 2 through 7
unresolved_identity_mappings:
- 56 exact Git author/committer tuples remain unmapped; see people/github/seed-inventory-001.md
- contributor login RyanLi1028 and raw noreply string RyanLi0802 are not assumed equivalent
unresolved_lineages:
- PR #289 and #290 exact PR-surface duplicate candidate; patch identity pending
- popper_biomni, 0.0.4_release, hotfix/v0.0.6-param-naming, and pre-commit-ci-update-config branch leads require patch/PR normalization
unresolved_questions: []
next_action: resume GitHub API pagination after rate-limit reset; then complete commit/fork inventories
