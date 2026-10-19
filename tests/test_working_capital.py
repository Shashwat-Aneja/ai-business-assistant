import unittest

from assistant import respond


class WorkingCapitalTests(unittest.TestCase):
    def test_working_capital_query_returns_formula_and_context(self):
        answer = respond("How do I calculate working capital?")
        self.assertIn("Current Assets - Current Liabilities", answer)
        self.assertIn("short-term obligations", answer)

    def test_working_capital_matching_is_case_insensitive(self):
        self.assertIn("Working Capital =", respond("WORKING CAPITAL"))
