# Markdown copy of the site

Every page of the site, as Markdown. Same folder layout as the HTML pages:
`index.md` is the home page, `setup-days/...`, `metta-day-cleanup/...` and so on.

These files are generated from the HTML pages by `tools/to_md.py`. Edit the HTML (or regenerate) and these stay in step. Do not hand-edit them, or the next regeneration will overwrite the edits.

Regenerate from the repo root:

    python3 -I tools/to_md.py . markdown
