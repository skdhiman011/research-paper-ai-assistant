"""
rag_pipeline.py
---------------
RAG Pipeline:
1. PDF → Chunks → Embeddings → ChromaDB (indexing)
2. Query → Embedding → Vector Search → LLM → Answer (retrieval)
"""

import uuid
import chromadb
from ingestion import load_pdf, chunk_text
from embeddings import embed_texts, embed_query

# In-memory ChromaDB
_client = chromadb.Client()
_collection = None


def build_index(pdf_path: str) -> str:
    """
    PDF load and Vector DB indexing
    
    Returns:
        Status message
    """
    global _collection

    # Previous collection removed
    try:
        _client.delete_collection("research_paper")
    except Exception:
        pass
    _collection = _client.create_collection("research_paper")

    # PDF → Text → Chunks
    text = load_pdf(pdf_path)
    if len(text.strip()) < 100:
        return "❌ Could not extract text from PDF."

    chunks = chunk_text(text)

    # Chunks → Embeddings → ChromaDB
    embeddings = embed_texts(chunks)
    _collection.add(
        embeddings=embeddings,
        documents=chunks,
        ids=[str(uuid.uuid4()) for _ in chunks]
    )

    return f"✅ Indexed **{len(chunks)}** chunks into Vector DB!"


def retrieve_context(query: str, top_k: int = 3) -> str:
    """
    Find similar relevand chunks like Query 
    
    Returns:
        Combined context string
    """
    global _collection
    if _collection is None or _collection.count() == 0:
        return ""

    q_emb = embed_query(query)
    results = _collection.query(query_embeddings=q_emb, n_results=top_k)
    return "\n\n---\n\n".join(results['documents'][0])


def is_index_ready() -> bool:
    """Vector DB data check """
    return _collection is not None and _collection.count() > 0
