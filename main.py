# Running report generation in 'Redmine'

import red_api
import template_doc

if __name__ == '__main__':
    red_api_key = ""
    # date = red_api.mouth_report  # Example, 2020-06-30 (today - 1 mouth)
    date = '2020-06-28'

    red_api.put_api(red_api_key, gen_csv=True, start_date=date)
    template_doc.create_report(red_api_key)
