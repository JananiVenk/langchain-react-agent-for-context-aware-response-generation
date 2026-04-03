# 🤖 LangChain ReAct Agent for Context-Aware Response Generation

A context-aware conversational agent built with **LangChain** and **LangGraph** that dynamically selects the best tool — text, video, or web search — to answer user queries. Powered by OpenAI's GPT-4o and guided by the **ReAct (Reasoning + Acting)** framework.

---

## 📌 Overview

This project implements a ReAct agent named **Chandler** that intelligently decides *how* to respond based on what the user is asking:

- **Conceptual questions** → answered with a Wikipedia text summary
- **Tutorial or how-to queries** → answered with YouTube video links
- **Everything else** → answered via Google Serper web search

The agent maintains context-awareness across queries using LangChain's memory and message-passing architecture.

---

## 🧠 How It Works

The ReAct framework combines two capabilities:

1. **Reasoning** — The agent thinks through what kind of response best fits the user's query.
2. **Acting** — The agent invokes the appropriate tool and returns a grounded response.

Each query goes through the following flow:

```
User Query
    │
    ▼
ReAct Agent (GPT-4o)
    │
    ├── Is it best explained as text?    ──► Wikipedia Tool
    ├── Is it best shown as a video?     ──► YouTube Search Tool
    └── Neither text nor video fits?     ──► Google Serper (Web Search)
    │
    ▼
Final Response
```

---

## 🛠️ Tools Used

| Tool | Purpose |
|------|---------|
| `WikipediaQueryRun` | Fetches concise text explanations for concepts |
| `YouTubeSearchTool` | Searches and returns relevant YouTube video links |
| `GoogleSerperAPIWrapper` | Performs general web searches for everything else |

---

## 📦 Prerequisites

- Python 3.8+
- An [OpenAI API key](https://platform.openai.com/account/api-keys)
- A [Serper API key](https://serper.dev/) (free tier available)

---

## 🚀 Installation

**1. Clone the repository**

```bash
git clone https://github.com/JananiVenk/langchain-react-agent-for-context-aware-response-generation.git
cd langchain-react-agent-for-context-aware-response-generation
```

**2. Install dependencies**

```bash
pip install langchain langchain-community langchain-openai langgraph openai wikipedia
```

**3. Add your API keys**

Open `langchain-react-agent.py` and replace the placeholder values:

```python
llm = ChatOpenAI(
    model="gpt-4o",
    api_key="your_openai_key"       # ← Replace with your OpenAI API key
)

search = GoogleSerperAPIWrapper(
    serper_api_key="your_serper_key"  # ← Replace with your Serper API key
)
```

---

## ▶️ Usage

Run the agent script:

```bash
python langchain-react-agent.py
```

The script runs three sample queries by default:

```python
execute(agent, query="Explain AI")
execute(agent, query="Give me list of course links to learn AI")
execute(agent, query="Give some video tutorials for AI")
```

**Sample Output:**

```
Human Query: Explain AI
Tool used: wikipedia
Result:
Artificial intelligence (AI) is the simulation of human intelligence processes
by computer systems...

Human Query: Give me list of course links to learn AI
Tool used: serper_tool
Result:
Here are some top resources to learn AI: ...

Human Query: Give some video tutorials for AI
Tool used: YouTubeSearch
Result:
['https://www.youtube.com/watch?v=...', ...]
```

---

## 📁 Project Structure

```
├── langchain-react-agent.py   # Main agent script
├── langchain_result_1.png     # Sample output screenshot 1
├── langchain_result_2.png     # Sample output screenshot 2
├── langchain_result_3.png     # Sample output screenshot 3
└── README.md
```

---

## 🔧 Customization

You can extend the agent by:

- **Adding new tools** — wrap any Python function with LangChain's `Tool` class and append it to the `tools` list.
- **Changing the LLM** — swap `gpt-4o` for any model supported by `ChatOpenAI` (e.g., `gpt-3.5-turbo`).
- **Modifying the system prompt** — edit the `system_prompt` `SystemMessage` to change Chandler's name, persona, or decision logic.

---

## 📚 Key Dependencies

| Package | Version |
|---------|---------|
| `langchain` | ≥ 0.2 |
| `langchain-community` | ≥ 0.2 |
| `langchain-openai` | ≥ 0.1 |
| `langgraph` | ≥ 0.1 |
| `openai` | ≥ 1.0 |
| `wikipedia` | ≥ 1.4 |

---

## 📄 License

This project is open source. Feel free to use, modify, and distribute it.

---

## 🙌 Acknowledgements

Built with [LangChain](https://www.langchain.com/), [LangGraph](https://github.com/langchain-ai/langgraph), and [OpenAI](https://openai.com/).
