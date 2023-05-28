import numpy as np
import pandas as pd

data = [{'name': '张三', 'age': 15, 'num': 1}, {'name': '李四', 'age': 16, 'num': 2}, {'name': '王五', 'age': 3, 'num': 3}]
df01 = pd.DataFrame(data, index=['a', 'b', 'c'])
print(df01)

a1 = np.array([['张三', 15, 1], ['lisi', 16, 2], ['siy', 16, 3]])
print(a1)

print(df01.index)
print(df01['name'][0])

# todo 1 iloc[] 通过索引查找 取数 取行数据 第一个参数是行 : 所有 第二个参数是列
"""
df.iloc[]
    位置索引进行索引/切片
    [n] 取出第N行的数据 返回一个Series
    [[n]] 切片取出第n行数据 返回是一个DataFrame
    [:,n] 取出第N列 返回一个Series
    [:,[n]] 切片取出第N列的数据，返回是一个DataFrame
    [n,m]  取出第n行第n列的元素，返回一个元素
"""
print('\n模仿平时索引,根据数值索引取数')
a = df01.iloc[[0, 2]]  # 取行
print(a)
print(type(a))

# todo 2 iloc[] 查找 取数 取列数据 df01.iloc[[0,1]]
b = df01.iloc[:, [1]]
print(b)

# todo 3 df.loc[] 通过标签查找 第一个参数行，第二个参数传列 标签索引
print("\ndf.loc")
print(df01['name'])  # 按照列名取数据
print(type(df01['name']))
print(df01.loc[:, ["name", "age"]])
print(df01.columns)
print(df01.index)
df01.index = ['b', 'c', 'd']
print(df01.index)
a = df01.columns.values
print(df01.columns)
print(a)