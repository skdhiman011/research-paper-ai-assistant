"""
ingestion.py
------------
PDF to text etraction and chunks dividation
"""

import fitz


def load_pdf(pdf_path: str) -> str:
    """PDF to text extract """
    try:
        doc = fitz.open(pdf_path)
        text = "".join(page.get_text() for page in doc)
        doc.close()
        return text
    except Exception as e:
        raise ValueError(f"PDF error: {str(e)}")


def chunk_text(text: str, chunk_size: int = 400, overlap: int = 50) -> list:
    """
    Text overlap with small chunks dividation।
    
    Args:
        text: Full document text
        chunk_size:  hunk  words
        overlap: continuous two chunk and shared word
    
    Returns:
        List of text chunks
    """
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i + chunk_size])
        if chunk.strip():
            chunks.append(chunk)
    return chunks
