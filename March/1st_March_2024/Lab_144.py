# open csv file

import csv

with open('test.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        print(row)
        line_count += 1
    print(line_count)