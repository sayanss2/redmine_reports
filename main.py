import redminelib
import csv

## - functions
def print_list_red (x_arg_input):
    for data in x_arg_input:
        print(data)

## - auth
red = redminelib.Redmine('http://red.eltex.loc', key='01ec8ef40c680c06b32e7201dfd80c328803ee4b')
print("================================================")
print(' auth +', red.url, '\n','Ваше Имя:', red.user.get('current')) #Получение адреса и имени пользователя
print(' Ваш ID:', red.user.get('current').id) #Получение ID пользователя 
print("================================================")
print("================================================")


issues = red.issue.filter(cf_2='me', status_id='!6', updated_on='>=2020-07-03') # issue_custom_field_values_2 - Quality Assurance 6 статус это Rejected


# print(list(issues))
print_list_red(issues)
print("================================================")
print("================================================")

# Выгрузка для linux
issues.export('csv', savepath='../result_file/', filename='issues21333222.csv', columns=['project','fixed_version','status','subject']) #Экспорт в csv задач
# Выгрузка для Windows
#issues.export('csv', savepath='./result_file/', filename='issues21333222.csv', columns=['project','fixed_version','status','subject']) #Экспорт в csv задач















##МУСОР_МУСОР

#print_list_red(red.user.get('current')) #Информация о пользователе
# 5 статус это Closed
# 6 статус это Rejected
# 9 статус это Testing
# ,'2','3','4','5','6','8','9','10','11','12','13'
## - get all project
#project_red = red.project.all()
#print_list_red(project_red)
## - get issue
#print(red.project.get('IoT'))

##
# iu = red.user.get('current').issues
# print_list_red(iu)

# print("================================================")
# list_issues = list(issues)
# print(list_issues)
# print("================================================")
# a = list_issues[1:2]
# print(a)
#usuei = red.issue.get(150779)
#print(usuei)
#usuei.export('pdf', savepath='/home/v/python_file')
#issues = red.issue.filter(assigned_to_id='me')