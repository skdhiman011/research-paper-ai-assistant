"""
streamlit_app.py
----------------
Project 3: Multi-Agent Research Assistant
3 AI Agents work sequentially via an Orchestrator.
"""

import os
import sys
import gradio as gr

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from ingestion import load_pdf
from agents import orchestrator


def run_agents(pdf_file, progress=gr.Progress()):
    """Orchestrator for — all agent working step by steo।"""
    if pdf_file is None:
        yield "⚠️ Please upload a PDF!", "", "", ""
        return

    yield "⏳ Reading PDF...", "", "", ""
    text = load_pdf(pdf_file)

    if len(text.strip()) < 100:
        yield "❌ Could not extract text from PDF.", "", "", ""
        return

    progress(0.1, desc="Starting agents...")
    steps = list(orchestrator(text))

    progress(0.4, desc="Agent 1 done...")
    yield "🤖 Agent 2 working...", steps[0][1], "", ""

    progress(0.7, desc="Agent 2 done...")
    yield "🤖 Agent 3 working...", steps[1][1], steps[1][2], ""

    progress(1.0, desc="All done!")
    final = steps[-1]
    yield final[0], final[1], final[2], final[3]


# ── Gradio UI ──────────────────────────────────────────
with gr.Blocks(title="Multi-Agent Research Assistant", theme=gr.themes.Soft()) as app:

    gr.Markdown("""
    # 🤖 Multi-Agent Research Assistant
    ### Project 3 | Advanced AI Course | Group 2
    **Powered by:** API · LLaMA 3.3 70B · Gradio

    | Agent | Role | Task |
    |-------|------|-----|
    | 🤖 Agent 1 | Paper Summarizer | Paper Summary |
    | 🤖 Agent 2 | Citation Extractor | Find citation |
    | 🤖 Agent 3 | Research Gap Finder | Find research gap |
    """)

    with gr.Row():
        with gr.Column(scale=1):
            pdf_input = gr.File(label="📄 Upload Research Paper PDF", file_types=[".pdf"])
            run_btn = gr.Button("🚀 Run All 3 Agents", variant="primary", size="lg")
            status_box = gr.Markdown("_Upload a PDF and click the button..._")
            gr.Markdown("""
            **Multi-Agent Flow:**
