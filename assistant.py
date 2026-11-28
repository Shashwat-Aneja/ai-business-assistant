import re
import argparse
import json
import unicodedata
from pathlib import Path


RESPONSES = {
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


def available_topics():
    return sorted(RESPONSES)


def normalize_topic(text):
    if not isinstance(text, str):
        raise ValueError("Business queries must be text.")
    return " ".join(re.sub(r"[\W_]+", " ", unicodedata.normalize("NFKC", text).casefold()).split())


def respond(query):
    query = normalize_topic(query)


    # Match the most specific topic first and avoid partial-word matches.
    for key in sorted(RESPONSES, key=len, reverse=True):
        normalized_key = normalize_topic(key)
        if re.search(rf"\b{re.escape(normalized_key)}\b", query):
            return RESPONSES[key]

    return "I’m not trained for that yet. Try asking about profit, ROI, KPI, revenue, break-even point, cash flow, liquidity ratios, or operating margin."


def matching_topics(query):
    normalized = normalize_topic(query)
    candidates = []
    for key in RESPONSES:
        for match in re.finditer(rf"\b{re.escape(normalize_topic(key))}\b", normalized):
            candidates.append((match.start(), match.end(), key))
    accepted = []
    occupied = bytearray(len(normalized))
    for start, end, key in sorted(candidates, key=lambda item: (-(item[1] - item[0]), item[0], item[2])):
        if not any(occupied[start:end]):
            occupied[start:end] = b"\x01" * (end - start)
            accepted.append((start, end, key))
    return list(dict.fromkeys(key for _, _, key in sorted(accepted)))


def query_record(query, all_matches=False):
    record = {"query": query, "answer": respond(query)}
    topics = matching_topics(query) if all_matches else []
    if all_matches:
        record["matches"] = [{"topic": key, "answer": RESPONSES[key]} for key in topics]
        if record["matches"]:
            record["answer"] = "\n".join(item["answer"] for item in record["matches"])
    return record


def read_queries(path):
    # Read a bounded amount even if the file grows after opening.
    with Path(path).open("rb") as handle:
        raw = handle.read(1024 * 1024 + 1)
    if len(raw) > 1024 * 1024:
        raise ValueError("Query file exceeds the 1 MiB budget")
    queries = [line.strip() for line in raw.decode("utf-8-sig").splitlines() if line.strip()]
    if not queries or len(queries) > 1000 or any(len(q) > 16384 for q in queries):
        raise ValueError("Provide 1–1000 nonblank queries of at most 16384 characters")
    return queries


def main(argv=()):
    parser = argparse.ArgumentParser(description="Look up rule-based business guidance")
    parser.add_argument("query", nargs="?", help="Answer one query without entering the interactive loop")
    parser.add_argument("--json", action="store_true", help="Emit a machine-readable single-query answer")
    parser.add_argument("--topics", action="store_true", help="List supported topics without answering a query")
    parser.add_argument("--queries-file", help="Read bounded UTF-8 queries; emit one JSON object per nonblank line")
    parser.add_argument("--all-matches", action="store_true", help="Return distinct nonoverlapping business topics in query order")
    args = parser.parse_args(argv)
    if args.all_matches and (args.topics or (args.query is None and args.queries_file is None)):
        parser.error("--all-matches requires a query or query file")
    if args.queries_file is not None:
        if args.query is not None or args.topics:
            parser.error("--queries-file cannot be combined with a query or --topics")
        try:
            queries = read_queries(args.queries_file)
        except (OSError, UnicodeError, ValueError) as exc:
            parser.error(str(exc))
        for query in queries:
            print(json.dumps(query_record(query, args.all_matches), ensure_ascii=False))
        return 0
    if args.topics:
        if args.query is not None:
            parser.error("--topics cannot be combined with a query")
        print(json.dumps(available_topics()) if args.json else "\n".join(available_topics()))
        return 0
    if args.query is not None:
        record = query_record(args.query, args.all_matches)
        print(json.dumps(record, ensure_ascii=False) if args.json else record["answer"])
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

