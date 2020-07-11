# -*- coding: utf-8 -*-

# module csv parser

# lib
import csv

csv_file_path = '../result_file/issues21333222.csv'

def parser_csv_file():
    lines = []
    with open(csv_file_path, 'r') as csvfile:
        csv_read = csv.DictReader(csvfile)
        for i in csv_read:
            lines.append(i)
    return lines


# arg1_info = 'Проект'
# arg2_info = 'Версия'
# arg3_info = 'Статус'
# arg4_info = 'Тема'
# arg5_info = '#'
# dict_s1 = {} #Словарь по Проект:Версия
# dict_s2 = {}
# for i in parser_csv_file():
#         if str(i[arg1_info]) in dict_s1.keys():
#             pass
#         else:
#             dict_s1[i[arg1_info]] = {}
#             dict_s2 = {} 
#             for j in parser_csv_file():
#                 if str(i[arg1_info]) in j[arg1_info]:
#                     dict_s2[j[arg5_info]] = [j[arg4_info], j[arg3_info]]
#                     dict_s1[str(i[arg1_info])][j[arg2_info]] = dict_s2

#print(dict_s1)


edibles = ['Проект','Версия', 'Статус', 'Тема', '#']
dict1 = {}

with open(csv_file_path, 'r') as csvfile:
    csv_read = csv.DictReader(csvfile)
    for row in csv_read:
        for p_vstav in edibles:
            #print(row[p_vstav], "\n")
            pd = dict1.update(row[p_vstav])
            print(pd)
















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
#     for row in csv_read:
#         print(row['Проект'])
