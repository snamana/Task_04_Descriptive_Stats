# Task_04_Descriptive_Stats

This repository contains scripts for descriptive statistical analysis of the `SocialMediaTop100.csv` dataset using pure Python, pandas, and polars. Bonus: visualization script included.

## Files
- `pure_python.py`: Analysis using only the Python standard library.
- `pandas_python.py`: Analysis using pandas.
- `polars_python.py`: Analysis using polars.
- `requirements.txt`: Python dependencies for pandas, polars, matplotlib, seaborn.
- `.csv`: The dataset (add this file to the repo, not included here).
- **Original dataset:** [ IC2023 — Educational Offerings, Organization, Services, and Athletic Associations](https://nces.ed.gov/ipeds/datacenter/DataFiles.aspx?gotoReportId=7&sid=7285e87d-99f8-4da4-b169-96299b680333&rtid=7)

## Instructions
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Place `IC2023.csv` in the repository directory.
3. Run the scripts:
   - Pure Python: `python3 pure_python.py`
   - Pandas: `python3 pandas_python.py`
   - Polars: `python3 polars_python.py`

## Summary of Findings
- The majority of institutions are "Degree-granting, primarily baccalaureate or above".This indicates that most listed institutions offer full 4-year (or above) degree programs.
- The CONTROL column showed that a significant proportion of institutions are public.Among public vs. private, private nonprofit institutions are also highly represented, while for-profit institutions are in the minority.
- Higher education access is primarily concentrated in urban/suburban areas — potentially a point of consideration for policy outreach to rural populations.
- The nonprofit model still dominates U.S. higher education, with very few for-profit players remaining post-regulation.
- Institutional diversity (sector, control, level) is well captured through categorical variables — ideal for dashboards or regional summaries.

