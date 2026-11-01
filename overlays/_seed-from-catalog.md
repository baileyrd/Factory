# Domain-layer seed: project bindings removed from the generic catalog

## From windows-console-expert


When the task concerns Nano's rusty_conhost (own console host, issue #1222) or rusty_mux's `RUSTY_CONSOLE_HOST=own|conpty` switch:

- **Oracle:** conhost under ConPTY (OpenConsole at a pinned commit), not windowed inbox conhost.
- **Past real findings were robustness bugs, not parity bugs.** They were per-call containment, retained-memory accounting, cooked-read echo amplification, ESC and UTF-16 split boundaries, and child custody. Hunt for those first.
- **Threat model:** client processes are hostile. Terminal-side input is the user's, so it is trusted but must still be capped.
- **Recorded decisions count as decisions.** Decisions in the design doc's §5–§7 are design questions, not defects.
- **Severity:** lower it for narrow triggers.
- **Probes:** probe in a scratch copy, never in the working tree.
- **Delivery:** findings go to the thread that owns the PR, not as GitHub comments, unless told otherwise.

## From terminal-emulation-expert


When the task concerns Nano's rusty_term (a Rust terminal) or its core crate:

- `rusty_term_core::Grid` is shared with rusty_conhost (the console host built on top of Grid). Changes to Grid's public surface are public-API changes, so flag them and ask before making them.
- `rt-caps.sh` is the project's capability-gap probe. Extend it rather than writing ad hoc checks, and re-run it on `main` to confirm a gap before reporting it.
- The project has throughput baselines against libghostty-vt. Perf claims must state the workload (plain text, cursor-heavy, scroll-heavy), the machine and the commit.
- Follow the repo conventions: Rust with `Result` and `?` and no `unwrap()` outside tests, small single-purpose functions, tests for each behavior change (happy path plus boundary cases such as the last column, wide pairs, margins and split UTF-8), and focused diffs.

## From windows-systems-rust-expert


When the task concerns Nano's rusty_mill repos (rusty_conhost, rusty_mux's Windows port, rusty_term's Windows backends, and the shared `platform_windows` crate):

- All raw Windows calls live in `platform_windows` (for example, its `condrv` module, the ConPTY wrapper, and process/job helpers). Domain crates use the safe API only. A new raw call goes there with a test.
- rusty_conhost is std-first Rust that opens `\Device\ConDrv\Server` through the native API. Its ConDrv layouts are **[RE]**. Pair this agent with the Windows console expert for ConDrv semantics.
- rusty_mux runs ConPTY with dedicated reader and writer threads over AF_UNIX sockets. That's the deliberate threads-over-async choice, so don't propose a runtime without a measured reason.
- Minimal dependencies: prefer `windows-sys` or a checked-in `windows-bindgen` subset, and justify any new crate. Changes to public APIs, toolchains or dependencies need Nano's approval before they land.
- Windows CI is manual (D4) and the local machine runs PowerShell. Provide the exact PowerShell repro or test command.
