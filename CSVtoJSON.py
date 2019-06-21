import csv
import json

csvfile = open('E:/Park_Ivnt/Python/SciNames.csv', 'r')
jsonfile = open('E:/Park_Ivnt/Python/SciNames.json', 'w')

fieldnames = ("name", "code")
reader = csv.DictReader(csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')
