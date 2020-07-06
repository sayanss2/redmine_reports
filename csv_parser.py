#module csv parser

# lib
import csv

with open('../result_file/issues21333222.csv', 'r') as csvfile:
    csv_read = csv.reader(csvfile, delimiter = ';')
    for line in csv_read:
        print(line[2])

