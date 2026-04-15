# 🔬 Project 1: Research Paper Summarizer

> **Course:** Advanced Artificial Intelligence | **Group:** Alpha

## 📌 Overview
Upload any research paper PDF and get instant AI-powered analysis including Summary, Key Contributions, and Limitations.

## 🚀 Live Demo
👉 [Open Live App](https://huggingface.co/spaces/skdhiman011/research-paper-summarizer)

## 🏗️ Architecture
User Interface (Gradio)
↓
Application Backend (app/streamlit_app.py)
↓
LLM + Prompting (src/agents.py)
↓
PDF Ingestion (src/ingestion.py)
↓
Knowledge Documents (data/raw/)

## 📁 Folder Structure
project1_summarizer/
├── data/
│   ├── raw/          ← Upload PDF files here
│   └── processed/    ← Extracted text saved here
├── notebooks/
│   └── experiments.ipynb
├── src/
│   ├── ingestion.py  ← PDF text extraction
│   ├── embeddings.py ← (Used in Project 2)
│   ├── rag_pipeline.py ← (Used in Project 2)
│   └── agents.py     ← LLM summarization agent
├── app/
│   └── streamlit_app.py ← Gradio UI
├── requirements.txt
└── README.md

## ⚙️ How to Run
```bash
pip install -r requirements.txt
export GROQ_API_KEY="your_key_here"
python app/streamlit_app.py
```

## 🛠️ Technologies
| Component | Technology |
|-----------|-----------|
| LLM | Groq API (LLaMA 3.3 70B) |
| PDF Processing | PyMuPDF |
| UI | Gradio |
| Deployment | Hugging Face Spaces |
