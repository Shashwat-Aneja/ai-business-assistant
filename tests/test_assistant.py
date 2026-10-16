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


    def test_normalizes_repeated_whitespace(self):
        self.assertEqual(
            respond("  what   is   profit margin?  "),
            "Profit Margin = (Profit / Revenue) × 100",
        )

    def test_topic_matching_does_not_match_inside_larger_words(self):
        self.assertIn("not trained", respond("Explain profitability trends"))

    def test_break_even_point_returns_unit_contribution_formula(self):
        self.assertEqual(
            respond("How do I calculate the break-even point?"),
            "Break-even point = Fixed Costs / (Selling Price per Unit - Variable Cost per Unit).",
        )


if __name__ == "__main__":
    unittest.main()
