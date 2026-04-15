"""
streamlit_app.py
----------------
Project 2: RAG-based Research Paper Q&A
Pipeline: PDF → Chunks → Embeddings → ChromaDB → Query → LLM → Answer
"""

import os
import sys
import gradio as gr

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from rag_pipeline import build_index, retrieve_context, is_index_ready
from agents import qa_agent


def load_paper(pdf_file):
    """PDF load  Vector DB  indexing """
    if pdf_file is None:
        return "⚠️ Please upload a PDF first!"
    return build_index(pdf_file)


def answer_question(question):
    """RAG pipeline answering।"""
    if not is_index_ready():
        return "⚠️ Please upload and load a PDF first!"
    if not question.strip():
        return "⚠️ Please enter a question!"

    # Step 1: Vector DB to relevant context retrieve
    context = retrieve_context(question)

    # Step 2: LLM answering
    return qa_agent(question, context)


# ── Gradio UI ──────────────────────────────────────────
with gr.Blocks(title="Research Paper Q&A", theme=gr.themes.Soft()) as app:

    gr.Markdown("""
    # 📚 Research Paper Q&A System
    ### Project 2 | Advanced AI Course | Group 2
    **Powered by:** Groq API · ChromaDB · Sentence Transformers · Gradio
    """)

    with gr.Row():
        with gr.Column(scale=1):
            pdf_input = gr.File(label="📄 Upload PDF", file_types=[".pdf"])
            load_btn = gr.Button("📥 Load into Vector DB", variant="primary")
            status_box = gr.Markdown("_Upload a PDF to begin..._")
            gr.Markdown("""
            **RAG Pipeline:**
            
            PDF → Text Chunks
              → Embeddings
              → ChromaDB
              → Query Search
              → LLM Answer
          **Example Questions:**
            - What is the methodology?
            - What dataset was used?
            - What are the limitations?
            - What are the contributions?
            """)

        with gr.Column(scale=2):
            question_input = gr.Textbox(
                label="❓ Ask a Question",
                placeholder="Type your question here...",
                lines=2
            )
            ask_btn = gr.Button("🔍 Get Answer", variant="primary", size="lg")
            answer_output = gr.Markdown()
            gr.Examples(
                examples=[
                    ["What is the main methodology used?"],
                    ["What dataset was used in this paper?"],
                    ["What are the limitations of this research?"],
                    ["What are the key contributions?"],
                    ["What problem does this paper solve?"]
                ],
                inputs=question_input
            )

    load_btn.click(fn=load_paper, inputs=pdf_input, outputs=status_box)
    ask_btn.click(fn=answer_question, inputs=question_input, outputs=answer_output)


if __name__ == "__main__":
    app.launch()
