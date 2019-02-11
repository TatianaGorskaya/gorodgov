import requests as rq
import time
import pandas as pd

# файл со скачанными id всех обращений
id_of_prblms = pd.read_csv('C:/Users/asus_/Desktop/IDsnow.csv', sep=",", encoding='latin-1')['ID']
all_id = pd.Series.tolist(id_of_prblms)

new_file = open('C:/Users/asus_/Desktop/detailssnow.txt', 'a', encoding='utf-8-sig')

base_url = "https://gorod.gov.spb.ru/public_api/problems/%d/"
for i in all_id:
    url = base_url % i
    print(i, all_id.index(i))
    r = rq.get(url)
    time.sleep(0.4)
    new_file.write(r.text)

new_file.close()
