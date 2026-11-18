"""Usage: python main.py   (run generate_samples.py first if resumes/ is empty)"""
from pathlib import Path
from src.skills import load_skill_config
from src.pipeline import screen, list_resumes


def main():
    job_text = Path("data/job_description.txt").read_text(encoding="utf-8")
    cfg = load_skill_config("data/skills.json")
    resumes = list_resumes("resumes")
    if not resumes:
        print("No resumes found. Run: python generate_samples.py"); return
    df = screen(job_text, resumes, cfg, min_years=2.0, threshold=45)
    cols = ["rank", "candidate", "score", "tfidf_similarity", "must_have_coverage", "status"]
    print("\n=== RESUME RANKING ===")
    print(df[cols].to_string(index=False))
    print("\nMissing must-haves:")
    for _, r in df.iterrows():
        if r["missing_must_have"]:
            print(f"  {r['candidate']}: {r['missing_must_have']}")
    print("\nSaved: outputs/ranking_report.csv")


if __name__ == "__main__":
    main()
