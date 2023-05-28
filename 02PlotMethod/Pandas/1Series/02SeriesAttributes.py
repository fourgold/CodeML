import pandas as pd

i = 0
s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print('{}.基础演示'.center(20, '-').format(i := i + 1))
print(s)

# todo 索引
print('{}.索引'.center(20, '-').format(i := i + 1))
print(s[0])  # 直接按顺序
print(s['a'])  # 按照索引长度
print(s[0:3:2])  # 按照切片取
print(s[['a', 'b', 'd']])  # 标签索引 索引过长会报错 传行索引
print(s[[1, 2, 3]])  # 直接按索引取

# todo 维度
print('{}.维度'.center(20, '-').format(i := i + 1))
print(s.shape)  # 形状
print(s.size)  # 元素数目
print(s.ndim)  # 数组的维度
print(s.index)  # 查看标签
print(s.axes)  # 轴
print(s.values)  # 值
print(s.head(1))  # 查看头几条数据
print(s.tail(1))  # 查看后面几条数据
print(s.isnull())  # 检测缺失值 对象的功能
print(s.notna())  # 返回布尔矩阵
print(s.notnull()) # 返回布尔矩阵
print(pd.notnull(s)) # 返回布尔矩阵
pass
