import pandas as pd
from pandas import DataFrame


# pandas是一个数据处理的包，本身提供了许多读取文件的函数，像read_csv（读取csv文件），
# read_excel（读取excel文件）等，只需一行代码就能实现文件的读取
df = pd.read_excel(r'data_openpyxl.xlsx', sheet_name=0)
print(type(df.head))
print(df.head())

data = {
   'name': ['张三', '李四', '王五'],
   'age': [11, 12, 13],
   'sex': ['男', '女', '男']
}

df = DataFrame(data)
df.to_excel('new1.xlsx')

