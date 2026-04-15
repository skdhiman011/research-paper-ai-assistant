"""
agents.py
---------
LLM Agent — Research Paper Summarizer
API used to paper summarize
"""

import os
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
MODEL = "llama-3.3-70b-versatile"


def summarize_agent(paper_text: str) -> str:
    """
    Research paper summarize agent।
    
    Args:
        paper_text: PDF  extracted text
    
    Returns:
        Structured summary as markdown string
    """
    prompt = f"""You are an expert AI Research Assistant. 
Analyze the following research paper and provide structured analysis in English.

Research Paper:
{paper_text}

Provide the following:

## 📋 Summary 
(Write 5-6 lines about what this paper is about)

## 🌟 Key Contributions 
(List 4-5 main new contributions of this paper)

## ⚠️ Limitations 
(List 3-4 limitations or weaknesses)

Be concise, accurate, and helpful."""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=1500
    )
    return response.choices[0].message.content
