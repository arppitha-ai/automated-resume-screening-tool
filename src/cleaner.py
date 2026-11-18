"""Step 2: clean text (lowercase, remove emails/phones/extra symbols)."""
import re


def clean_text(text):
    text = text.lower()
    text = re.sub(r"\S+@\S+", " ", text)            # emails (also avoids bias/privacy issues)
    text = re.sub(r"\+?\d[\d\s\-]{8,}\d", " ", text)  # phone numbers
    text = re.sub(r"[^a-z0-9+#.\s]", " ", text)     # keep c++, c#, .net style tokens
    return re.sub(r"\s+", " ", text).strip()


def guess_name(raw_text, fallback):
    """First non-empty line of a resume is usually the candidate's name."""
    for line in raw_text.splitlines():
        if line.strip():
            return line.strip()[:40]
    return fallback
