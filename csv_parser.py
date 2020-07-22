# -*- coding: utf-8 -*-

# module csv parser

# lib
import csv

csv_file_path = 'artifacts/issues_control.csv'


def parser_csv_file():
    lines = []
    with open(csv_file_path, 'r') as csvfile:
        csv_read = csv.DictReader(csvfile, delimiter=';')
        for i in csv_read:
            lines.append(i)
    return lines


arg1_info = 'Проект'
arg2_info = 'Версия'
arg3_info = 'Статус'
arg4_info = 'Тема'
arg5_info = '\ufeff#'
dict_s1 = {}  # Словарь по Проект:Версия
dict_s2 = {}
for i in parser_csv_file():  # Строим Проект
    if str(i[arg1_info]) in dict_s1.keys():
        pass
    else:
        dict_s1[i[arg1_info]] = {}
        for j in parser_csv_file():  # Строим Версию
            if str(i[arg1_info]) in j[arg1_info]:  # Проверка по Проекту
                if dict_s1.get(str(i[arg1_info])).get(j[arg2_info], {}):
                    pass
                else:
                    for k in parser_csv_file():
                        if str(i[arg1_info]) in k[arg1_info]:
                            if str(j[arg2_info]) in k[arg2_info]:
                                dict_s2[k[arg5_info]] = [k[arg4_info], k[arg3_info]]
                    dict_s1[str(i[arg1_info])][j[arg2_info]] = dict_s2
                    dict_s2 = {}


# print(dict_s1)


#  Подсчет количества Проектов
# print(dict_s1.keys())
# print(dict_s1.keys())
# key = list(dict_s1.keys())[0]
# val = list(dict_s1.get(key).keys())[0]


def get_cnt_project_version():
    cnt = 0
    for key in dict_s1:
        for val in dict_s1.get(key):
            cnt += 1
    return cnt


def get_project_version(return_sep=None):
    ver_list = []
    if return_sep:
        for key in dict_s1:
            for val in dict_s1.get(key):
                ver_list.append(key + '/' + val)
    else:
        for key in dict_s1:
            for val in dict_s1.get(key):
                line_str = key + '/' + val
                dict_str = {'oneline': line_str, 'project': key, 'version': val}
                ver_list.append(dict_str)
    return ver_list


def get_order_project_version(project_input=None, version_input=None):
    order_list = []
    if project_input and version_input:
        for key, value in dict_s1.get(project_input).get(version_input).items():
            url_value = 'http://red.eltex.loc/issues/' + key
            title_value = ' (' + value[0] + ')'
            status_value = value[1]
            dict_str = {'url': url_value, 'title': title_value, 'status': status_value}
            order_list.append(dict_str)
    return order_list


def get_cnt_order(project_input=None, version_input=None):
    cnt = 0
    if project_input and version_input:
        for item in dict_s1.get(project_input).get(version_input).items():
            cnt += 1
    return cnt


print('Count = ', get_cnt_project_version())  # Вывод кол-ва Проектов/Версий
for i in get_project_version():
    print(i.get('oneline'))  # Вывод наименования Проекта/Версии одной строкой
    print('Count = ', get_cnt_order(i.get('project'), i.get('version')))  # Вывод кол-ва задач в Проекте/Версии
    for j in get_order_project_version(i.get('project'), i.get('version')):
        print(j.get('url') + ' ' + j.get('title') + ' ' + j.get('status'))  # Вывод ссылки, наименования и статуса
        # задачи в Проекте/Версии

