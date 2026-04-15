# 🔬 Research Paper AI Assistant

> **Course:** Advanced Artificial Intelligence  
> **Group:** Alpha 
> **Track:** Research Paper AI Assistant  

An AI-powered system to summarize, question-answer, and analyze research papers using **LLMs**, **RAG**, **Vector Databases**, and **Multi-Agent Systems**.

---

## 🚀 Live Demos

| Project | Description | Live Link |
|---------|-------------|-----------|
| 📋 Project 1 | Research Paper Summarizer | [Open App](https://huggingface.co/spaces/skdhiman011/research-paper-summarizer) |
| 📚 Project 2 | RAG-based Q&A System | [Open App](https://huggingface.co/spaces/skdhiman011/research-paper-q_a) |
| 🤖 Project 3 | Multi-Agent Research Assistant | [Open App](https://huggingface.co/spaces/skdhiman011/researchai) |

---

## 📁 Project Structure

### Project 1 — Research Paper Summarizer
- Upload any research paper PDF
- Get instant **Summary**, **Key Contributions**, and **Limitations**
- Built with: `API` + `PyMuPDF` + `Gradio`

### Project 2 — RAG + Vector DB Question Answering
- Upload a paper and ask any question about it
- Uses **Retrieval-Augmented Generation (RAG)** to find answers
- Built with: `API` + `ChromaDB` + `Sentence Transformers` + `Gradio`

### Project 3 — Multi-Agent Research Assistant
- 3 AI Agents work together automatically
- **Agent 1:** Paper Summarizer
- **Agent 2:** Citation Extractor  
- **Agent 3:** Research Gap Finder
- Built with: `API` + `Gradio`

---

## 🛠️ Technologies Used

| Category | Technology |
|----------|-----------|
| LLM Provider | API (LLaMA 3.3 70B) |
| Vector Database | ChromaDB |
| Embedding Model | Sentence Transformers (all-MiniLM-L6-v2) |
| AI Framework | Custom Agent Architecture |
| PDF Processing | PyMuPDF (fitz) |
| User Interface | Gradio |
| Deployment | Hugging Face Spaces |

---

## ⚙️ How to Run Locally

### 1. Clone the repository
\```bash
git clone https://github.com/YOUR_USERNAME/research-paper-ai-assistant.git
cd research-paper-ai-assistant
\```

### 2. Install dependencies
\```bash
# For Project 1
pip install -r project1_summarizer/requirements.txt

# For Project 2
pip install -r project2_rag_qa/requirements.txt

# For Project 3
pip install -r project3_multi_agent/requirements.txt
\```

### 3. Set your API Key
\```bash
export API_KEY="your_api_key_here"
\```

### 4. Run any project
\```bash
python project1_summarizer/app.py
\```

---

## 📊 System Architecture

### Project 2 — RAG Pipeline
\```
PDF Upload → Text Extraction → Chunking → Embedding → ChromaDB
                                                           ↓
User Question → Embedding → Vector Search → Top 3 Chunks → LLM → Answer
\```

### Project 3 — Multi-Agent Flow
\```
PDF Upload
    ↓
Orchestrator
    ├── Agent 1: Summarizer    → Summary
    ├── Agent 2: Citation Bot  → References
    └── Agent 3: Gap Finder    → Future Work
\```
