
import polars as pl
from pathlib import Path

def main():
    filepath = "/content/sample_data/ic2023.csv"
    output_dir = Path("polars_results")
    output_dir.mkdir(exist_ok=True)

    df = pl.read_csv(filepath)
    num_cols = [c for c, dt in zip(df.columns, df.dtypes) if dt in (pl.Float32, pl.Float64, pl.Int64, pl.Int32, pl.UInt32, pl.UInt64)]
    cat_cols = [c for c in df.columns if c not in num_cols]


    with open(output_dir / "ic2023_stats.txt", 'w') as f:
        f.write("==== OVERALL NUMERIC STATS ====\n")
        desc = df.select(num_cols).describe()
        f.write(desc.write_csv(separator="\t"))
        f.write("\n\n==== OVERALL CATEGORICAL STATS ====\n")
        for col in cat_cols[:10]:
            try:
                s = df[col].drop_nulls()
                vals = s.to_list()
                mode = max(set(vals), key=vals.count)
                f.write(f"{col}:\n")
                f.write(f"  unique: {len(set(vals))}\n")
                f.write(f"  mode: {mode}\n")
                f.write(f"  mode count: {vals.count(mode)}\n\n")
            except:
                continue

if __name__ == "__main__":
    main()
