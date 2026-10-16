# Usage: python3 create_filtereddata.py OUTPUT.csv [column=value ...] [column!=value ...] [--cols a,b,c]
# Needs: pip install pandas
# Reads: attendance_full.csv
#
#   column=v1,v2    keep rows where column is any of the listed values
#   column!=v1,v2   drop rows where column is any of the listed values
#   --cols a,b,c    only write these columns (default: all)
#
# Column names and values are listed in data_dictionary.md. Quote values with spaces.
#
# Examples:
#   python3 create_filtereddata.py sector_data.csv sex=All geo=All indigenous=All "year_level=Years 1-10" is_quarter_row=False sector=Government,Catholic,Independent --cols year,state,sector,rate,level
#   python3 create_filtereddata.py states_2025.csv year=2025 sector=All sex=All geo=All indigenous=All "year_level=Years 1-10" is_quarter_row=False state!=Australia
import sys
import pandas as pd

if len(sys.argv) < 2:
    sys.exit("Usage: python3 create_filtereddata.py OUTPUT.csv [column=value ...] [--cols a,b,c]")

out = sys.argv[1]
args = sys.argv[2:]

# Read everything as text so "2025" or "False" in a filter matches exactly what is in the file.
df = pd.read_csv("attendance_full.csv", dtype=str, keep_default_na=False)
print("Read", len(df), "rows")
full = df  # spelling checks look at the whole file, not what's left after earlier filters

cols = None
i = 0
while i < len(args):
    arg = args[i]
    if arg == "--cols":
        cols = args[i + 1].split(",")
        i += 2
        continue
    if "!=" in arg:
        col, vals = arg.split("!=", 1)
        keep = False
    elif "=" in arg:
        col, vals = arg.split("=", 1)
        keep = True
    else:
        sys.exit(f"Don't understand '{arg}'. Use column=value or column!=value.")

    if col not in df.columns:
        sys.exit(f"Unknown column '{col}'. Columns are: {', '.join(df.columns)}")
    # Case-insensitive, so sex=male matches "Male".
    vals = [v.lower() for v in vals.split(",")]
    unknown = [v for v in vals if v not in set(full[col].str.lower())]
    if unknown:
        print(f"Warning: {col} has no rows equal to {unknown} (check spelling in data_dictionary.md)")

    match = df[col].str.lower().isin(vals)
    df = df[match] if keep else df[~match]
    print(f"  {arg}: {len(df)} rows left")
    i += 1

if cols:
    missing = [c for c in cols if c not in df.columns]
    if missing:
        sys.exit(f"Unknown column(s) in --cols: {missing}")
    df = df[cols]

df.to_csv(out, index=False)
print("Wrote", len(df), "rows to", out)
