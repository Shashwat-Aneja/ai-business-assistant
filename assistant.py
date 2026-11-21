import re
import argparse
import json
import unicodedata


def normalize_topic(text):
    if not isinstance(text, str):
        raise ValueError("Business queries must be text.")
    return " ".join(re.sub(r"[\W_]+", " ", unicodedata.normalize("NFKC", text).casefold()).split())


def respond(query):
    query = normalize_topic(query)

    responses = {
        "profit": "Profit = Revenue - Expenses",
        "revenue": "Revenue = Units Sold × Selling Price",
        "profit margin": "Profit Margin = (Profit / Revenue) × 100",
        "roi": "ROI = (Net Profit / Cost of Investment) × 100",
        "kpi": "KPI stands for Key Performance Indicator. Examples: revenue growth, profit margin, churn rate.",
        "increase revenue": "Improve marketing, optimize pricing, expand reach, or introduce new products.",
        "reduce expenses": "Negotiate vendor costs, optimize resources, use automation tools.",
        "business growth": "Focus on customer retention, efficiency, product innovation, and analytics.",
        "automation": "Automation improves efficiency by reducing manual work using software and AI systems.",
        "break-even point": "Break-even point = Fixed Costs / (Selling Price per Unit - Variable Cost per Unit).",
        "cash flow": "Net Cash Flow = Cash Inflows - Cash Outflows. Track timing as well as totals to anticipate shortfalls.",
        "gross margin": "Gross Margin = ((Revenue - Cost of Goods Sold) / Revenue) × 100. Revenue must be non-zero.",
        "working capital": "Working Capital = Current Assets - Current Liabilities. Positive working capital generally supports short-term obligations; compare it with operating cash needs.",
        "current ratio": "Current Ratio = Current Assets / Current Liabilities. A ratio above 1 generally means current assets exceed current liabilities; interpret it alongside cash-flow timing and industry norms.",
        "quick ratio": "Quick Ratio = (Cash + Marketable Securities + Accounts Receivable) / Current Liabilities. It excludes inventory and other less-liquid current assets.",
        "debt-to-equity ratio": "Debt-to-Equity Ratio = Total Debt / Shareholders' Equity. Interpret the result against the company's industry and financing model.",
        "operating margin": "Operating Margin = (Operating Income / Revenue) × 100. Revenue must be non-zero.",
    }

    # Match the most specific topic first and avoid partial-word matches.
    for key in sorted(responses, key=len, reverse=True):
        normalized_key = normalize_topic(key)
        if re.search(rf"\b{re.escape(normalized_key)}\b", query):
            return responses[key]

    return "I’m not trained for that yet. Try asking about profit, ROI, KPI, revenue, break-even point, cash flow, liquidity ratios, or operating margin."


def main(argv=()):
    parser = argparse.ArgumentParser(description="Look up rule-based business guidance")
    parser.add_argument("query", nargs="?", help="Answer one query without entering the interactive loop")
    parser.add_argument("--json", action="store_true", help="Emit a machine-readable single-query answer")
    args = parser.parse_args(argv)
    if args.query is not None:
        answer = respond(args.query)
        print(json.dumps({"query": args.query, "answer": answer}, ensure_ascii=False) if args.json else answer)
        return 0
    if args.json:
        parser.error("--json requires a query")
    print("\n=== AI Business Assistant ===")
    print("Type 'exit' to quit.\n")

    while True:
        try:
            query = input("> ")
        except (EOFError, KeyboardInterrupt):
            print("\nAssistant: Goodbye!")
            break
        if query.strip().casefold() in ["exit", "quit"]:
            print("Assistant: Goodbye!")
            break
        print("Assistant:", respond(query))


if __name__ == "__main__":
    import sys
    main(sys.argv[1:])

