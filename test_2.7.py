# использование NOT

import requests

STATUS_200_OK=200
CONTENT_TYPE_ANSWER="application/json; charset=UTF-8"
log_name="test_2.7.log"

URL="https://api.hh.ru/vacancies/"
HEADERS = {'User-Agent': 'HomeTask testing'}
text_data="Python NOT JavaScript"
PARAMS={'text': text_data}

f = open(log_name, 'w')

response = requests.get(URL, headers=HEADERS, params=PARAMS)
if(response.status_code!=STATUS_200_OK):
    f.write("Response_status=" + response.status_code + '\n')
    print("NOT OK")
elif(response.headers['Content-Type']!=CONTENT_TYPE_ANSWER):
    f.write("Content-Type=" + response.headers['Content-Type'] + '\n')
    print("NOT OK")
elif(int(response.json()['found'])<=0):
    f.write("Vacancies found=" + str((response.json()['found'])) + '\n')
    print("NOT OK")
else:
    f.write("OK\n");
    print("OK")

f.close()
