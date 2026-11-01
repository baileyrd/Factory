# Project overlay template

Copy to `.factory/overlay.md` in the project's repo. Optional: a project with no overlay runs on the base roles and standards it touches. An overlay adds and tightens; it never removes a base rule, gate or separation of duties. Changes to it go through review like code.

```markdown
---
project: <name>
version: 0.1
---

# Brief
Two or three sentences: what the project is, who it's for, what matters most.

# Experts
- <expert-name>: when a card should load it

# Standards
- <standard-name>

# Project rules
Project-specific musts and shoulds, marked as such. Each one says why.

# Role notes
- Planner:
- Architect:
- Builder:
- Tester:
- Reviewer:

# Oracles and tools
Reference implementations, probes, benchmarks and how to run them.
```
