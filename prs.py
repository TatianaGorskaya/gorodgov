import requests as rq
import time

base_url = "https://gorod.gov.spb.ru/api/v3.2/problems/all/?page="
for i in range(1, 1001):
    url = base_url + str(i)
    r = rq.get(url)
    time.sleep(0.4)
    new_file = open('C:/Users/asus_/Desktop/prsallpr.txt', 'a')
    new_file.write(r.text)
    new_file.close()

