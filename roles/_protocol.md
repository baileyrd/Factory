# Factory protocol

The contract every role works inside. Roles never move a card past a gate; only the Approver does.

## Layers

| Layer | What it holds | Where it lives |
|---|---|---|
| Roles | Planner, Architect, Builder, Reviewer, Tester, Retro | `roles/` |
| Knowledge | Generic domain experts (catalog format) | `knowledge/` |
| Standards | House rules: musts (blockable) and shoulds (flagged) | `standards/` |
| Overlay | Per project: which knowledge and standards, project rules, per-role notes, oracles | the project's repo, `.factory/overlay.md` (drafts in `overlays/`) |

An overlay adds and tightens. It never removes a base rule, a gate or separation of duties.

Which model fills a role is configuration, not part of this protocol.

## Flow

See `docs/factory-map.svg`.

```
Planner ─► Architect ─► [Gate 1] ─► Builder ─► V&V Test ─► [Gate 2] ─► Done ─► Retro
   │           │                     ▲            │
   └─ Tester and Reviewer alongside, from the first requirement ─┘
```

1. **Planner** researches (cited) and writes requirements with acceptance criteria.
2. **Tester** starts the test plan from the requirements. **Reviewer** reviews the requirements.
3. **Architect** writes the design. **Tester** checks it for testability: an untestable design is a blocking finding sent to the Reviewer; anything else goes into the test plan. **Reviewer** reviews the design.
4. **Gate 1**: the Approver approves the design.
5. **Tester** writes the tests first; they fail. **Reviewer** reviews them.
6. **Builder** makes the tests pass and writes code docs and user guides. **Reviewer** reviews code and docs: blocks on musts, flags shoulds.
7. **V&V Test** (run by the Tester): the full suite from unit through end to end, every user guide followed step by step, acceptance criteria checked. **Reviewer** reviews the results.
8. **Gate 2**: the Approver approves the merge.
9. **Retro** runs after every card, whatever the outcome.

## Gates

- Two human gates, held by the Approver: **design approval** and **merge approval**.
- The Approver sees only artifacts the Reviewer has already reviewed, plus the Reviewer's flagged shoulds for decision.
- Approvals are recorded verbatim with who approved and when.

## Separation of duties

- No one reviews or tests their own work. The Reviewer and Tester are never the Builder.
- Reviewer and Tester never share a model provider with the Builder of the same card.
- Disputes between Builder and Tester go to the Reviewer. They never settle it between themselves.

## Retries and escalation

- The Builder gets six attempts to make the tests pass. After that the card goes **Blocked** with a summary.
- Before Blocked, the Builder may **challenge a test** with evidence. The Reviewer decides: wrong test → Tester fixes it; right test → Builder continues.
- Any role can raise a **question for the Approver**. It parks the card; it doesn't count as a retry.

## Handoff block

Every role ends its turn with this block, posted as a card comment. `next` routes the card to the next thread.

```
handoff:
  role: <planner|architect|builder|reviewer|tester|retro>
  card: <id>
  stage: <requirements|design|tests|build|vv-test|retro>
  status: <done|blocked|needs-approval|challenge>
  artifacts: [<path or link>, ...]
  blocking: [<finding>, ...]      # musts; empty when none
  flags: [<finding>, ...]         # shoulds, for the Approver
  next: <role or gate-1|gate-2>
  notes: <one or two lines>
```

## Loading context

At the start of a card each role loads, in order: this protocol, its role file, the project overlay, then only the knowledge and standards the overlay lists **and the card touches**.

If a benched project agent exists for this role and project in Expert-Agents (`experts/<project>` for the Reviewer, `developers/<project>` for the Builder), it is used in place of the base role file. The protocol, handoff block and gates still apply.
