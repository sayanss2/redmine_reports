# Модуль взаимодействия с redmine для построения отчетов

import redminelib  # install from pip "redminelib"
import os
import shutil
import datetime
from dateutil.relativedelta import relativedelta  # install from pip "python-dateutil"

# - functions
# def print_list_red(x_arg_input):
#     for data in x_arg_input:
#         print(data)
today = datetime.date.today()
mouth_report = today + relativedelta(months=-1)
mouth_plan = today + relativedelta(months=+1)

# - auth
red = redminelib.Redmine('http://red.eltex.loc', key='01ec8ef40c680c06b32e7201dfd80c328803ee4b')
# print(' auth +', red.url, '\n','Ваше Имя:', red.user.get('current')) #Получение адреса и имени пользователя
# print(' Ваш ID:', red.user.get('current').id) #Получение ID пользователя

# issue_custom_field_values_2 - Quality Assurance 6 статус это Rejected
issues = red.issue.filter(cf_2='me', status_id='!6',
                          updated_on='>=' + str(mouth_report))

# print_list_red(issues)

# Выгрузка в csv
shutil.rmtree('artifacts/', ignore_errors=True)
if not os.path.exists('artifacts/'):
    os.makedirs('artifacts/')
    issues.export('csv', savepath='artifacts/', filename='issues_control.csv',
                  columns=['project', 'fixed_version', 'status', 'subject'])  # Экспорт в csv задач

# МУСОР_МУСОР

# print_list_red(red.user.get('current')) #Информация о пользователе
# 5 статус это Closed
# 6 статус это Rejected
# 9 статус это Testing
# ,'2','3','4','5','6','8','9','10','11','12','13'
