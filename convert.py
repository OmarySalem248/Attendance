# Usage: python3 xlsx_to_full.py Student_attendance_dataset.xlsx
# Needs: pip install pandas openpyxl
# Writes: attendance_full.csv (every row, every column, cleaned)
#         data_dictionary.md  (what each column contains, with every distinct value)
import sys
import pandas as pd

src = sys.argv[1]
df = pd.read_excel(src)
print("Read", len(df), "rows x", len(df.columns), "columns")

# Code-friendly names. The ORIGINAL name is kept in the data dictionary.
names = {"Calendar year": "year", "State/Territory": "state", "School Sector": "sector",
         "Sex/Gender": "sex", "Geolocation": "geo", "Indigenous Status": "indigenous",
         "Disaggregation": "disaggregation", "School Year Level": "year_level",
         "Attendance Rate": "rate", "Attendance Level": "level"}
df = df.rename(columns=names)

# "-" (value withheld) -> blank number, so charts never see text in a number column.
df["level"] = pd.to_numeric(df["level"], errors="coerce")

# Add ONE helper column, clearly marked: True for the rows ACARA calls "1st-4th Quarter".
# (These look like school advantage groups, not times of year. Confirm with ACARA's notes.)
q = ["1st Quarter", "2nd Quarter", "3rd Quarter", "4th Quarter"]
df["is_quarter_row"] = df["disaggregation"].isin(q)

df.to_csv("attendance_full.csv", index=False)

# Data dictionary: every column, its type, blanks, range or distinct values.
orig = {v: k for k, v in names.items()}
lines = ["# Data dictionary", "", f"Source file: {src}", f"Rows: {len(df)}", ""]
for c in df.columns:
    s = df[c]
    lines.append(f"## `{c}`" + (f"  (original column: \"{orig[c]}\")" if c in orig else "  (added by script)"))
    lines.append(f"- type: {s.dtype}; blank values: {int(s.isna().sum())}; distinct values: {s.nunique()}")
    if pd.api.types.is_numeric_dtype(s) and s.nunique() > 25:
        lines.append(f"- range: {s.min()} to {s.max()}")
    elif s.nunique() <= 60:
        lines.append("- values: " + "; ".join(f"{v} ({n})" for v, n in s.value_counts(dropna=False).sort_index().items()))
    lines.append("")
open("data_dictionary.md", "w").write("\n".join(lines))
print("Wrote attendance_full.csv and data_dictionary.md")