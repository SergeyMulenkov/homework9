# import pandas as pd
#
# file = pd.read_csv('D:\GeekBrains\Studies\Python\homeworks\homework9\sample_data\california_housing_train.csv')

# # Задача 40: Работать с файлом california_housing_train.csv, который находится в папке
# # sample_data. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)

# print(file.loc[(file['population'] > 0) & (file['population'] < 500), ['median_house_value']])

# Задача 42: Узнать какая максимальная households в зоне минимального значения population

# print(file.loc[file['population'] == file['population'].min(), ['households']].max())