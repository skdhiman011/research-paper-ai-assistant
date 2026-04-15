"""
embeddings.py
-------------
Sentence Transformer used for text embedding ।
"""

from sentence_transformers import SentenceTransformer

# embedding model (~90MB)
_model = None


def get_embedder():
    """Embedding model load (Single time load)."""
    global _model
    if _model is None:
        print("⏳ Loading embedding model...")
        _model = SentenceTransformer('all-MiniLM-L6-v2')
        print("✅ Embedding model ready!")
    return _model


def embed_texts(texts: list) -> list:
    """
    Text list to embedding list convert 
    
    Args:
        texts: List of strings
    
    Returns:
        List of embedding vectors
    """
    embedder = get_embedder()
    return embedder.encode(texts).tolist()


def embed_query(query: str) -> list:
    """
    Single query text to embedding convert ।
    
    Returns:
        Single embedding vector as list
    """
    embedder = get_embedder()
    return embedder.encode([query]).tolist()
