"""Catalog checks: frontmatter, project leaks in generic layers, overlay references, thread coverage.

Run: python3 -m tools.check [repo_root]
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

GENERIC_DIRS: tuple[str, ...] = ("roles", "knowledge", "standards")
PRIVATE_TERMS: tuple[str, ...] = (
    "nano", "baileyrd", "rusty_", "rusty-", "mill board", "mill_board", "remind-me",
    "pythrust", "mediboard", "dottius", "baileyai", "rusty mill",
)
_FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
_BACKTICKED = re.compile(r"`([a-z0-9][a-z0-9-]*)`")


@dataclass(frozen=True)
class Problem:
    """One failed check, tied to a file."""

    path: Path
    message: str

    def __str__(self) -> str:
        return f"{self.path}: {self.message}"


def frontmatter(text: str) -> dict[str, str]:
    """Return simple `key: value` frontmatter pairs, or {} when there is none."""
    match = _FRONTMATTER.match(text)
    if not match:
        return {}
    pairs = (line.split(":", 1) for line in match.group(1).splitlines() if ":" in line)
    return {key.strip(): value.strip() for key, value in pairs}


def catalog_files(root: Path, folder: str) -> list[Path]:
    """Definition files in a folder: skips README and `_`-prefixed support files."""
    return sorted(
        p for p in (root / folder).glob("*.md")
        if p.name != "README.md" and not p.name.startswith("_")
    )


def check_frontmatter(path: Path) -> list[Problem]:
    """Frontmatter exists, `name` equals the file stem, `description` is set."""
    meta = frontmatter(path.read_text(encoding="utf-8"))
    if not meta:
        return [Problem(path, "missing frontmatter")]
    problems: list[Problem] = []
    if meta.get("name") != path.stem:
        problems.append(Problem(path, f"name {meta.get('name')!r} != file stem {path.stem!r}"))
    if not meta.get("description"):
        problems.append(Problem(path, "missing description"))
    return problems


def check_leaks(path: Path, terms: tuple[str, ...] = PRIVATE_TERMS) -> list[Problem]:
    """Generic files must not name private projects or people (whole words; `rusty_` style terms as prefixes)."""
    text = path.read_text(encoding="utf-8")
    return [
        Problem(path, f"private term {term!r} in a generic file")
        for term in terms
        if _term_pattern(term).search(text)
    ]


def _term_pattern(term: str) -> re.Pattern[str]:
    end = r"\b" if term[-1].isalnum() else ""
    return re.compile(rf"\b{re.escape(term)}{end}", re.IGNORECASE)


def overlay_section(text: str, heading: str) -> str:
    """Body of a `# heading` section, up to the next `# ` heading."""
    match = re.search(rf"^# {re.escape(heading)}\n(.*?)(?=^# |\Z)", text, re.DOTALL | re.MULTILINE)
    return match.group(1) if match else ""


def check_overlay(path: Path, root: Path) -> list[Problem]:
    """An overlay names a project and only references knowledge and standards that exist."""
    text = path.read_text(encoding="utf-8")
    problems: list[Problem] = []
    if not frontmatter(text).get("project"):
        problems.append(Problem(path, "missing `project` in frontmatter"))
    for heading, folder in (("Experts", "knowledge"), ("Standards", "standards")):
        for ref in _BACKTICKED.findall(overlay_section(text, heading)):
            if not (root / folder / f"{ref}.md").exists():
                problems.append(Problem(path, f"{heading}: `{ref}` not found in {folder}/"))
    return problems


def check_threads(root: Path) -> list[Problem]:
    """Every role has a thread prompt, and every thread prompt has a role."""
    roles = {p.stem for p in catalog_files(root, "roles")}
    threads = {p.stem for p in catalog_files(root, "threads")}
    missing = [Problem(root / "threads", f"no thread prompt for role {r!r}") for r in sorted(roles - threads)]
    orphan = [Problem(root / "threads", f"thread {t!r} has no role file") for t in sorted(threads - roles)]
    return missing + orphan


def run(root: Path) -> list[Problem]:
    """All checks over the repo at `root`."""
    problems: list[Problem] = []
    for folder in GENERIC_DIRS:
        for path in catalog_files(root, folder):
            problems += check_frontmatter(path) + check_leaks(path)
    for path in catalog_files(root, "overlays"):
        problems += check_overlay(path, root)
    return problems + check_threads(root)


def main(argv: list[str]) -> int:
    root = Path(argv[1]) if len(argv) > 1 else Path(__file__).resolve().parent.parent
    problems = run(root)
    for problem in problems:
        print(problem)
    print(f"{len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
