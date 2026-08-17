# FÆBRIQ Working Memory — append-only log

## 2026-08-17
- Created CLAUDE.md and MEMORY.md for session persistence. (Note: this entry was originally misdated 2026-08-13; corrected.)
- Repo's default branch is named `mknuever-lgtm-patch-1`, not `main` — an old auto-generated name from a one-off GitHub web edit that got left as default. Functions fine, just an unusual name. Renaming the actual GitHub "default branch" setting isn't reachable from this session's GitHub tools (no repo-admin/settings endpoint); would need the GitHub web UI (Settings → Branches) or a session with broader GitHub scope.
- Every Claude Code web session works on its own auto-named branch (e.g. `claude/great-wozniak-Ke10Y`); it only lands in the real project once merged via PR. Found 6 old leftover session branches never cleaned up — 5 were stale/fully superseded by later work already on the default branch. One (`claude/shopify-product-progress-o8wxkv`) contained a real, unmerged FÆBRIQ Brand Kit (`faebriq-brand-kit/SKILL.md` + `references/`) — voice, visual identity, color/type tokens, sample copy — recovered and merged into the default branch. CLAUDE.md's brand-voice section now points to it directly.
