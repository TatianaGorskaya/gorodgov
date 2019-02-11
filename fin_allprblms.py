import json
import pandas as pd

# обработка скачанного json по общему описанию обращений

# руками в txt заменила }{ на },{, завернула все содержимое в {"allresults:"[...]}
with open('C:/Users/asus_/Desktop/allprbl11_copy.txt') as data_file:
    data = json.load(data_file)


# создаем список из нужных нам элементов
def get_list(a, b, c):
    first_key = a
    second_key = b
    third_key = c
    new_list = []
    for i in range(0, 2998):
        for n in range(0, 10):
            new_list.append(data[first_key][i][second_key][n][third_key])
    return new_list


requests_date = get_list('allresults', 'results', 'dt')
requests_reason = get_list('allresults', 'results', 'reason')
requests_id = get_list('allresults', 'results', 'id')


# записываем в csv
frame = pd.DataFrame([requests_id, requests_reason, requests_date])  # собираем все списки
frame1 = frame.transpose()  # транспонируем фрейм, чтобы названия полей стали столбцами
frame1.to_csv('C:/Users/asus_/Desktop/newprblm.csv', index=False, encoding='cp1251')  # экспортируем в файл

