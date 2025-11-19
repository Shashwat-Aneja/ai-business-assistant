def respond(query):
    query = query.lower()

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
    }

    for key in responses:
        if key in query:
            return responses[key]

    return "I’m not trained for that yet. Try asking about profit, ROI, KPI, revenue, or automation."


def main():
    print("\n=== AI Business Assistant ===")
    print("Type 'exit' to quit.\n")

    while True:
        query = input("> ")
        if query.lower() in ["exit", "quit"]:
            print("Assistant: Goodbye!")
            break
        print("Assistant:", respond(query))


if __name__ == "__main__":
    main()
