import re
import pandas as pd


# читаем данные с сайта и преобразуем их в список
def file_for_list(file):
    with open(file, "r") as my_file:
        data = my_file.readlines()
    str_data = str(data)  # собираем в строку все содержимое файла
    new_list = str_data.split(',')  # строка превращается в список и разделяется на элементы по символу ","
    # каждое поле разбивается на элемент списка. Что плохо - адрес тоже разбивается на части. Либо можно
    # делить по символу "}", тогда одно сообщение - один элемент
    return new_list


# очичение элементов списка
def clean_str(string):
    b = str(string)
    result = re.sub('["\[\'\]{]', '', b)
    result_fin = (re.sub('results:', '', result)).split(', ')
    return result_fin


a = file_for_list('C:/Users/asus_/Desktop/test.txt')
id_el = list(filter(lambda i: '"id"' in i, a))  # находим все элементы, содержащие запись об id
reason = list(filter(lambda i: '"reason"' in i, a))  # находим все причины обращений

# очищаем все элементы списка от лишних символов
new_str_id = clean_str(id_el)
new_str_rsn = clean_str(reason)

# записываем в csv
frame = pd.DataFrame([new_str_id, new_str_rsn])  # собираем все списки
frame1 = frame.transpose()  # транспонируем фрейм, чтобы названия полей стали столбцами
frame1.to_csv('C:/Users/asus_/Desktop/allprblms.csv', index=False, encoding='cp1251')  # экспортируем в файл

