"""Tests for tools.check, plus the real repo passing it."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from tools import check

REPO = Path(__file__).resolve().parent.parent


def write(root: Path, rel: str, text: str) -> Path:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def agent(name: str, body: str = "body") -> str:
    return f"---\nname: {name}\ndescription: does things\n---\n\n{body}\n"


class FrontmatterTest(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(tempfile.mkdtemp())

    def test_valid(self) -> None:
        path = write(self.root, "roles/planner.md", agent("planner"))
        self.assertEqual(check.check_frontmatter(path), [])

    def test_missing(self) -> None:
        path = write(self.root, "roles/planner.md", "# no frontmatter\n")
        self.assertEqual([p.message for p in check.check_frontmatter(path)], ["missing frontmatter"])

    def test_name_mismatch_and_no_description(self) -> None:
        path = write(self.root, "roles/planner.md", "---\nname: plan\n---\n")
        messages = [p.message for p in check.check_frontmatter(path)]
        self.assertEqual(len(messages), 2)
        self.assertIn("file stem", messages[0])


class LeakTest(unittest.TestCase):
    def test_flags_private_term_case_insensitively(self) -> None:
        root = Path(tempfile.mkdtemp())
        path = write(root, "knowledge/x.md", agent("x", "Used by Rusty_Term."))
        self.assertEqual(len(check.check_leaks(path)), 1)

    def test_word_boundary(self) -> None:
        root = Path(tempfile.mkdtemp())
        path = write(root, "knowledge/x.md", agent("x", "Timers in nanoseconds."))
        self.assertEqual(check.check_leaks(path), [])

    def test_clean_file(self) -> None:
        root = Path(tempfile.mkdtemp())
        path = write(root, "knowledge/x.md", agent("x", "Uses microsoft/terminal."))
        self.assertEqual(check.check_leaks(path), [])


class OverlayTest(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(tempfile.mkdtemp())
        write(self.root, "knowledge/windows-console-expert.md", agent("windows-console-expert"))
        write(self.root, "standards/rust.md", agent("rust"))

    def overlay(self, experts: str, standards: str, project: str = "demo") -> Path:
        text = f"---\nproject: {project}\n---\n\n# Experts\n{experts}\n\n# Standards\n{standards}\n"
        return write(self.root, "overlays/demo.md", text)

    def test_valid_references(self) -> None:
        path = self.overlay("- `windows-console-expert`: always", "- `rust`")
        self.assertEqual(check.check_overlay(path, self.root), [])

    def test_unknown_expert_and_standard(self) -> None:
        path = self.overlay("- `no-such-expert`", "- `cobol`")
        self.assertEqual(len(check.check_overlay(path, self.root)), 2)

    def test_missing_project(self) -> None:
        path = self.overlay("", "", project="")
        self.assertIn("project", check.check_overlay(path, self.root)[0].message)


class ThreadsTest(unittest.TestCase):
    def test_missing_and_orphan(self) -> None:
        root = Path(tempfile.mkdtemp())
        write(root, "roles/planner.md", agent("planner"))
        write(root, "roles/_protocol.md", "protocol")
        write(root, "threads/builder.md", "# Builder thread")
        write(root, "threads/_loop.md", "loop")
        messages = sorted(p.message for p in check.check_threads(root))
        self.assertEqual(len(messages), 2)
        self.assertTrue(any("planner" in m for m in messages))
        self.assertTrue(any("builder" in m for m in messages))


class RepoTest(unittest.TestCase):
    def test_repo_passes(self) -> None:
        problems = check.run(REPO)
        self.assertEqual(problems, [], "\n".join(map(str, problems)))


if __name__ == "__main__":
    unittest.main()
