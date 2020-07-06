#Модуль создания шаблона .doc файла для построения отчета

# lib
from jinja2 import Template

#xml_body = open('../result_file/xml/test_filef.xml').read()
xml_body = open('../result_file/xml/body_template.xml').read()
xml_body_template = Template(xml_body)
print(xml_body_template.render(xml_project_name='Eltex-SC (IoT-Core)', xml_issue_name='Обновить smart3.eltex-co.ru до версии 1.15 ядро 870'))

