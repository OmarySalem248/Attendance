# Usage: python3 xlsx_to_csv.py Student_attendance_dataset.xlsx
# Needs: pip install pandas openpyxl
import sys
import pandas as pd

df = pd.read_excel(sys.argv[1])          # 1. read the spreadsheet

df = df.rename(columns={                  # 2. short, code-friendly column names
    "Calendar year": "year", "State/Territory": "state", "School Sector": "sector",
    "Sex/Gender": "sex", "Geolocation": "geo", "Indigenous Status": "indigenous",
    "Disaggregation": "disaggregation", "School Year Level": "year_level",
    "Attendance Rate": "rate", "Attendance Level": "level"})

# 3. "-" means suppressed. Turn it into a real number or blank.
df["level"] = pd.to_numeric(df["level"], errors="coerce")

# 4. Keep only the rows this chart needs (this is what shrinks the file).
#    Full-year rows (not the 1st-4th "Quarter" rows), all students, Years 1-10, states only.
keep = (
    ~df["disaggregation"].isin(["1st Quarter", "2nd Quarter", "3rd Quarter", "4th Quarter"])
    & (df["sector"] == "All") & (df["sex"] == "All") & (df["geo"] == "All")
    & (df["indigenous"] == "All") & (df["year_level"] == "Years 1-10")
    & (df["state"] != "Australia")
)
small = df.loc[keep, ["state", "year", "rate", "level"]]

small.to_csv("attendance_by_state.csv", index=False)   # 5. write the small file
print(len(df), "rows in ->", len(small), "rows out")
print(small.head())