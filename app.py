"""Optional dashboard: streamlit run app.py"""
import tempfile
from pathlib import Path
import streamlit as st
from src.skills import load_skill_config
from src.pipeline import screen

st.set_page_config(page_title="Resume Screening Tool", layout="wide")
st.title("Automated Resume Screening Tool")
cfg = load_skill_config("data/skills.json")
default_jd = Path("data/job_description.txt").read_text(encoding="utf-8")
jd = st.text_area("Job description", default_jd, height=180)
must = st.text_input("Must-have skills (comma separated)", ", ".join(cfg["must_have"]))
cfg["must_have"] = [s.strip().lower() for s in must.split(",") if s.strip()]
min_years = st.slider("Minimum years of experience", 0.0, 10.0, 2.0, 0.5)
threshold = st.slider("Shortlist score threshold", 0, 100, 45)
files = st.file_uploader("Upload resumes (PDF/DOCX/TXT)", type=["pdf", "docx", "txt"], accept_multiple_files=True)

if st.button("Screen resumes") and files:
    with tempfile.TemporaryDirectory() as tmp:
        paths = []
        for f in files:
            p = Path(tmp) / f.name; p.write_bytes(f.getbuffer()); paths.append(p)
        df = screen(jd, paths, cfg, min_years, threshold)
    st.dataframe(df, use_container_width=True)
    st.download_button("Download CSV", df.to_csv(index=False), "ranking_report.csv")
