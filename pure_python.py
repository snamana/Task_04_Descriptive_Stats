
import csv
import math
from collections import Counter, defaultdict
from pathlib import Path

def try_float(s):
    try:
        return float(str(s).replace(',', '').strip())
    except (ValueError, TypeError):
        return None

def infer_column_types(rows, sample_size=20):
    if not rows:
        return set(), set()
    cols = rows[0].keys()
    numeric, categorical = set(), set()
    for col in cols:
        floats = [try_float(row[col]) for row in rows[:sample_size]]
        n_floats = sum(v is not None for v in floats)
        if n_floats >= 0.8 * len(floats):
            numeric.add(col)
        else:
            categorical.add(col)
    return numeric, categorical

def compute_numeric_stats(values):
    vals = [try_float(v) for v in values if try_float(v) is not None]
    if not vals:
        return {}
    n = len(vals)
    mean = sum(vals) / n
    std = math.sqrt(sum((x - mean) ** 2 for x in vals) / (n - 1)) if n > 1 else 0
    return {'count': n, 'mean': mean, 'min': min(vals), 'max': max(vals), 'std': std}

def compute_categorical_stats(values):
    vals = [v for v in values if v]
    count = Counter(vals)
    if not count:
        return {}
    mode, mode_count = count.most_common(1)[0]
    return {'count': len(vals), 'unique': len(count), 'mode': mode, 'mode_count': mode_count}

def analyze_group(rows, num_cols, cat_cols):
    stats = {}
    for col in num_cols:
        stats[col] = compute_numeric_stats([r[col] for r in rows])
    for col in cat_cols:
        stats[col] = compute_categorical_stats([r[col] for r in rows])
    return stats

def group_by_key(rows, key):
    groups = defaultdict(list)
    for r in rows:
        if key in r:
            groups[r[key]].append(r)
    return groups

def main():
    filepath = "/content/sample_data/ic2023.csv"
    output_dir = Path("pure_python_results")
    output_dir.mkdir(exist_ok=True)

    with open(filepath, newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))

    num_cols, cat_cols = infer_column_types(rows)
    overall_stats = analyze_group(rows, num_cols, cat_cols)

    group_stats = {}
    for key in ['CNTLAFFI']:  # control/affiliation is a good group key
        groups = group_by_key(rows, key)
        sample_key = next(iter(groups))
        group_stats[f"{key}={sample_key}"] = analyze_group(groups[sample_key], num_cols, cat_cols)

    with open(output_dir / "ic2023_stats.txt", 'w', encoding='utf-8') as f:
        f.write("==== OVERALL STATS ====\n")
        for col, stat in overall_stats.items():
            f.write(f"{col}:\n")
            for k, v in stat.items():
                f.write(f"  {k}: {v}\n")
        for gname, stats in group_stats.items():
            f.write(f"\n==== GROUP: {gname} ====\n")
            for col, stat in stats.items():
                f.write(f"{col}:\n")
                for k, v in stat.items():
                    f.write(f"  {k}: {v}\n")

if __name__ == "__main__":
    main()
