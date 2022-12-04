import numpy as np

# 快速创建数组的几种方式
# todo 1.empty 创建一个新数组 ？
print(np.empty((2, 3), dtype=np.int16))
a = ([1, 2, 3], [4, 5, 6])
print(np.empty_like(a))

a = np.array(a)
print(a)
print(np.empty_like(a, dtype=np.int32))

# todo 2.zeros 创建一个全0数组
print(np.zeros((2, 3), dtype=np.int32))
print(np.zeros_like(a))

# todo 3.ones 返回给定形状于类型的新数组 并用1填充
print(np.ones((2, 3), dtype=np.int32))
print(np.ones_like(a))

# todo 4Functions.full 使用填充数制作新数组 给定类型将会覆盖原有类型
print()
print(np.full((3, 3), 1))
print(np.full_like(a, 1))

# todo 5.eye 据单位矩阵的特点,任何矩阵与单位矩阵相乘都等于本身
print(np.eye(3))
print(np.eye(3, 4))
print()
print(np.eye(3, 4, k=1))  # k是对角线的索引 默认为0 表示主对角线 正值表示上对角线 负值表示下对角线

# todo 6.identity(n) #单位矩阵
print(np.identity(3, dtype=np.int32))
