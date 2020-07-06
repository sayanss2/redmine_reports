#module csv parser

# lib
import csv

csv_file_path = '../result_file/issues21333222.csv'

def read_csv_file(number_column):
    with open(csv_file_path, 'r') as csvfile:
        csv_read = csv.reader(csvfile, delimiter = ';')
        for line in csv_read:
            return (line[number_column])

read_csv_file(2)


