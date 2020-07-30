# Running report generation in 'Redmine'

import red_api
import template_doc

if __name__ == '__main__':
    red_api_key = "7a736b6cd99b4ba28273ff39797a96ab90e0195c"

    red_api.put_api(red_api_key, True)
    template_doc.create_report(red_api_key)
