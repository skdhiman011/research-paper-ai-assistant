"""
agents.py
---------
RAG-based Question Answering Agent
Context ways LLM provide answer of the question
"""

import os
from groq import Groq

client = (api_key=os.environ.get("API_KEY"))
MODEL = "llama-3.3-70b-versatile"


def qa_agent(question: str, context: str) -> str:
    """
    Retrieved context for question answering।
    
    Args:
        question: User question
        context: Vector DB for retrieved relevant chunks
    
    Returns:
        LLM generated answer
    """
    prompt = f"""You are a helpful Research Paper Assistant.
Answer the question based ONLY on the provided context from the paper.

Context from paper:
{context}

Question: {question}

Instructions:
- Answer in English
- Be specific and reference the context
- If answer is not in context, say: "This information was not found in the paper."

Answer:"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=1000
    )
    return response.choices[0].message.content
