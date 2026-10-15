import unittest

from assistant import respond


class RespondTests(unittest.TestCase):
    def test_longer_topic_wins_over_shorter_substring(self):
        self.assertEqual(
            respond("What is the profit margin?"),
            "Profit Margin = (Profit / Revenue) × 100",
        )

    def test_matching_is_case_insensitive(self):
        self.assertEqual(respond("ROI"), "ROI = (Net Profit / Cost of Investment) × 100")

    def test_unknown_question_uses_fallback(self):
        self.assertIn("not trained", respond("What is supply chain elasticity?"))

    def test_eof_exits_cleanly(self):
        from unittest.mock import patch
        from io import StringIO
        from contextlib import redirect_stdout
        from assistant import main

        output = StringIO()
        with patch("builtins.input", side_effect=EOFError), redirect_stdout(output):
            main()
        self.assertIn("Goodbye", output.getvalue())


if __name__ == "__main__":
    unittest.main()
