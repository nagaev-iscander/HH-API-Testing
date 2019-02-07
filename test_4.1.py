# использование поля в виде бинарных данных

import requests

STATUS_NOT_FOUND=400
SERVER_ERROR=500
CONTENT_TYPE_ANSWER="application/json; charset=UTF-8"
log_name="test_4.1.log"

URL="https://api.hh.ru/vacancies/"
HEADERS = {'User-Agent': 'HomeTask testing'}
text_data=[1]*10
PARAMS={'text': text_data}

f = open(log_name, 'w')

response = requests.get(URL, headers=HEADERS, params=PARAMS)
if(response.status_code<STATUS_NOT_FOUND or response.status_code>=SERVER_ERROR):
    f.write("Response_status=" + response.status_code + '\n')
    print("NOT OK")
else:
    f.write("OK\n");
    print("OK")

f.close()
