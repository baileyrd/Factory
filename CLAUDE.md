# Factory

Source of truth for the software factory's roles, knowledge, standards, overlay drafts and role threads. Read `README.md` and `roles/_protocol.md` first.

## Rules for working in this repo

- `roles/`, `knowledge/` and `standards/` are generic: no project names, private repos or people. Project specifics belong in an overlay.
- Every role, knowledge and standard file has YAML frontmatter whose `name` equals the file stem.
- Never weaken a gate, separation of duties, or the Reviewer's and Tester's independence from the Builder.
- Changes land by PR with `python3 -m unittest` and `python3 -m tools.check` passing.
- Retro proposals cite the cards and projects that justify them (see `roles/retro.md` for the evidence bar).
- Keep files terse. Match the existing format of the folder you're editing.
