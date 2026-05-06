import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -------- LOAD RESUMES --------
def load_resumes(folder):
    resumes = []
    names = []

    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        with open(path, "r", encoding="utf-8") as f:
            text = f.read().lower()

        resumes.append(text)
        names.append(file)

    return resumes, names

# -------- MAIN FUNCTION --------
def main():
    resumes, names = load_resumes("resumes/")

    with open("data/job_description.txt", "r") as f:
        job_desc = f.read().lower()

    documents = resumes + [job_desc]

    tfidf = TfidfVectorizer()
    vectors = tfidf.fit_transform(documents)

    similarity = cosine_similarity(vectors[-1], vectors[:-1])

    scores = similarity.flatten()

    df = pd.DataFrame({
        "Resume": names,
        "Score": scores
    })

    df = df.sort_values(by="Score", ascending=False)

    df["Status"] = df["Score"].apply(lambda x: "Shortlisted" if x > 0.2 else "Rejected")

    print("\nFinal Results:\n")
    print(df)

    df.to_csv("outputs/results.csv", index=False)

if __name__ == "__main__":
    main()
