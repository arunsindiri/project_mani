import pandas as pd

df = pd.read_csv("report_2026_01_07.csv", encoding="latin1")
df.to_excel("report_2026_01_07.xlsx", index=False)

print("Excel file created successfully")
