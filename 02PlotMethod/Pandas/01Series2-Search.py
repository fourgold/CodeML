import pandas as pd

s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(s)
# todo 1 直接位置索引访问 切片 标签 属性 方法
print('direct', s[0])
print(s[0:3:2])
print(s[['a', 'b', 'd']])  # 标签索引 索引过长会报错
print(s.shape)
print(s.size)
print(s.ndim)  # 数组的维度
print(s.index)  # 查看标签
print('索引', s.axes)
print('值', s.values)
print(s.head(1))  # 查看头几条数据
print(s.tail(1))  # 查看后面几条数据
# 检测缺失值 对象的功能
print('缺失值', s.isnull())
print(s.notna())
print(s.notnull())
print(" ")
print(pd.notnull(s))