import json
import pandas as pd


with open('C:/Users/asus_/Desktop/detailssnow_corr.txt', encoding='utf-8-sig') as data_file:
    data = json.load(data_file)


def get_list(a, b):
    first_key = a
    second_key = b
    new_list = []
    for i in range(0, 14288):
        new_list.append(data[first_key][i][second_key])
    return new_list


details_id = get_list('allresults', 'id')
details_district = get_list('allresults', 'district_name')
frame = pd.DataFrame([details_id, details_district])
frame1 = frame.transpose()
frame1.to_csv('C:/Users/asus_/Desktop/IDDistrict.csv', encoding='utf-8-sig')

