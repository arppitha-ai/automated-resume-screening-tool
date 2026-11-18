"""Step 5: build ranking table and save CSV report."""
import pandas as pd
from pathlib import Path


def build_report(rows, out_path="outputs/ranking_report.csv"):
    df = pd.DataFrame(rows).sort_values("score", ascending=False).reset_index(drop=True)
    df.insert(0, "rank", df.index + 1)
    Path(out_path).parent.mkdir(exist_ok=True)
    df.to_csv(out_path, index=False)
    return df
