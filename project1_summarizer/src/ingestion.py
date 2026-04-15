"""
ingestion.py
------------
PDF text converting module
"""

import fitz  # PyMuPDF


def load_pdf(pdf_path: str, max_chars: int = 12000) -> str:
    """
    PDF to text extract
    
    Args:
        pdf_path: PDF file path
        max_chars: Maximum character selection
    
    Returns:
        Extracted text string
    """
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page_num, page in enumerate(doc):
            text += f"\n--- Page {page_num + 1} ---\n"
            text += page.get_text()
        doc.close()
        return text[:max_chars]
    except Exception as e:
        raise ValueError(f"PDF not readed: {str(e)}")


def get_pdf_metadata(pdf_path: str) -> dict:
    """
    Find PDF metadata (title, author, pages)
    
    Returns:
        Dictionary with metadata
    """
    doc = fitz.open(pdf_path)
    metadata = {
        "title": doc.metadata.get("title", "Unknown"),
        "author": doc.metadata.get("author", "Unknown"),
        "total_pages": len(doc)
    }
    doc.close()
    return metadata
