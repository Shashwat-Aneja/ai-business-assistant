# AI Business Assistant (CLI)

A lightweight command-line chatbot that assists with business-related queries using rule-based logic. It answers finance concepts, KPI formulas, business terms, and basic growth strategy questions.

---

## 💬 Example Conversations

```
> What is profit margin?
Profit margin = (Profit / Revenue) × 100

> How do I increase revenue?
Improve sales strategy, reduce expenses, optimize pricing, or increase product value.
```

---

## 🚀 Usage

### 1. Clone repo
```bash
git clone https://github.com/Shashwat-Aneja/ai-business-assistant
cd ai-business-assistant
```

### 2. Run directly
```bash
python assistant.py
```

---

### Run tests

The regression tests use Python's standard `unittest` framework and require no extra test dependency:

```bash
python -m unittest discover -s tests -v
```

## 🧠 Supported Questions

| Supported query | Response |
|-----------------|----------|
| `profit` | Profit formula |
| `revenue` | Revenue formula |
| `profit margin` | Profit-margin formula |
| `roi` | Return-on-investment formula |
| `kpi` | KPI definition and examples |
| `increase revenue` | Revenue-growth suggestions |
| `reduce expenses` | Cost-reduction suggestions |
| `business growth` | Growth-strategy suggestions |
| `automation` | Automation overview |

---

## 📌 Project Structure

```
ai-business-assistant/
│
├── assistant.py
├── README.md
└── tests/
    └── test_assistant.py
```

---

## 🛠 Future Enhancements
- Integrate OpenAI API for advanced responses
- Connect KPIs from actual business data
- Use voice input
- Deploy as API with FastAPI

---

Developed by **Shashwat Aneja**


### Additional finance topics

The assistant also answers common operating-finance questions:

- **Cash flow:** net cash flow is cash inflows minus cash outflows. Consider timing, not only the total.
- **Gross margin:** `((Revenue - Cost of Goods Sold) / Revenue) × 100`. Revenue must be non-zero when calculating the ratio.

Try asking `How should I track cash flow?` or `Explain gross margin` in the CLI.
