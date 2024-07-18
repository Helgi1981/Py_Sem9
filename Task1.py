# Задача №1. Решение в группах

# 1. Прочесть с помощью pandas файл california_housing_test.csv, который находится в папке
# sample_data
# 2. Посмотреть сколько в нем строк и столбцов
# 3. Определить какой тип данных имеют столбцы

from pandas import read_csv

# Указываем путь к файлу и читаем его
file_path = 'california_housing_test.csv'
data = read_csv(file_path)

# Определяем тип данных файла
print(type(data))

# Смотрим, сколько в файле строк и столбцов
print(data.shape)

# Определяем, какой тип данных имеют столбцы
print(data.dtypes)

# Вызываем метод info
print(data.info())

# Вызываем метод describe (информация о нашем data.frame)
print(data.describe())
