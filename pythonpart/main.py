import csv
file = open('pythonpart/data/Hockey_Eerste_klasse_tussenstand.csv', "r")
file2 = open('pythonpart/data/totalData.txt', "w+")
reader = csv.DictReader(file)
filesList = list(reader)

overtredingenAantal = 0
overtredingenGemiddel = 0
XInt = 0

for overtredingen in filesList:
    overtredingenAantal = overtredingenAantal + int(overtredingen['overtredingen'])
    XInt = XInt + 1

overtredingenGemiddel = overtredingenAantal/XInt

names = []
overtredingenTop5 = []

for row in file:
    names.append(row['scheidsrechter'])
    overtredingenTop5.append(row['overtredingen'])

print(f"XInt {XInt}")
print(overtredingenAantal)
print(overtredingenGemiddel)
print(names)
file2.write(f"Total overtredingen : {overtredingenAantal} \nGemmideled overtredingen : {overtredingenGemiddel}")
file2.close()
file.close()