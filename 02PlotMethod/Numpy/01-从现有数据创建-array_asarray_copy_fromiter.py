import numpy as np
from typing import Iterable

# todo 1.array
a = np.array([[[2, 3], [2, 4], [4, 6]], [[2, 5], [5, 6], [6, 8]], [[3, 4], [4, 5], [8, 6]]])  # 轴的数量或者维度的数量

print(isinstance(a, Iterable))
print(a.dtype)  # 数组元素的数据类型
print(a.ndim)  # 指定生成数组的最小维度
print(a.size)  # 矩阵的运行逻辑
print(a.itemsize)  # 对象中每个元素的大小

# todo 2.asarray 传入对象是nd对象同时类型不变时，不会发生复制
a = [1, 2, 3]
arr1 = np.array(a)
arr2 = np.asarray(a)

print(arr1)
print(arr2)
a.insert(0, 3)
print(arr1)  # 申请新内存
print(arr2)  # 申请新内存

a = np.array(a)
na1 = np.array(a)
na2 = np.asarray(a)
a[0] = 5
print('a', a)
print('na1', na1)
print('na2', na2)  # 跟随先前的nd对象一起变化，不会发生复制

# todo 3.copy()
a = [1, 2, 3, 4]
print('a', a)
b = a.copy()
print(id(a), id(b))

b = np.copy(a)
print(type(a), type(b))

a2 = np.array([1, 2, 3])
a3 = np.copy(a2)
a2[2] = 0

print(a2)
print(a3)

a4 = a3.copy()  # 可以使用对象直接调用
print(a4)
# todo 4Functions.fromiter 数组整体类型转换
it = list((x * x for x in range(5)))
print(it)
print(np.fromiter(it, dtype=np.float64))
