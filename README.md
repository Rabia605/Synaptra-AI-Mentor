# Synaptra - AI Mentor Chatbot

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white"/>
  <img src="https://img.shields.io/badge/OpenRouter-412991?style=for-the-badge&logo=openai&logoColor=white"/>
  <img src="https://img.shields.io/badge/Mistral--7B-FF6B35?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge"/>
</p>

<p align="center">
  An AI-powered mentor chatbot built with <b>LangChain, Streamlit & OpenRouter</b>  providing career guidance, course recommendations, and resume-building advice for students in Artificial Intelligence.
</p>

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Workflow](#project-workflow)
- [How to Run](#how-to-run)
- [Project Structure](#project-structure)
- [Author](#author)

---

## Overview

**Synaptra** is an AI-powered mentor chatbot designed to guide students in the field of Artificial Intelligence. It leverages **LangChain's chat model abstraction**, the **Mistral-7B-Instruct** model via **OpenRouter**, and a **Streamlit** interface to deliver real-time, context-aware career mentoring with a persistent chat history.

---

## Features

- Career guidance tailored to AI/ML students
- Course and learning path recommendations
- Resume-building advice
- Persistent multi-turn conversation with message history
- Powered by Mistral-7B-Instruct via OpenRouter API
- Clean chat UI using `streamlit-chat`
- Secrets-based API key management (no hardcoded keys)

---

## Tech Stack

| Tool | Purpose |
|:---|:---|
| Python | Core language |
| Streamlit | Web UI framework |
| streamlit-chat | Chat message UI components |
| LangChain | LLM abstraction & message handling |
| OpenRouter API | LLM API gateway (Mistral-7B-Instruct) |
| python-dotenv | Environment variable management |

---

| Step | Description |
|:---:|:---|
| 1 | User types a query in the Streamlit chat interface |
| 2 | Query is appended to session state message history |
| 3 | Full conversation history is built using `SystemMessage`, `HumanMessage`, `AIMessage` |
| 4 | LangChain sends the message list to Mistral-7B via OpenRouter |
| 5 | AI response is returned and appended to session state |
| 6 | Chat history is displayed in reverse chronological order |

---

## How to Run

**1. Clone the repository**
```bash
git clone https://github.com/Rabia605/Synaptra-AI-Mentor.git
cd Synaptra-AI-Mentor
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Set up your API key**

Create a `.streamlit/secrets.toml` file (do NOT commit this):
```toml
OPENROUTER_API_KEY = "your_openrouter_api_key_here"
OPENROUTER_API_BASE = "https://openrouter.ai/api/v1"
```

> Get your free API key at [openrouter.ai](https://openrouter.ai)

**4. Run the app**
```bash
streamlit run streamlit_app.py
```

---

## Project Structure

```
Synaptra-AI-Mentor/
│
├── streamlit_app.py               # Main application
├── requirements.txt               # Dependencies
├── .gitignore                     # Ignores secrets.toml
├── .streamlit/
│   └── secrets_example.toml     
└── README.md
```

> Never commit `.streamlit/secrets.toml` — it contains your private API key.

---

## Author

**Rabia Noreen**
*Software Engineer | Building with AI & ML*

---

<p align="center">If this project inspired you, hit that ⭐ button!</p>
