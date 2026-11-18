"""Creates 8 synthetic resumes (TXT, DOCX, PDF) so the project runs without real data."""
from pathlib import Path
from docx import Document
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

R = {
"Asha Menon": ("pdf", "Data Analyst with 3 years of experience.\nSkills: Python, SQL, Excel, Power BI, Pandas, NumPy, Tableau, Git.\nBuilt Power BI dashboards and cleaned data with Pandas. Strong statistics and data visualization."),
"Rahul Nair": ("docx", "Business Analyst with 4 years of experience.\nSkills: SQL, Excel, Power BI, Tableau.\nCreated Excel reports and Power BI dashboards for sales teams. Basic Python."),
"Divya Krishnan": ("txt", "Fresher Data Science graduate, 1 year internship.\nSkills: Python, Pandas, NumPy, Machine Learning, Matplotlib, Git.\nProjects: house price prediction, sentiment analysis."),
"Arjun Das": ("pdf", "Senior Data Analyst, 5 years of experience.\nSkills: Python, SQL (PostgreSQL), Excel, PowerBI, Pandas, Seaborn, Statistics, Git.\nAutomated weekly reports and presented insights to management."),
"Meera Pillai": ("docx", "Web Developer with 3 years of experience.\nSkills: JavaScript, React, Node, HTML, CSS, MongoDB.\nBuilt e-commerce websites."),
"Sanjay Kumar": ("txt", "Accountant with 6 years of experience.\nSkills: Excel, Tally, bookkeeping, GST filing.\nPrepared financial statements and monthly Excel reports."),
"Neha Joseph": ("pdf", "Data Analyst, 2 years of experience.\nSkills: Python, SQL, Excel, Pandas, Tableau.\nWorked on customer churn analysis and Excel dashboards."),
"Keyword Stuffer": ("txt", "python sql excel power bi pandas tableau git statistics python sql excel power bi pandas\nNo work experience. Skills skills skills."),
}

def make(name, kind, body, folder=Path("resumes")):
    folder.mkdir(exist_ok=True)
    fn = folder / f"{name.replace(' ', '_')}.{kind}"
    text = f"{name}\n{body}"
    if kind == "txt":
        fn.write_text(text, encoding="utf-8")
    elif kind == "docx":
        d = Document()
        for line in text.split("\n"): d.add_paragraph(line)
        d.save(fn)
    else:
        c = canvas.Canvas(str(fn), pagesize=A4); y = 800
        for line in text.split("\n"):
            c.drawString(50, y, line[:95]); y -= 20
        c.save()

if __name__ == "__main__":
    for n, (k, b) in R.items(): make(n, k, b)
    print(f"Created {len(R)} sample resumes in resumes/")
