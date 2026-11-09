---
name: push-to-git
description: Commit and push occi-setup site changes to GitHub (pavan4all/occi-setup, branch main) so GitHub Pages republishes. Use whenever the user says push, publish, sync with git, or deploy for this project.
---

# Push occi-setup to GitHub

Repo: https://github.com/pavan4all/occi-setup (branch `main`, public, served by GitHub Pages at https://pavan4all.github.io/occi-setup/, also reachable at https://viriya4all.org/occi-setup via a Cloudflare redirect).

## Steps

1. Work from the repo root (`C:\Users\pgoklani\Claude Projects\occi-setup`). Confirm with `git rev-parse --show-toplevel` that it is this repo and not the home-directory repo.
2. Use the `pavan4all` GitHub account for this project. Run `gh auth status`; if `pavan4all` is not the active account, run `gh auth switch -u pavan4all`. Do not leave another account active for this repo's operations.
3. `git fetch origin`, then `git status -sb`. If behind, `git pull --rebase origin main` before committing. Stop and report if there are conflicts.
4. Regenerate the Markdown copy so it matches the HTML: `python3 -I tools/to_md.py . markdown` (needs `beautifulsoup4` and `markdownify`). Never hand-edit `markdown/`; edit the HTML and regenerate.
5. Review what will be committed (`git status --short`, `git diff --stat`). Do not commit `.cursor/` (ignored), temp test files (`_t*.html`), or anything outside the site. Stage specific files or `git add -A` only after this check.
6. Commit with a short imperative message. End the message with:
   `Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>`
7. `git push origin main`. Never force-push.
8. Verify: `git rev-list --left-right --count origin/main...HEAD` returns `0 0`, and report the commit hash.
9. Optionally confirm the Pages build: `gh api repos/pavan4all/occi-setup/pages --jq .status` should reach `built` (usually under 2 minutes).

## Notes

- Every page loads `assets/auth.js` (client-side login gate) and `assets/nav.js` (menu). New pages must include both, with relative paths. Check with `grep -L "assets/auth.js"` over the HTML files before pushing.
- The login gate is not real security. Never put secrets in the repo; it is public.
- If `viriya4all.org` does not load from the user's machine, that is a network/Cisco filter issue, not a push problem. Use the github.io URL to verify.
