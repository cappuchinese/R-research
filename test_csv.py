import csv

with open("testrun1.csv") as csvfile:
    reader = csv.reader(csvfile)

for row in reader:
    print(", ".join(row))
