# Expert catalog

This folder holds 59 generic domain-expert agent prompts, written from `_BRIEF.md`. None of the prompts is tied to a project; overlays bind them to repos. Each file is a Claude Code subagent definition (`name` and `description` frontmatter), so it can go straight into `.claude/agents/`.

All of them share one structure: Role, Ground rules (authority ranking, citations, version stamps, evidence over intuition), Knowledge map, How you work, and Output contract. They tag claims by source, and anything not checked on the web as of November 1, 2026 is marked **[recall]**.

Supporting files:
- `_BRIEF.md` is the brief the experts were written from. Reuse it to add new experts.
- Which project bullets each expert came from is recorded in `overlays/_catalog-sources.md`. It is project-side, so it stays out of this folder.
- The project-binding sections taken out of the first three experts now live in `overlays/_seed-from-catalog.md`.

## Experts

| Expert | Covers |
|---|---|
| **Agents and memory** | |
| `mcp-agent-tool-design-expert` | MCP and agent tool design |
| `agent-memory-modeling-expert` | Agent memory modelling |
| `retrieval-search-expert` | Retrieval and search |
| `agent-engineering-expert` | Agent engineering across tools |
| `agent-security-threat-modeling-expert` | Agent security: authority limits, prompt injection |
| `distributed-coordination-expert` | Distributed state, concurrency, claiming and hand-off |
| **Evaluation, review and testing** | |
| `llm-agent-evaluation-expert` | Evaluation design for LLM agents |
| `experiment-design-statistics-expert` | Experiment design and measurement discipline |
| `defect-mining-expert` | Mining defect patterns |
| `code-review-operations-expert` | Review operations |
| `testing-fuzzing-conformance-expert` | Testing discipline: fuzzing, conformance |
| **Rust core** | |
| `idiomatic-rust-api-design-expert` | Idiomatic Rust, type-driven design, panic-free libraries |
| `rust-performance-engineering-expert` | Systems Rust performance |
| `concurrency-correctness-expert` | Lock-free design, memory ordering |
| `async-runtime-internals-expert` | Executor and waker internals |
| `async-runtime-migration-expert` | Runtime interop and large workspace migrations |
| **OS, I/O and protocols** | |
| `os-io-multiplexing-expert` | OS I/O layers |
| `filesystem-io-performance-expert` | Filesystem and I/O internals |
| `process-supervision-pty-expert` | Cross-platform PTYs, process supervision |
| `remote-session-protocol-expert` | Remote and network session protocols |
| `binary-format-parsing-expert` | Binary formats and parsers |
| **Windows and terminals** (written first) | |
| `windows-console-expert` | Windows console internals |
| `terminal-emulation-expert` | Terminal emulation |
| `windows-systems-rust-expert` | Systems Rust on Windows |
| `windows-gui-rendering-expert` | Native Windows GUI: DPI, DXGI, DirectWrite, glyph atlas, IME, UIA |
| **Services and data** | |
| `rust-web-services-expert` | Production Rust web services |
| `api-contract-evolution-expert` | API contracts |
| `relational-storage-expert` | Data modelling, storage layer, SQLite/Postgres/pgvector |
| `oauth-identity-expert` | OAuth for remote connectors, token lifecycle |
| `typescript-web-ui-expert` | TypeScript web UI |
| **Build and CI** | |
| `rust-build-performance-expert` | Tuned large Cargo workspaces |
| `cargo-workspace-architecture-expert` | Monorepo and repo splitting, workspace migration order |
| `github-actions-ci-expert` | GitHub Actions at scale, CI and merge queues |
| `ci-runner-infrastructure-expert` | Self-hosted and ephemeral runners |
| `ci-finops-expert` | CI cost management |
| **Platform, ops and data safety** | |
| `sandbox-isolation-expert` | Isolation and virtualization, sandboxing untrusted code |
| `storage-durability-backup-expert` | Storage, durability and backup |
| `linux-single-host-ops-expert` | Running a single Linux host, systemd deploys |
| `hashing-dedup-expert` | Hashing and deduplication |
| `privacy-sensitive-data-expert` | Privacy and health data security |
| **Compilers and languages** | |
| `ownership-inference-expert` | Ownership and memory analysis |
| `gradual-typing-inference-expert` | Type systems for dynamic languages |
| `compiler-backend-codegen-expert` | Native backends |
| `language-design-expert` | Language design judgement |
| **ML, RL and simulation** | |
| `continual-learning-expert` | Catastrophic forgetting and replay; non-stationary environments |
| `model-based-rl-exploration-expert` | Model-based RL and exploration |
| `bio-plausible-learning-expert` | Biologically plausible learning |
| `rl-environment-engineering-expert` | RL and ML environment engineering |
| `game-physics-simulation-expert` | Game physics fidelity |
| `rocket-league-ecosystem-expert` | Game modding and research scene |
| **Product and architecture** | |
| `flow-metrics-kanban-expert` | Built flow and kanban tools |
| `devtools-product-expert` | Pragmatic product calls for developer tools |
| `competitive-analysis-roadmap-expert` | Product strategy and roadmaps |
| `enterprise-architecture-expert` | Enterprise architecture |
| `product-reverse-engineering-expert` | Inferring data models and APIs |
| `clean-room-ip-compliance-expert` | Legal and ethical lines; licence compatibility of ported code |
| **Regulated domains** | |
| `clinical-informatics-expert` | Clinical informatics |
| `va-disability-claims-expert` | VA disability claims |
| `document-extraction-ocr-expert` | Document extraction |

## Not turned into an expert

- **Domain depth to judge findings:** the domain experts themselves cover this.

## Known caveats

- Most files are 150–250 lines rather than the brief's 250–350. They're about the same size in bytes as the first three, though: the lines are longer and use tables more.
- Fast-changing facts were checked on the web, but some workers hit search limits. Anything they couldn't confirm is tagged **[recall]**. Check those before relying on them, especially version numbers, kernel versions, and game constants.
