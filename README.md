# automated-resume-screening-tool
AI-based Resume Screening Tool using Python, NLP, and Streamlit

# Automated Resume Screening Tool

## Overview
Automated Resume Screening Tool is a Python-based NLP project that simulates how Applicant Tracking Systems (ATS) screen resumes against job descriptions.

The system extracts resume text, analyzes candidate profiles, compares them with job requirements, calculates similarity scores, and ranks candidates automatically.

This project is designed as a practical implementation of:
- Resume parsing
- Job matching
- Candidate ranking
- Basic NLP techniques

---

## Problem Statement
Recruiters often receive hundreds of resumes for a single job opening.

Manual resume screening is:
- Time-consuming
- Error-prone
- Inconsistent

This project automates the initial screening process by:
1. Extracting text from resumes
2. Matching resumes with job descriptions
3. Scoring candidates
4. Generating shortlist decisions

---

## Features

- Upload multiple resumes
- Supports:
  - TXT
  - PDF
  - DOCX
- Job description input
- Resume text extraction
- Text preprocessing
- TF-IDF vectorization
- Cosine similarity scoring
- Candidate ranking
- Shortlist / Reject decision
- CSV report generation
- Streamlit web interface
- Score visualization chart

---

## Project Workflow

```text
Resume Upload
   ↓
Text Extraction
   ↓
Text Cleaning
   ↓
Feature Extraction
   ↓
TF-IDF Vectorization
   ↓
Cosine Similarity
   ↓
Resume Ranking
   ↓
Shortlist Decision
   ↓
CSV Report
```

---

## Tech Stack

### Programming Language
- Python 3

### Libraries
- pandas
- scikit-learn
- streamlit
- matplotlib
- PyPDF2
- python-docx

### Concepts Used
- Natural Language Processing (NLP)
- TF-IDF
- Cosine Similarity
- Text Mining
- Resume Ranking

---

## Folder Structure

```text
Automated-Resume-Screening-Tool/
│
├── resumes/
│   ├── resume1.txt
│   ├── resume2.txt
│   └── resume3.txt
│
├── data/
│   └── job_description.txt
│
├── outputs/
│   └── results.csv
│
├── src/
│   └── utils.py
│
├── app.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Installation

Clone repository:

```bash
git clone https://github.com/your-username/automated-resume-screening-tool.git
cd automated-resume-screening-tool
```

Create virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run Streamlit application:

```bash
streamlit run app.py
```

Open browser:

```text
http://localhost:8501
```

---

## Output
The system generates:

- Ranked resumes
- Candidate scores
- Shortlisted candidates
- Rejected candidates
- CSV report in `outputs/results.csv`

---

## Sample Use Case

### Job Description
Looking for candidates with:
- Python
- SQL
- Machine Learning
- Data Analysis

### Resume Screening Output
| Resume | Score | Status |
|--------|------|--------|
| resume1.txt | 0.78 | Shortlisted |
| resume2.txt | 0.22 | Rejected |
| resume3.txt | 0.61 | Shortlisted |

---

## Learning Outcomes
This project helped in understanding:

- File handling in Python
- NLP fundamentals
- Resume parsing
- Similarity algorithms
- Streamlit UI development
- Project structuring for GitHub

---

## Future Improvements
Possible enhancements:

- Advanced skill extraction using spaCy
- Named Entity Recognition
- Recruiter dashboard
- FastAPI backend
- Database integration
- Authentication system
- Deployment to cloud

---

## Industry Relevance
This project simulates real-world ATS functionality used in:

- HR Tech platforms
- Recruitment automation systems
- Talent screening solutions
- Hiring analytics platforms

---

## Author
Arppitha R A
