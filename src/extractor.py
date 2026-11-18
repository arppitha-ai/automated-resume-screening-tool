"""Step 1: read raw text from PDF, DOCX or TXT resumes."""
from pathlib import Path
import pdfplumber
from docx import Document


def extract_text(path):
    path = Path(path)
    ext = path.suffix.lower()
    if ext == ".pdf":
        with pdfplumber.open(path) as pdf:
            return "\n".join((page.extract_text() or "") for page in pdf.pages)
    if ext == ".docx":
        return "\n".join(p.text for p in Document(path).paragraphs)
    if ext == ".txt":
        return path.read_text(encoding="utf-8", errors="ignore")
    raise ValueError(f"Unsupported file type: {ext}")
