# Expert catalog

This folder holds 59 generic domain-expert agent prompts, built from the hiring profiles in `Expert_Agents.md`. Overlapping bullets were merged into one expert each. None of the prompts is tied to a project; a separate domain layer will bind them to repos. Each file is a Claude Code subagent definition (`name` and `description` frontmatter), so it can go straight into `.claude/agents/`.

All of them share one structure: Role, Ground rules (authority ranking, citations, version stamps, evidence over intuition), Knowledge map, How you work, and Output contract. They tag claims by source, and anything not checked on the web as of November 1, 2026 is marked **[recall]**.

Supporting files:
- `_BRIEF.md` is the brief the experts were written from. Reuse it to add new experts.
- The project-binding sections taken out of the first three experts now live in `overlays/_seed-from-catalog.md`.

## Experts and the bullets they came from

| Expert | Source (project: bullet) |
|---|---|
| **Agents and memory** | |
| `mcp-agent-tool-design-expert` | Mill Board: coordinated agents · Tick: MCP/agent tooling · Remind-me: shipped agent tooling · Mux: product sense for agent tooling · Agent Cloud: agent tooling |
| `agent-memory-modeling-expert` | Remind-me: memory modeling |
| `retrieval-search-expert` | Remind-me: retrieval |
| `agent-engineering-expert` | Expert Agents: agent engineering across tools |
| `agent-security-threat-modeling-expert` | Agent Cloud: security · Expert Agents: authority limits, prompt injection |
| `distributed-coordination-expert` | BBP_SWF: distributed state and concurrency · Mill Board: claiming and hand-off |
| **Evaluation, review and testing** | |
| `llm-agent-evaluation-expert` | Expert Agents: evaluation design · BBP_SWF: experiment design for LLM agents |
| `experiment-design-statistics-expert` | Apprentice: sound experiment design · Rocket League: measurement discipline |
| `defect-mining-expert` | Expert Agents: mining defect patterns |
| `code-review-operations-expert` | Expert Agents: review operations |
| `testing-fuzzing-conformance-expert` | Rusty Term: testing discipline |
| **Rust core** | |
| `idiomatic-rust-api-design-expert` | PythRust: Rust fluency · Tick: type-driven design · BBP_SWF: panic-free library code |
| `rust-performance-engineering-expert` | Mux: systems Rust · Fclone: systems Rust · Rocket League: systems Rust |
| `concurrency-correctness-expert` | Mux: lock-free rendering · Tokio: loom bonus |
| `async-runtime-internals-expert` | Tokio: executor and waker internals |
| `async-runtime-migration-expert` | Tokio: interop with tokio-only libraries; large workspace migrations |
| **OS, I/O and protocols** | |
| `os-io-multiplexing-expert` | Tokio: OS I/O layers |
| `filesystem-io-performance-expert` | Fclone: filesystem and I/O internals |
| `process-supervision-pty-expert` | Mux: cross-platform PTYs · BBP_SWF: process supervision and PTY |
| `remote-session-protocol-expert` | Mux: remote and network protocols |
| `binary-format-parsing-expert` | Rocket League: binary formats for the replay parser |
| **Windows and terminals** (written first) | |
| `windows-console-expert` | Rusty Term: Windows console internals |
| `terminal-emulation-expert` | Rusty Term: terminal emulation · Mux: terminal-emulator internals |
| `windows-systems-rust-expert` | Rusty Term: systems Rust on Windows |
| `windows-gui-rendering-expert` | Added 2026-11-01: native Windows GUI, DPI, DXGI, DirectWrite, glyph atlas, IME, UIA (gap found when binding Rusty Term) |
| **Services and data** | |
| `rust-web-services-expert` | Mill Board: production Rust web services · Tick: Rust services · Remind-me: systems |
| `api-contract-evolution-expert` | Tick: API contracts |
| `relational-storage-expert` | Tick: data modeling · Mill Board: storage layer · Remind-me: SQLite/Postgres/pgvector |
| `oauth-identity-expert` | Remind-me: OAuth for remote connectors · Agent Cloud: token lifecycle |
| `typescript-web-ui-expert` | Tick: TypeScript web UI |
| **Build and CI** | |
| `rust-build-performance-expert` | Repo Mgmt: tuned large Cargo workspaces |
| `cargo-workspace-architecture-expert` | Tick: monorepo and repo splitting · Tokio: workspace migration order |
| `github-actions-ci-expert` | Repo Mgmt: GitHub Actions at scale · BBP_SWF: CI and merge queues |
| `ci-runner-infrastructure-expert` | Repo Mgmt: self-hosted and ephemeral runners |
| `ci-finops-expert` | Repo Mgmt: CI FinOps |
| **Platform, ops and data safety** | |
| `sandbox-isolation-expert` | Agent Cloud: isolation and virtualization · BBP_SWF: sandboxing untrusted code |
| `storage-durability-backup-expert` | Agent Cloud: storage and durability · Fclone: data-safety mindset |
| `linux-single-host-ops-expert` | Agent Cloud: running a single box · Mill Board: systemd deploys |
| `hashing-dedup-expert` | Fclone: hashing know-how |
| `privacy-sensitive-data-expert` | Remind-me: privacy · MediBoard: health data privacy and security |
| **Compilers and languages** | |
| `ownership-inference-expert` | PythRust: ownership and memory analysis |
| `gradual-typing-inference-expert` | PythRust: type systems for dynamic languages |
| `compiler-backend-codegen-expert` | PythRust: native backends |
| `language-design-expert` | PythRust: language design judgment |
| **ML, RL and simulation** | |
| `continual-learning-expert` | Apprentice: catastrophic forgetting and replay; non-stationary environments |
| `model-based-rl-exploration-expert` | Apprentice: model-based RL and exploration |
| `bio-plausible-learning-expert` | Apprentice: biologically plausible learning |
| `rl-environment-engineering-expert` | Rocket League: RL/ML-environment extras |
| `game-physics-simulation-expert` | Rocket League: game physics fidelity |
| `rocket-league-ecosystem-expert` | Rocket League: modding and research scene |
| **Product and architecture** | |
| `flow-metrics-kanban-expert` | Mill Board: built flow and kanban tools |
| `devtools-product-expert` | Mill Board: pragmatic product calls |
| `competitive-analysis-roadmap-expert` | Reverse: product strategist |
| `enterprise-architecture-expert` | Reverse: enterprise architecture domain |
| `product-reverse-engineering-expert` | Reverse: inferring data models and APIs |
| `clean-room-ip-compliance-expert` | Reverse: legal and ethical lines · Expert Agents: licence compatibility of ported code |
| **Regulated domains** | |
| `clinical-informatics-expert` | MediBoard: clinical informatics |
| `va-disability-claims-expert` | MediBoard: VA disability claims |
| `document-extraction-ocr-expert` | MediBoard: document extraction |

## Not turned into an expert

- **Expert Agents, "enough domain depth to judge findings":** the domain experts themselves cover this.
- **Rusty MMDB:** the doc has no profile for it yet.

## Known caveats

- Most files are 150–250 lines rather than the brief's 250–350. They're about the same size in bytes as the first three, though: the lines are longer and use tables more.
- Fast-changing facts were checked on the web, but some workers hit search limits. Anything they couldn't confirm is tagged **[recall]**. Check those before relying on them, especially version numbers, kernel versions, and Rocket League game constants.
