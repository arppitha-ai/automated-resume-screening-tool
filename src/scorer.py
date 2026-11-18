"""Step 4: TF-IDF + cosine similarity, combined with skill coverage."""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from src.skills import find_skills, find_years_of_experience

W_TFIDF, W_MUST, W_NICE, W_EXP = 0.40, 0.35, 0.10, 0.15


def tfidf_scores(clean_job, clean_resumes):
    vec = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
    matrix = vec.fit_transform([clean_job] + clean_resumes)
    return cosine_similarity(matrix[0:1], matrix[1:]).flatten()


def score_resume(clean, tfidf, cfg, min_years):
    must = find_skills(clean, cfg["must_have"], cfg["aliases"])
    nice = find_skills(clean, cfg["nice_to_have"], cfg["aliases"])
    years = find_years_of_experience(clean) or 0.0
    must_cov = len(must) / max(1, len(cfg["must_have"]))
    nice_cov = len(nice) / max(1, len(cfg["nice_to_have"]))
    exp_score = min(1.0, years / min_years) if min_years else 1.0
    final = 100 * (W_TFIDF * tfidf + W_MUST * must_cov + W_NICE * nice_cov + W_EXP * exp_score)
    return {
        "score": round(final, 2),
        "tfidf_similarity": round(float(tfidf), 3),
        "years_experience": years,
        "must_have_coverage": round(must_cov, 2),
        "matched_must_have": ", ".join(must),
        "missing_must_have": ", ".join(s for s in cfg["must_have"] if s not in must),
        "matched_nice_to_have": ", ".join(nice),
    }


def decide(row, threshold=45, min_must_coverage=0.6, min_years=2.0):
    if row["must_have_coverage"] < min_must_coverage:
        return "Rejected (missing must-have skills)"
    if row["score"] < threshold:
        return "Rejected (low score)"
    if row["years_experience"] < 0.5 * min_years:
        return "Manual review (low/unclear experience)"
    return "Shortlisted"
