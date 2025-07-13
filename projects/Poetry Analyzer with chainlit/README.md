# 🧠 Poetry Analyzer (AI Agent Based)

A multi-agent AI system that analyzes different types of poetry using natural language understanding.

Built using `openai-agents-sdk` and `uv` with support for structured agent handoffs and deep poetry analysis.

---

## 🚀 Features

- 🔍 Automatically detects poetry type:
  - 🎵 Lyric Poetry (feelings/emotions)
  - 📖 Narrative Poetry (story-based)
  - 🎭 Dramatic Poetry (dialogue/monologue)
- 🤖 Multi-Agent Structure (Parent + Specialized Agents)
- 🧠 Analyzes and explains poems in clear, poetic language (tashreeh)
- 🛠️ Built with Python + `uv` + `openai-agents-sdk`

---

## 🛠️ Tech Stack

| Layer           | Tool                      |
|----------------|---------------------------|
| Language        | Python 3.12+              |
| Agents Engine   | `openai-agents` SDK       |
| Runtime         | [`uv`](https://github.com/astral-sh/uv) (pyproject.toml based) |
| Environment     | `python-dotenv`           |
| Optional UI     | `Chainlit` (if extended)  |

---

## 📦 How to Run

> 🧪 Make sure you have [`uv`](https://github.com/astral-sh/uv) installed.

```bash
# Clone this repo
git clone https://github.com/your-username/poetry-analyzer
cd poetry-analyzer

# Install dependencies from pyproject.toml
uv pip install -r pyproject.toml

# Run the poetry analyzer
uv run main.py
