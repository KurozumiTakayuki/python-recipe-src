import csv

with open('sample.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
