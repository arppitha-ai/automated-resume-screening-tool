"""Runs the full screening workflow; shared by main.py and the Streamlit app."""
from pathlib import Path
from src.extractor import extract_text
from src.cleaner import clean_text, guess_name
from src.skills import load_skill_config
from src.scorer import tfidf_scores, score_resume, decide
from src.report import build_report

SUPPORTED = {".pdf", ".docx", ".txt"}


def screen(job_text, resume_paths, cfg, min_years=2.0, threshold=45, out_path="outputs/ranking_report.csv"):
    raws, files = [], []
    for p in resume_paths:
        p = Path(p)
        try:
            raws.append(extract_text(p)); files.append(p)
        except Exception as e:
            print(f"[skip] {p.name}: {e}")
    cleans = [clean_text(r) for r in raws]
    sims = tfidf_scores(clean_text(job_text), cleans)
    rows = []
    for raw, clean, sim, f in zip(raws, cleans, sims, files):
        row = {"candidate": guess_name(raw, f.stem), "file": f.name}
        row.update(score_resume(clean, sim, cfg, min_years))
        row["status"] = decide(row, threshold, min_years=min_years)
        rows.append(row)
    return build_report(rows, out_path)


def list_resumes(folder="resumes"):
    return sorted(p for p in Path(folder).iterdir() if p.suffix.lower() in SUPPORTED)
