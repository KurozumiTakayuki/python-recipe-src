import csv

sample_list = [["col1", "col2", "col3"], [101, 102, 103], [201, 202, 203], [301, 302, 303]]
with open('sample2.csv', 'w', newline='') as f:
    writer = csv.writer(f, lineterminator='\n')
    for row in sample_list:
        writer.writerow(row)
