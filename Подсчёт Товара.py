import pandas as pd

import warnings
warnings.simplefilter("ignore")


# Читаем файл Excel
data = pd.read_excel(r"C:\Users\user1c\Desktop\python project\18nov.xlsx")

# Извлекаем колонку 'column_name' из данных
prices = data['Сумма безналичными']
checes = data['Чек']

priceList = [i for i in prices]
checkList = [i for i in checes]

dictFinal = {}


# Если вы хотите сохранить данные в списке, вы можете сделать так:
#list_data = column.tolist()