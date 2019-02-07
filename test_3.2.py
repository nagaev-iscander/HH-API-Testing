# использование поля в 512 символов

import requests

STATUS_NOT_FOUND=400
CONTENT_TYPE_ANSWER="application/json; charset=UTF-8"
log_name="test_3.2.log"

URL="https://api.hh.ru/vacancies/"
HEADERS = {'User-Agent': 'HomeTask testing'}
text_data=['a']*512
PARAMS={'text': text_data}

f = open(log_name, 'w')

response = requests.get(URL, headers=HEADERS, params=PARAMS)
if(response.status_code!=STATUS_NOT_FOUND):
    f.write("Response_status=" + response.status_code + '\n')
    print("NOT OK")
else:
    f.write("OK\n");
    print("OK")

f.close()
