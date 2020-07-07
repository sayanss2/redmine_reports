# -*- coding: utf-8 -*-

#module csv parser

# lib
import csv, json

csv_file_path = '../result_file/issues21333222.csv'



# def read_csv_file(number_column):
#     with open(csv_file_path, 'r') as csvfile:
#         csv_read = csv.reader(csvfile, delimiter = ';')
#        #number = 0
#         my_list = []
#         next(csv_read) #переход на следующие значение
#         for line in csv_read:
#             print (line[number_column])
#             my_list.append(line[number_column])
#     print('Количество элементов = ', len(my_list)) #Длинна списка
#     print(my_list) # Показать список
# read_csv_file(2)


# with open(csv_file_path, 'r') as csvfile:
#     csv_read = csv.DictReader(csvfile)
#     for row in csv_read:
#         print(row['Версия'])

def parser_csv_file():
    lines = []
    with open(csv_file_path, 'r') as csvfile:
        csv_read = csv.DictReader(csvfile)
        for i in csv_read:
            lines.append(i)
    return lines
        # for row in csv_read:
        #     print(row[_info])

arg1_info = 'Проект'
dict_s = {}
for i in parser_csv_file():
    dict_s[i[arg1_info]] = ""
for i in dict_s.keys():
    print(i)
    for j in parser_csv_file():
        if i in j[arg1_info]:
            print(j['version'])
    print("_________________")

# print(parser_csv_file(arg_info))
# for row in parser_csv_file():
#     print(row[arg_info])


# with open(csv_file_path, 'r') as csvfile:
#     csv_read = csv.DictReader(csvfile)
#     i = 0
#     for row in csv_read:
#         print(row)
#         print('-------------------line_------------------------------------')
#         i = i + 1
#         print(i)
#         print(row['Проект'])
#         print('-------------------line_------------------------------------')