"""
agents.py
---------
Multi-Agent System — Three (3) AI Agent:
- Agent 1: Paper Summarizer
- Agent 2: Citation Extractor  
- Agent 3: Research Gap Finder
- Orchestrator: All Agent run together
"""

import os
from groq import Groq

client = (api_key=os.environ.get("API_KEY"))
MODEL = "llama-3.3-70b-versatile"


def _run_agent(system_prompt: str, user_content: str, max_tokens: int = 1200) -> str:
    """Base function — agent ।"""
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content}
        ],
        temperature=0.3,
        max_tokens=max_tokens
    )
    return response.choices[0].message.content


def agent_summarizer(text: str) -> str:
    """
    Agent 1: Paper Summarizer
    Paper Summarize, objective, methodology ও results
    """
    return _run_agent(
        system_prompt="You are Agent 1: Paper Summarizer. Always respond in both Bengali and English.",
        user_content=f"""Analyze this research paper:

## 📋 Summary 
(5-6 lines about the paper)

## 🎯 Research Objective 
(What problem does it solve?)

## 🔬 Methodology
(How did they approach it?)

## 📊 Results 
(Main findings)

Paper: {text}"""
    )


def agent_citation_extractor(text: str) -> str:
    """
    Agent 2: Citation Extractor
    From Paper find all references and citations 
    """
    return _run_agent(
        system_prompt="You are Agent 2: Citation Extractor. Always respond in English.",
        user_content=f"""Extract all citations and references:

## 📚 References 
(Author, Year, Title, Journal — numbered list)

## 📊 Citation Statistics 
- Total references found
- Year range of citations
- Most cited authors

Paper: {text}"""
    )


def agent_gap_finder(text: str) -> str:
    """
    Agent 3: Research Gap Finder
    """
    return _run_agent(
        system_prompt="You are Agent 3: Research Gap Finder. Always respond in English.",
        user_content=f"""Find research gaps and future opportunities:

## 🔭 Research Gaps 
(What remains unanswered?)

## 🚀 Future Work 
(4-5 specific future research ideas)

## ⚠️ Unsolved Problems যা
(What does this paper NOT solve?)

## 💡 Improvement Ideas
(How can this work be extended?)

Paper: {text}"""
    )


def orchestrator(text: str):
    """
    Orchestrator — Three agent work sequentially
    Generator function — Each agent yield after finishing।
    """
    yield "🤖 Agent 1 working — Summarizing paper...", "", ""
    summary = agent_summarizer(text)

    yield "🤖 Agent 2 working — Extracting citations...", summary, ""
    citations = agent_citation_extractor(text)

    yield "🤖 Agent 3 working — Finding research gaps...", summary, citations
    gaps = agent_gap_finder(text)

    yield "✅ All 3 Agents completed!", summary, citations, gaps
