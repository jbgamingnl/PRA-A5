import pandas as pd
from datetime import datetime, timedelta

data = pd.read_excel("data/Hockey_Eerste klasse_tussenstand.xlsx")
df = pd.DataFrame(data)

overtredingenAantal = data["overtredingen"].count()

SumOvertredingen = data["overtredingen"].sum()

data_stored = data.sort_values("overtredingen", ascending=False)
top5Overtredingen = data_stored.head(5)

df["datum"] = pd.to_datetime(df["datum"], format="%d/%m/%Y", errors="coerce")

today = datetime.now()
twentyonedaysago = today - timedelta(days=21)
mask = (df["datum"] >= twentyonedaysago) & (df["overtredingen"] <= 1)
CorrectDate = df.loc[mask]

output = (
    f"aantal overtredding: {overtredingenAantal}\n"
    f"Gemiddeld overtredingen: {SumOvertredingen}\n"
    f"Top 5 overtredingen:\n{top5Overtredingen.to_string(index=False)}\n\n"
    f"Filtered data (last 21 days and overtredingen <= 1):\n{CorrectDate.to_string(index=False)}\n"
)

with open("data/output.txt", "w", encoding="utf-8") as file:
    file.write(output)

print("Output written to 'output.txt'")