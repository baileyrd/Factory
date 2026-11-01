---
name: interface
description: House standard for programmatic interfaces (public APIs, CLIs, wire protocols, MCP tools, config formats, module boundaries). Musts are blockable; shoulds are flagged.
version: 0.1
owner: Approver
---

# Scope
Any card that adds or changes a public API, CLI, wire protocol, MCP tool, config format or module boundary. GUI has its own standard. Pair with `api-contract-evolution-expert` and `mcp-agent-tool-design-expert` where relevant.

# Musts
- Contract first: inputs, outputs, errors and invariants specified before code; the Tester writes tests against it.
- Breaking changes are explicit: version bump, migration note, and the Approver's sign-off.
- Errors are typed and actionable: what failed, why, what the caller can do.
- Input validated at the boundary; unknown or invalid input rejected clearly.
- Interfaces expose domain types, not framework or storage types.
- Safe defaults; destructive operations need explicit intent.

# Shoulds
- Small surface; options only for real callers.
- Consistent naming, argument order and error shapes across the project.
- Idempotent operations where possible.
- Common case simple, rare case possible.
- Machine-readable output (JSON) alongside human output for CLIs and tools.
- Every public entry point documented with an example.

# Mistakes to avoid
Boolean flag parameters; stringly-typed options; leaking internals; silent defaults that change behavior; one endpoint doing many things; versioning added after the first break.

# Role notes
- Planner: name the callers and use cases; define the contract in the requirements.
- Architect: own boundaries and contract shape.
- Tester: contract tests including invalid input, error shapes and compatibility.
- Reviewer: check consistency with existing interfaces; flag every breaking change.

# Review checklist
Contract documented · errors typed with context · breaking changes versioned and approved · input validated · no internal types exposed · examples present.

# References
Rust API Guidelines; the project's existing interface conventions.
