---
project: rusty_term
version: 0.1
---

<!-- Draft built from _seed-from-catalog.md. Copy to rusty_term/.factory/overlay.md. -->

# Brief
A Rust terminal and console host for Windows, replacing conhost and the terminal. `rusty_term_core::Grid` is shared with rusty_conhost, the console host built on top of it. Correctness against conhost behavior and robustness against hostile clients matter most, then latency.

# Experts
- `windows-console-expert`: any card touching ConDrv, the console API, ConPTY or rusty_conhost.
- `terminal-emulation-expert`: VT parsing, grid, scrollback, reflow, width tables.
- `windows-gui-rendering-expert`: window, DPI, swap chain, DirectWrite, glyph atlas, input/IME, UIA.
- `windows-systems-rust-expert`: raw Windows calls, `platform_windows`, process and handle custody.
- `testing-fuzzing-conformance-expert`: conformance suites, fuzzing parsers and the console server.
- `idiomatic-rust-api-design-expert`: public API changes to `rusty_term_core` or `platform_windows`.

# Standards
- `rust`
- `interface`
- `gui`

# Project rules
- **Must:** changes to `Grid`'s public surface are public-API changes. Flag them; they need the Approver. (Shared with rusty_conhost.)
- **Must:** all raw Windows calls live in `platform_windows`; domain crates use its safe API. A new raw call lands there with a test.
- **Must:** console clients are hostile. Validate every length, rectangle, handle and code page; bound retained memory per client and per wait.
- **Must:** perf claims state the workload (plain text, cursor-heavy, scroll-heavy), machine and commit, against the libghostty-vt baselines.
- **Should:** minimal dependencies; prefer `windows-sys` or a checked-in `windows-bindgen` subset.
- **Should:** threads over async for ConPTY I/O unless a measured reason says otherwise.
- Recorded decisions in the design doc (§5–§7) are design questions, not defects.

# Role notes
- Planner: name the conhost behavior being matched and the oracle used to confirm it.
- Architect: say which layer (client, ConDrv, server dispatch, host semantics, parser, buffer, ConPTY, renderer) each change touches.
- Builder: probes go in a scratch copy, never the working tree. Give exact PowerShell repro commands.
- Tester: boundary cases include last column, wide pairs, margins, split UTF-8/UTF-16/ESC sequences, resize mid-output. Extend `rt-caps.sh` instead of ad hoc checks; re-run it on `main` before reporting a gap.
- Reviewer: hunt robustness first (containment, retained memory, echo amplification, split boundaries, child custody); lower severity for narrow triggers.

# Oracles and tools
- Oracle: conhost under ConPTY (OpenConsole at a pinned commit), not windowed inbox conhost.
- Secondary oracles: cmd.exe, PowerShell/PSReadLine, .NET console, crossterm consumers.
- `rt-caps.sh` capability-gap probe; libghostty-vt throughput baselines.
- Windows CI is manual; local shell is PowerShell.
