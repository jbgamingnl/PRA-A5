import pandas as pd
from datetime import datetime, timedelta

data = pd.read_excel("data/Hockey_Eerste klasse_tussenstand.xlsx")
df = pd.DataFrame(data)

overtredingenAantal = data["overtredingen"].sum()

MeanOvertredingen = data["overtredingen"].mean()

data_stored = data.sort_values("overtredingen", ascending=False)
top5Overtredingen = data_stored.head(5).drop(columns=["divisie", "stadion"], errors="ignore")

df["datum"] = pd.to_datetime(df["datum"], format="%d/%m/%Y", errors="coerce")

today = datetime.now()
twentyonedaysago = today - timedelta(days=21)
mask = (df["datum"] >= twentyonedaysago) & (df["overtredingen"] <= 1)
CorrectDate = df.loc[mask].drop(columns=["divisie", "stadion"], errors="ignore")

with open("data/overtredingAantal.txt", "w", encoding="utf-8") as file:
    file.write(str(overtredingenAantal))
with open("data/overtredingMean.txt", "w", encoding="utf-8") as file:
    file.write(str(MeanOvertredingen))
with open("data/Top5Overtredingen.txt", "w", encoding="utf-8") as file:
    file.write(top5Overtredingen.to_string(index=False))
with open("data/FilteredData.txt", "w", encoding="utf-8") as file:
    file.write(CorrectDate.to_string(index=False))
print("Done making files")