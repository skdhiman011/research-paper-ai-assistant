# 📚 Project 2: Research Paper Q&A (RAG + Vector DB)

> **Course:** Advanced Artificial Intelligence | **Group:** 2

## 📌 Overview
Ask any question about a research paper. Uses RAG to find relevant sections and answer accurately.

## 🚀 Live Demo
👉 [Open Live App](https://huggingface.co/spaces/skdhiman011/research-paper-q_a)

## 🏗️ Architecture
```
User Interface (Gradio)
↓
Application Backend (app/streamlit_app.py)
↓
LLM + Prompting (src/agents.py)
↓
Retrieval System (src/rag_pipeline.py)
↓
Vector Database (ChromaDB in-memory)
↓
Knowledge Documents (PDF → src/ingestion.py → chunks)
```

## 📁 Folder Structure
```
project2_rag_qa/
├── data/
│   ├── raw/             ← PDF files
│   └── processed/       ← Chunked text
├── notebooks/
│   └── experiments.ipynb
├── src/
│   ├── ingestion.py     ← PDF loading & chunking
│   ├── embeddings.py    ← Sentence Transformer embeddings
│   ├── rag_pipeline.py  ← ChromaDB indexing & retrieval
│   └── agents.py        ← LLM Q&A agent
├── app/
│   └── streamlit_app.py ← Gradio UI
├── requirements.txt
└── README.md
```

## ⚙️ How to Run
```bash
pip install -r requirements.txt
export API_KEY="your_key_here"
python app/streamlit_app.py
```

## 🛠️ Technologies
| Component | Technology |
|-----------|-----------|
| LLM | API (LLaMA 3.3 70B) |
| Vector DB | ChromaDB |
| Embeddings | Sentence Transformers (all-MiniLM-L6-v2) |
| PDF Processing | PyMuPDF |
| UI | Gradio |
