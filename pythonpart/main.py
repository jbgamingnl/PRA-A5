import csv
file = open('Hockey_Eerste_klasse_tussenstand.csv', "r")
reader = csv.DictReader(file, delimiter=';')
filesList = list(reader)
overtredingenAantal = 0
for overtredingen in filesList:
    overtredingenAantal = overtredingenAantal + int(overtredingen['overtredingen'])
print(overtredingenAantal)