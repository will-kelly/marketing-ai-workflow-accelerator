import unittest
from accelerator.core import inspect_copy, make_draft, export_package

class TestWorkflow(unittest.TestCase):
    def test_demo_offline(self):
        self.assertIn("For marketers", make_draft("Brief", "marketers", "Email", ["Claim"]))
    def test_claim_flags(self):
        labels = {f["type"] for f in inspect_copy("Guaranteed 40% faster, best in class.")}
        self.assertIn("quantified_claim", labels)
        self.assertIn("absolute_claim", labels)
        self.assertIn("comparative_claim", labels)
    def test_banned_term_blocks(self):
        flags = inspect_copy("Our solution is zero risk", banned_terms=["zero risk"])
        with self.assertRaises(ValueError):
            export_package("Our solution is zero risk", flags, "A", "Checked", True, "brief", "demo")
    def test_requires_review(self):
        with self.assertRaises(ValueError):
            export_package("Copy", [], "", "", True, "brief", "demo")
    def test_approval(self):
        pkg = export_package("Copy", [], "Editor", "Checked source", True, "brief", "demo")
        self.assertEqual(pkg["status"], "approved_by_human")

if __name__ == "__main__":
    unittest.main()
