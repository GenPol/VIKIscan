import pandas as pd
import warnings

warnings.simplefilter("ignore")

# Читаем файл Excel
data = pd.read_excel(r"18nov.xlsx")

# Извлекаем колонку 'column_name' из данных
beznal = data['Сумма безналичными']
checks = data['Чек']


def tocheck(sums, nums):
    # convert to list data
    SumList = [i for i in sums]
    NumList = [i for i in nums]
    return SumList



print(tocheck(beznal, checks))
