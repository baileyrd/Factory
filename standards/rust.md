---
name: rust
description: House standard for Rust code. Load for any card that writes or changes Rust. Musts are blockable by the Reviewer; shoulds are flagged.
version: 0.1
owner: Approver
---

# Scope
Any card that writes or changes Rust code. Pair with `idiomatic-rust-api-design-expert` for depth.

# Musts
- Library code uses `Result` and `?`. No `unwrap()`, `expect()` or `panic!` outside tests and prototypes.
- Never silently swallow errors: handle, propagate with context, or log.
- Make illegal states unrepresentable: enums, newtypes, typestate over runtime flags.
- No `unsafe` without a `// SAFETY:` comment and a test that exercises it.
- Validate external input at the boundary.
- Never log or commit secrets.
- Passes `cargo fmt --check`, `cargo clippy -- -D warnings` and `cargo test`.
- Every new dependency has a written justification.

# Shoulds
- Ownership and borrowing over `clone()` or `Rc<RefCell<_>>`.
- Flat control flow: guard clauses, early returns, at most 3 levels of nesting.
- Short, single-purpose functions; composition through traits.
- Async only where there is real I/O concurrency.
- Doc comments on the public API past the spike stage.
- Domain logic free of I/O (ports and adapters).
- No abstraction before two real call sites.

# Mistakes to avoid
Cloning to silence the borrow checker; stringly-typed errors; giant `match` arms; `Arc<Mutex<_>>` by reflex; framework types leaking into the domain.

# Role notes
- Planner: state error cases and failure behavior in acceptance criteria.
- Builder: focused diffs, match existing conventions.
- Tester: happy path, failure and boundary cases; property tests where inputs are wide.
- Reviewer: enforce musts, flag shoulds.

# Review checklist
No `unwrap`/`expect` in library code · errors carry context · clippy clean · every `unsafe` justified and tested · new dependencies justified · public items documented · failure paths tested.

# References
Rust API Guidelines; Clippy lint docs.
