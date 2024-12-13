import pandas as pd
from datetime import datetime,timedelta

data = pd.read_excel("data/Hockey_Eerste klasse_tussenstand.xlsx")

overtredingenAantal = data["overtredingen"].count()

SumOvertredingen = data["overtredingen"].sum()

data_stored = data.sort_values("overtredingen", ascending=False)
top5Overtredingen = data_stored.head(5)

datum = data["datum"]
datum = pd.to_datetime(data["datum"])
datum = data["datum"].dt.strftime("%d-%m-%Y")
today = datetime.now()
twentyonedaysago = today - timedelta(days=21)
filter = datum > twentyonedaysago

print(f"aantal overtredding : {overtredingenAantal}")
print(f"Gemiddeld overtredingen : {SumOvertredingen}")
print(f"Top 5 overtredingen :\n {top5Overtredingen}")
