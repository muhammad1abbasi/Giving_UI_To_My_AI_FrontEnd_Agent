# 🤖 AI Front-End Advisor Expert Chat Agent With UI 

This is an interactive AI-powered **frontend expert** chat agent built using:

- **OpenAI Agentic SDK**
- **Google Gemini API (via OpenAI-style client)**
- **Chainlit** (for chat interface)
- **UV + venv** for environment and package management

---

## 🚀 Features

- Live AI chat interface powered by [Chainlit](https://docs.chainlit.io/)
- Uses **Gemini 2.0 Flash** model via OpenAI-compatible API
- Maintains chat history session
- Answers frontend-related queries (HTML, CSS, JS, React, etc.)

---

## 🛠️ Tech Stack

| Tool         | Purpose                                 |
|--------------|------------------------------------------|
| `Chainlit`   | Chat UI framework                        |
| `OpenAI SDK` | Agent, model, runner config              |
| `Gemini API` | Provides LLM responses                   |
| `dotenv`     | Securely manage API keys                 |
| `UV` & `venv`| Fast virtual environment & package setup |

---

## 📁 Directory Structure

```bash
ai-front-end-expert-agent/
├── .env                  # Store your Gemini API key here
├── app.py                # Main chat agent logic
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
# Giving_UI_To_My_Chatting_Agent

