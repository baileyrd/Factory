---
name: gui
description: House standard for anything the user sees or does on screen (windows, rendering, fonts, input, settings, dialogs). Musts are blockable; shoulds are flagged.
version: 0.1
owner: Approver
---

# Scope
Any card that touches what the user sees or does on screen. Domain specifics (for example terminal escape sequences) stay with the domain experts. Pair with `windows-gui-rendering-expert` on Windows, `typescript-web-ui-expert` on the web.

# Musts
- The UI thread never blocks; I/O and heavy work run off it.
- Input is never lost or reordered: keyboard, mouse, IME, clipboard.
- Rendering is correct at any DPI and scale, and survives resizing and moving between monitors.
- Unicode text is correct: wide characters, combining marks, emoji, font fallback.
- Accessible: keyboard-only operation, a screen-reader path, system contrast settings respected.
- Settings save safely and validate on load; a bad config falls back to defaults with a visible notice.
- UI state is separate from domain logic; the view renders state and doesn't own it.

# Shoulds
- A defined, measured performance budget: frame time, input latency, startup time. The Planner sets the numbers per project.
- Platform conventions for shortcuts, dialogs and theming (light, dark, high contrast).
- User-facing errors say what happened and what to do next.
- Settings apply live where possible.
- Minimal dialogs with sensible defaults.

# Mistakes to avoid
Work on the UI thread; hardcoded pixel sizes; assuming one character is one cell or one byte; redrawing everything every frame; restart-required settings without reason; mouse-only features.

# Role notes
- Planner: performance budgets and accessibility needs in the acceptance criteria.
- Architect: separate state, rendering and input layers.
- Tester: snapshot/golden-image tests for rendering, input replay, DPI and resize cases, benchmarks against the budget.
- Reviewer: check platform conventions and budgets.

# Review checklist
UI thread free · DPI and resize tested · Unicode cases covered · keyboard-only path works · screen reader reads it · budgets measured · config validated.

# References
Platform UI and accessibility guidelines; the project's budgets.
