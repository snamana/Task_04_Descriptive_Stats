
import pandas as pd
from pathlib import Path

def main():
    filepath = "/content/sample_data/ic2023.csv"
    output_dir = Path("pandas_results")
    output_dir.mkdir(exist_ok=True)

    df = pd.read_csv(filepath)
    num_cols = df.select_dtypes('number').columns.tolist()
    cat_cols = [col for col in df.columns if col not in num_cols]

    overall = df[num_cols].describe().T.to_string()

    with open(output_dir / "ic2023_stats.txt", 'w') as f:
        f.write("==== OVERALL NUMERIC STATS ====\n")
        f.write(overall)
        f.write("\n\n==== OVERALL CATEGORICAL STATS ====\n")
        for col in cat_cols[:10]:  # restrict to top 10 for readability
            try:
                f.write(f"{col}:\n")
                f.write(f"  unique: {df[col].nunique()}\n")
                f.write(f"  mode: {df[col].mode().iloc[0] if not df[col].mode().empty else 'N/A'}\n")
                f.write(f"  top count: {df[col].value_counts().iloc[0] if not df[col].value_counts().empty else 'N/A'}\n\n")
            except:
                continue

if __name__ == "__main__":
    main()
