import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
from check_skills import check_repo  # noqa: E402

USER_POLICY = "policy:\n  allow_implicit_invocation: false\n"


class CheckSkillsTest(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp())
        (self.root / "skills").mkdir()
        self.readme = ""

    def add_skill(self, name, body="Steps.", extra="", policy="", folder=None):
        path = self.root / "skills" / (folder or name)
        (path / "agents").mkdir(parents=True)
        (path / "SKILL.md").write_text(
            f"---\nname: {name}\ndescription: Does a thing.\n{extra}---\n\n{body}\n")
        (path / "agents" / "openai.yaml").write_text("interface:\n  display_name: x\n" + policy)
        self.readme += f"- [{name}](skills/{folder or name}/SKILL.md)\n"

    def problems(self):
        (self.root / "README.md").write_text(self.readme)
        return check_repo(self.root)

    def test_valid_skills_pass(self):
        self.add_skill("grilling")
        self.add_skill("grill-me", body="Load the `grilling` skill with your skill tool.",
                       extra="disable-model-invocation: true\n", policy=USER_POLICY)
        self.assertEqual(self.problems(), [])

    def test_name_must_match_folder(self):
        self.add_skill("grilling", folder="grill")
        self.assertIn("skills/grill: name 'grilling' must match the folder name", self.problems())

    def test_user_invoked_flags_must_agree(self):
        self.add_skill("grill-me", extra="disable-model-invocation: true\n")
        self.assertIn("skills/grill-me: disable-model-invocation and agents/openai.yaml policy disagree",
                      self.problems())

    def test_reference_to_missing_skill(self):
        self.add_skill("grill-me", body="Load the `grilling` skill with your skill tool.")
        self.assertIn("skills/grill-me: refers to the `grilling` skill, which does not exist",
                      self.problems())

    def test_reference_to_user_invoked_skill(self):
        self.add_skill("grill-me", extra="disable-model-invocation: true\n", policy=USER_POLICY)
        self.add_skill("code-review", body="Load the `grill-me` skill with your skill tool.")
        self.assertIn("skills/code-review: refers to the `grill-me` skill, but only a person can start it",
                      self.problems())

    def test_broken_link(self):
        self.add_skill("tdd", body="See [tests](references/tests.md).")
        self.assertIn("skills/tdd: broken link 'references/tests.md' in SKILL.md", self.problems())

    def test_skill_missing_from_readme(self):
        self.add_skill("tdd")
        self.readme = ""
        self.assertIn("skills/tdd: not linked from README.md", self.problems())

    def test_em_dash(self):
        self.add_skill("tdd", body="Red \u2014 then green.")
        self.assertIn("skills/tdd: SKILL.md uses an em dash", self.problems())

    def test_missing_frontmatter(self):
        self.add_skill("tdd")
        (self.root / "skills" / "tdd" / "SKILL.md").write_text("No header.")
        self.assertEqual(self.problems(), ["skills/tdd: SKILL.md must start with a --- frontmatter block"])


if __name__ == "__main__":
    unittest.main()
