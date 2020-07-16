#Модуль создания шаблона .doc файла для построения отчета

# lib
from jinja2 import Template
import csv_parser


xml_body = open('../result_file/xml/xmlfile_123121.fodt').read()
#xml_body = open('../result_file/xml/body_template.xml').read()
xml_body_template = Template(xml_body)
output_from_parsed_template = xml_body_template.render(xml_project_name = csv_parser.get_ProjectVersion(), xml_count_project = csv_parser.get_cntProjectVersion())


with open("../result_file/r_xml_file_fodt.fodt", "w") as f:
    f.write(output_from_parsed_template)