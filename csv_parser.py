# -*- coding: utf-8 -*-

# module csv parser

# lib
import csv

csv_file_path = 'issues21333222.csv'


def parser_csv_file():
    lines = []
    with open(csv_file_path, 'r') as csvfile:
        csv_read = csv.DictReader(csvfile)
        for i in csv_read:
            lines.append(i)
    return lines


arg1_info = 'Проект'
arg2_info = 'Версия'
arg3_info = 'Статус'
arg4_info = 'Тема'
arg5_info = '#'
dict_s1 = {}  # Словарь по Проект:Версия
dict_s2 = {}
for i in parser_csv_file():  # Строим Проект
    if str(i[arg1_info]) in dict_s1.keys():
        pass
    else:
        dict_s1[i[arg1_info]] = {}
        for j in parser_csv_file():   # Строим Версию
            if str(i[arg1_info]) in j[arg1_info]:   # Проверка по Проекту
                if dict_s1.get(str(i[arg1_info])).get(j[arg2_info], {}):
                    pass
                else:
                    for k in parser_csv_file():
                        if str(i[arg1_info]) in k[arg1_info]:
                            if str(j[arg2_info]) in k[arg2_info]:
                                dict_s2[k[arg5_info]] = [k[arg4_info], k[arg3_info]]
                    dict_s1[str(i[arg1_info])][j[arg2_info]] = dict_s2
                    dict_s2 = {}

print(dict_s1)

# МУСОР

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
