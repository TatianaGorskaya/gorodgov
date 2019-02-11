import requests as rq
import time

new_file = open('C:/Users/asus_/Desktop/allprbl11.txt', 'a')

base_url = "https://gorod.gov.spb.ru/api/v3.2/problems/all/?page=%d"
for i in range(1000, 4000):
    # url = base_url + str(i)
    url = base_url % i
    r = rq.get(url)
    time.sleep(0.4)
    new_file.write(r.text)
    print(i)


new_file.close()

