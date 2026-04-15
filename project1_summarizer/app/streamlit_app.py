"""
streamlit_app.py
----------------
Project 1: Research Paper Summarizer
User Interface — Gradio (Streamlit-compatible structure)
"""

import os
import sys
import gradio as gr

# src folder add for import data
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from ingestion import load_pdf, get_pdf_metadata
from agents import summarize_agent


def process_paper(pdf_file):
    """
    Main pipeline:
    PDF Upload → Text Extraction → LLM Summarization → Output
    """
    if pdf_file is None:
        return "⚠️ Please upload a PDF file first!"

    # Step 1: PDF to text 
    text = load_pdf(pdf_file)

    if len(text.strip()) < 100:
        return "❌ Could not extract text from PDF. Please try another file."

    # Step 2: Metadata 
    meta = get_pdf_metadata(pdf_file)

    # Step 3: LLM summarize 
    result = summarize_agent(text)

    # Step 4: Metadata return
    header = f"""### 📄 Paper Info
- **Title:** {meta['title']}
- **Author:** {meta['author']}
- **Pages:** {meta['total_pages']}

---
"""
    return header + result


# ── Gradio UI ──────────────────────────────────────────
with gr.Blocks(title="Research Paper Summarizer", theme=gr.themes.Soft()) as app:

    gr.Markdown("""
    # 🔬 Research Paper Summarizer
    ### Project 1 | Advanced AI Course | Group Alpha
    **Powered by:** Groq API (LLaMA 3.3 70B) · PyMuPDF · Gradio
    """)

    with gr.Row():
        with gr.Column(scale=1):
            pdf_input = gr.File(
                label="📄 Upload Research Paper PDF",
                file_types=[".pdf"]
            )
            submit_btn = gr.Button("🔍 Analyze Paper", variant="primary", size="lg")
            gr.Markdown("""
            **Architecture:**
