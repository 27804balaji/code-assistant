
# 🎯 Code Assistant

**Your Local AI Pair Programmer**  
A context-aware coding assistant that reads your project files and provides intelligent explanations, suggestions, and improvements — all running locally or via preferred LLM APIs.

---

## 🚀 Key Features

- 📂 **Context-aware assistance** — Analyzes your local codebase to offer precise code explanations, refactoring tips, or suggestions  
- 💬 Natural-language chat interface via Streamlit  
- 🛠 Supports local tools like `tree` and file readers to understand project structure  
- 🔄 Configurable to use multiple LLM backends (Ollama, Mistral, Google Gemini, etc.)

---

## 🏗️ Project Structure

```
code-assistant/
├── api/                     # FastAPI backend and LLM handlers
├── streamlit_app.py         # Frontend chat UI
├── launch_assistant.sh      # Utility to start all services
├── requirements.txt         # Python dependencies
├── .env.example             # Example environment settings
└── README.md                # Project documentation
```

---

## ⚙️ Requirements

- **Python 3.11+**  
- `tree` command (install via `apt`, `brew`, or `choco`)  
- LLM provider credentials (Ollama, Mistral, Google, etc.) stored in `.env`

---

## 🛠️ Installation & Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/27804balaji/code-assistant.git
    cd code-assistant
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Configure environment variables:
    ```bash
    cp .env.example .env
    # Edit .env with:
    # MISTRAL_API_KEY=...
    # GOOGLE_API_KEY=...
    # TREE_CMD=tree
    ```

4. (Optional) Select your preferred LLM backend in `api/utils.py`.

---

## ▶️ Run the Assistant

```bash
chmod +x launch_assistant.sh
./launch_assistant.sh
```

This will:

- Launch the FastAPI backend
- Open the Streamlit frontend at `http://localhost:8501`

---

## 🧩 Usage Guide

- **Set project directory** in the sidebar  
- **Ask questions** like:
  - "Explain `run_agent` in `api.py`."
  - "Show folder structure."
  - "Suggest improvements for error handling in `streamlit_app.py`."

- **Clear chat history** using the sidebar option  
- Assistant maintains context throughout the session

---

## 📌 Configuration

Edit `load_llm()` in `api/utils.py` to change LLM provider:
```python
model = ChatOllama(model="llama3:8b")
# or use ChatMistralAI, ChatGoogleGenerativeAI, etc.
```

---

## 📈 Future enhancement

- [ ] Docker-based deployment
- [ ] Session history and bookmarking
- [ ] Plugin for VS Code

---

## 🤝 Contributing

1. Fork the repo  
2. Create a feature branch: `git checkout -b feature-name`  
3. Commit your changes  
4. Push to your fork  
5. Open a Pull Request

---

## 📄 License

MIT License – see the [LICENSE](LICENSE) file.

---

## 👤 Author

**Balaji Perumal**  
GitHub: [@27804balaji](https://github.com/27804balaji)  
Email: 27804balaji@gmail.com

---

> _"Make this your go-to dev companion. Provide context, ask away, and code smarter."_ 💡
