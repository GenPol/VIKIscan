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

    check_sum = {}

    for i, num in enumerate(NumList):
        check_sum[num] = check_sum.get(num, 0) + float(SumList[i])

    return check_sum  # {100: 5, 200: 10, 300: 15}




data = tocheck(beznal, checks)

df = pd.DataFrame.from_dict(data, orient='index')


# Экспорт в Excel
writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')
writer.close()