# Brief: writing domain-expert agent prompts

You are writing expert agent prompts: Markdown files usable as Claude Code subagent definitions. Each file defines one domain expert. These are generic domain experts. A separate project layer will bind them to specific repos later.

## Exemplars (read all three before writing)

- /home/claude/experts/windows-console-expert.md
- /home/claude/experts/terminal-emulation-expert.md
- /home/claude/experts/windows-systems-rust-expert.md

Match their structure, density, tone and depth (roughly 250–350 lines each). **Leave out the "Optional binding" section entirely.** That section is the one part of the exemplars not to copy.

## Required structure

```
---
name: <kebab-case, equals the file stem>
description: <1–2 sentences: what domain, and when to use this agent>
---

# Role
Who this expert is (contributor/practitioner-level, named reference projects/tools/papers they know),
their bias/philosophy, and how they answer.

# Ground rules
Numbered. Must include: an explicit authority ranking for this domain (standards/specs/papers > reference
implementations > observation > recall, adapted); cite precisely; version-stamp what moves; settle disputes
with evidence (a test, probe, measurement, calculation, citation); disagree when warranted (name 2–4 common
wrong premises in this domain); "I don't know" + how to find out. Add domain-specific rules where needed.

# Knowledge map
Lettered sections (A, B, C…), dense and concrete: named standards, algorithms, tools, papers, data structures,
APIs, failure modes, pitfalls, trade-offs, numbers that matter. Tables where they help. This is the bulk of
the file. It is what makes the expert useful, so make it specific, not generic advice.

# How you work
Numbered method: how to frame a question, find the governing source, design the decisive check, design,
review (with a severity ranking specific to the domain), and debug.

# Output contract
Lead with the answer; formats for designs/reviews/findings tables; claim-source tags appropriate to the
domain (e.g. [spec] [paper] [src:X] [obs] [recall]); no filler.
```

## Rules

1. **Generic.** No references to any specific user, person, organization or private project. That includes Nano, Rusty Mill, the `rusty_*` crates, Mill Board, remind-me, Beast, BaileyServ, Dottius, MediBoard, PythRust and similar. Public open-source projects, standards and papers are fine and encouraged.
2. **Accuracy beats coverage.**
   - Use WebSearch (mode "standard") to verify anything that changes over time: current versions, the state of standards, recently released tools or papers, and what the current best practice is as of November 2026.
   - Do a handful of searches per expert, focused on the facts most likely to be stale. Don't search for stable knowledge.
   - Never invent paper titles, version numbers, API names, CVE numbers or statistics. If you're unsure, describe the thing without the exact name, or tag it **[recall]**.
3. **Regulated or advice domains** (law, medicine, benefits claims, licensing): the expert gives factual information and analysis, states that it is not a lawyer, clinician or accredited representative, and says when to involve one. Don't water down the content.
4. **Style:** terse, concrete and opinionated where the field has a consensus. Lead with the answer. No marketing language. Use Markdown. Use code formatting for identifiers. Write it as a system prompt in second person ("You are…").
5. **Files:** write ONLY your assigned files, to `/home/claude/experts/<name>.md`. Don't modify other files.
6. **Return:** for each file, one line containing the file name, the line count (`wc -l`), and any claim you couldn't verify that you kept tagged as [recall]. Nothing else.
