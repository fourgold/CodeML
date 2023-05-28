import pandas as pd

# todo 0.基础
# data：一组数据(ndarray 类型)。ndarray、series, map, lists, dict
# index：数据索引标签，如果不指定，默认从 0 开始。
# dtype：数据类型，默认会自己判断。
# name：设置名称。
# copy：拷贝数据，默认为 False
a = pd.Series(data=[1, 2, 3, 4, 5], index=['a', 'b', 'c', 'e', 'f'], name='hello')  # 列向量
print(a)
print(type(a))
print(a.dtype)

# todo 1.使用dict创建数组 多列后会把类型设置成float NaN值只能继承于Float64 如果另外指定索引 数据的索引对应不上会丢失
b = {'a': 1, 'b': '2'}
c = pd.Series(b)
print(c)
print(c.dtype)

dict1 = {'a': 1, 'b': 1, 'c': 3}
print('dict1', dict1)
c = pd.Series(dict1)
print(c.dtype)

d = pd.Series(data=dict1, index=['a', 'b', 'e', 'd'])  # 这样子数据会丢失
print(d.dtype)
print(d)

# todo 2.使用二维数据创建Series 不能使用二维数据创建Series
print("使用二维数据创建Series")
a = [[1, 2, 3]]
s = pd.Series(data=a)
print(s)

# todo 3.使用标量创建Series 标量会是所有的值
print("\n标量")
s = pd.Series(5, index=['a', 'b', 'c'])  # 标量
print(s)
