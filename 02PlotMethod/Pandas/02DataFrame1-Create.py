import numpy as np
import pandas as pd

# pandas.2DataFrame( data, index, columns, dtype, copy)
# 参数说明：
# data：一组数据(ndarray、series, map, lists, dict 等类型)。
# index：索引值，或者可以称为行标签。
# columns：列标签，默认为 RangeIndex (0, 1, 2, …, n) 。
# dtype：数据类型。
# copy：拷贝数据，默认为 False

array02 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [2, 5, 8]])
df01 = pd.DataFrame([1, 2, 3, 4, 5], index=["a", 'b', 'c', 'd', 'e'], columns=['firstCol'])
print(df01)
print(array02)
df03 = pd.DataFrame(array02)
print(df03)

df04 = pd.DataFrame(array02)
print(array02)
print(df04.values)

# df给ndarray加了行索引于列索引
print(df01.shape)


print(df01)
print(df01.shape)
print(df01.columns)
print(df01.values)
print(type(df01.values))
print(df01.axes)  # 行与轴的标签索引
print("方法")
print('\ninfo')
print(df01.info())
print('\ndescribe')
print(df01.describe())  # 至针对数值型的列进行统计性的描述
