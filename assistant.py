import re


def respond(query):
    query = " ".join(query.casefold().split())

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
    }

    # Match the most specific topic first and avoid partial-word matches.
    for key in sorted(responses, key=len, reverse=True):
        if re.search(rf"\b{re.escape(key)}\b", query):
            return responses[key]

    return "I’m not trained for that yet. Try asking about profit, ROI, KPI, revenue, break-even point, or automation."


def main():
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
    main()
