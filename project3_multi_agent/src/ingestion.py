"""
ingestion.py - PDF text extraction 
"""
import fitz


def load_pdf(pdf_path: str, max_chars: int = 12000) -> str:
    """PDF to text extract"""
    try:
        doc = fitz.open(pdf_path)
        text = "".join(page.get_text() for page in doc)
        doc.close()
        return text[:max_chars]
    except Exception as e:
        raise ValueError(f"PDF error : {str(e)}")
