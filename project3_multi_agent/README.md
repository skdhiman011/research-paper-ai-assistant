# 🤖 Project 3: Multi-Agent Research Assistant

> **Course:** Advanced Artificial Intelligence | **Group:** Alpha

## 📌 Overview
3 specialized AI Agents work together to fully analyze a research paper.

## 🚀 Live Demo
👉 [Open Live App](https://huggingface.co/spaces/skdhiman011/researchai)

## 🏗️ Architecture
```
User Interface (Gradio)
↓
Orchestrator (app/streamlit_app.py)
↓
Agent 1: Summarizer ──┐
Agent 2: Citation   ──┼── (src/agents.py)
Agent 3: Gap Finder ──┘
↓
LLM: API (LLaMA 3.3 70B)
↓
Knowledge Documents (src/ingestion.py)
```

## 📁 Folder Structure
```
project3_multi_agent/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   └── experiments.ipynb
├── src/
│   ├── ingestion.py      ← PDF loading
│   ├── embeddings.py     ← (Placeholder)
│   ├── rag_pipeline.py   ← (Placeholder)
│   └── agents.py         ← 3 Agents + Orchestrator
├── app/
│   └── streamlit_app.py  ← Gradio UI
├── requirements.txt
└── README.md
```
## ⚙️ How to Run
```bash
pip install -r requirements.txt
export API_KEY="your_key_here"
python app/streamlit_app.py
```

