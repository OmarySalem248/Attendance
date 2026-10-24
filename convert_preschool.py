# Usage: python convert_preschool.py "data/Preschool Attendance, 2025, Tables 1-3.xlsx"
# Needs: pip install pandas openpyxl
# Writes: data/preschool_attendance_2025.csv (one row per table x state x service type x hours band)
import re
import sys
import pandas as pd

src = sys.argv[1]
sheets = {"Table 1": "All children", "Table 2": "Aboriginal and Torres Strait Islander",
          "Table 3": "Disadvantaged"}

def clean(s):
    # Drop footnote markers like "(f)" or a cut-off "(" and extra spaces.
    return re.sub(r"\s*\([a-z]?\)?\s*$", "", str(s)).strip()

rows = []
for sheet, group in sheets.items():
    df = pd.read_excel(src, sheet_name=sheet, header=None)
    bands = [clean(b).replace("Attended ", "") for b in df.iloc[3, 1:].dropna()]
    state = None
    for _, r in df.iloc[4:].iterrows():
        label = r[0]
        if pd.isna(label):
            if pd.notna(r[1]):
                state = clean(r[1])          # state heading row
            continue
        if state is None or pd.isna(r[1]):
            break                            # reached the footnotes
        for i, band in enumerate(bands, start=1):
            rows.append({"table": sheet, "group": group, "state": state,
                         "service_type": clean(label), "hours_band": band,
                         "children": pd.to_numeric(r[i], errors="coerce")})

out = pd.DataFrame(rows)
out.to_csv("data/preschool_attendance_2025.csv", index=False)
print("Wrote", len(out), "rows to data/preschool_attendance_2025.csv")
