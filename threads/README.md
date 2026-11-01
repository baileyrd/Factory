# Role threads

One long-running Claude Code session per base role. Each thread loops on Mill Board: find a card waiting for its role, do the work, post the handoff block, move the card when the role may.

| Thread | Prompt | Board role (today) |
|---|---|---|
| Planner | [planner.md](planner.md) | comment only |
| Architect | [architect.md](architect.md) | comment only |
| Tester | [tester.md](tester.md) | `qa` |
| Builder | [builder.md](builder.md) | `builder` |
| Reviewer | [reviewer.md](reviewer.md) | `reviewer` |
| Retro | [retro.md](retro.md) | comment only |

Every thread follows [_loop.md](_loop.md). The role specifics are in its own prompt.

## Stages on the board

Mill Board has seven columns and no design stage, so stages inside a column are routed by the latest handoff block's `next:` field.

| Stage | Column | Who acts | Leaves by |
|---|---|---|---|
| Requirements | `backlog` | Planner, then Tester (plan) and Reviewer | handoff `next: architect` |
| Design | `backlog` | Architect, then Tester (testability) and Reviewer | handoff `next: gate-1` |
| **Gate 1** | `backlog` → `ready` | **Approver** | Approver moves the card to `ready` |
| Tests first | `ready` | Tester, then Reviewer | handoff `next: builder` |
| Build | `building` | Builder (claims via `card_take`), then Reviewer | Builder moves to `qa` after the Reviewer passes |
| V&V Test | `qa` | Tester (claims), then Reviewer | Tester moves to `review` |
| **Gate 2** | `review` → `done` | **Approver** | Approver merges and moves to `done` |
| Retro | `done` | Retro | handoff only |
| Blocked | `blocked` | Approver | Approver moves it back |

## Starting a thread

1. Workspace: this repo, a clone of `baileyrd/expert-agents` beside it, and clones of the target repos the board serves (`board_projects`).
2. Open a Claude Code session in this repo with Mill Board and remind-me connected.
3. Paste the role's prompt from this folder as the first message. One thread per role; don't run two of the same role.

## Known gaps

- **Board roles don't enforce the protocol yet.** `builder` holds review and merge, and `reviewer` holds merge. Threads are told never to use those, but the board doesn't stop them. Mill Board card 35f928e7 (admin role CRUD) is the fix: add planner, architect, tester and retro roles, and leave merge to `human` only.
- **Planner, Architect and Retro have no board role,** so they comment and never move cards.
- **Provider separation is manual.** Start the Reviewer and Tester threads on a different provider from the Builder thread.
