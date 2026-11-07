import unittest

from assistant import respond


class FinancialRatioGuidanceTests(unittest.TestCase):
    def test_quick_ratio_excludes_inventory(self):
        answer = respond("How do I calculate the quick ratio?")
        self.assertIn("Cash + Marketable Securities + Accounts Receivable", answer)
        self.assertIn("excludes inventory", answer)

    def test_debt_to_equity_ratio_returns_financing_formula(self):
        answer = respond("Explain the debt-to-equity ratio")
        self.assertIn("Total Debt / Shareholders' Equity", answer)

    def test_operating_margin_returns_profitability_formula(self):
        answer = respond("What is operating margin?")
        self.assertEqual(
            answer,
            "Operating Margin = (Operating Income / Revenue) × 100. Revenue must be non-zero.",
        )

    def test_quick_does_not_match_inside_larger_words(self):
        self.assertIn("not trained", respond("How can we quickly expand sales?"))


    def test_break_even_guidance_explains_non_positive_contribution_margin(self):
        answer = respond("How do I calculate the break-even point?")
        self.assertIn("Selling price must exceed variable cost", answer)
        self.assertIn("no finite break-even volume", answer)

    def test_non_text_queries_return_an_actionable_message(self):
        for query in (None, 42, ["profit"]):
            with self.subTest(query=query):
                self.assertEqual(respond(query), "Please enter a text question.")


if __name__ == "__main__":
    unittest.main()

