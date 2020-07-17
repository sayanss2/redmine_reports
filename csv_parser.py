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
#print(dict_s1)



#  Подсчет количества Проектов
#print(dict_s1.keys())
#print(dict_s1.keys())
# key = list(dict_s1.keys())[0]
# val = list(dict_s1.get(key).keys())[0]


# for key in dict_s1:
#     for val in dict_s1.get(key):
#         print(key, '/', val)


def get_cntProjectVersion():
    cnt = 0
    for key in dict_s1:
        for val in dict_s1.get(key):
            cnt += 1
    return cnt


def get_ProjectVersion():
    verList = []
    for key in dict_s1:
        for val in dict_s1.get(key):
            verList.append(key+'/'+val)
    return verList


print('Count = ', get_cntProjectVersion())
print(*get_ProjectVersion(), sep='\n')