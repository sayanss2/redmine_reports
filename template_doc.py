# Модуль создания шаблона .doc файла для построения отчета

# lib
from jinja2 import Template  # install from pip "Jinja2"
import csv_parser
import red_api

months_number = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август',
                 9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}

xml_body = open('tReport/template.fodt').read()
xml_body_template = Template(xml_body)
report_user = red_api.red.user.get('current').lastname + ' ' + red_api.red.user.get('current').firstname[0] + '.'
output_from_parsed_template = xml_body_template.render(xml_project_name=csv_parser.get_project_version(),
                                                       xml_count_project=csv_parser.get_cnt_project_version(),
                                                       xml_count_issue=csv_parser.get_cnt_order,
                                                       xml_issues_name=csv_parser.get_order_project_version,
                                                       xml_name_user=report_user,
                                                       xml_month_report=months_number[red_api.today.month],
                                                       xml_month_plan=months_number[red_api.mouth_plan.month])


name_file = str(red_api.red.user.get('current').lastname) + '_План_на_' + str(months_number[red_api.today.month + 1]) + '_' + str(red_api.today.year) + '.fodt'
with open('artifacts/' + name_file, "w") as f:
    f.write(output_from_parsed_template)
