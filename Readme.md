# 🧠 LLM Summarizer – Arabic News Research Tool

An intelligent research and summarization tool that leverages Large Language Models (LLMs) to extract and summarize Arabic news content with precision and clarity. Built with Streamlit, LangChain, FAISS, and OpenAI's GPT-4.

---

## 🚀 Key Features

- 🔍 Search for news articles related to any user-defined topic.
- 📰 Automatically extract article content from URLs.
- 🧠 Summarize content in Arabic using GPT-4 via LangChain.
- 💾 Store summaries using FAISS for future semantic search.
- 🌐 Interactive and user-friendly interface using Streamlit.
- 🧪 Built-in utilities for language detection, cleanup, performance timing, and formatted output.

---

## 📁 Project Structure

LLM_Summarizer_Project/
├── app/
│ ├── init.py
│ ├── ui.py # Streamlit user interface
│ ├── api.py # (Optional) FastAPI endpoints
│ ├── summarizer.py # LLM summarization logic (OpenAI GPT-4)
│ ├── search.py # Google search API integration
│ ├── extractor.py # Article text extraction
│ ├── vector_store.py # FAISS-based summary storage and search
│ └── utils.py # Utility functions (text cleaning, language detection...)
├── .env # Environment variables (API keys)
├── main.py # Main application entry point
├── requirements.txt # Python package dependencies
├── README.md # Project documentation
└── scripts/
└── setup_env.sh # Script to scaffold project folders and files

## 🔧 Requirements

### Prerequisites:

- Python 3.8+
- OpenAI API Key
- Google Custom Search API Key & Custom Search Engine ID

### Install dependencies:

```bash
pip install -r requirements.txt


🖥️ Running the App


streamlit run main.py



📌 Future Improvements

 Add support for uploading and processing PDF or Word files.

 Use MongoDB or SQLite for persistent storage.

 Build a REST API using FastAPI.

 Deploy with Docker or on platforms like Render.

📜 License

MIT License – Free to use, modify, and contribute.

🙌 Contributing

Found a bug? Have a suggestion? Open an issue or submit a pull request. All contributions are welcome!



