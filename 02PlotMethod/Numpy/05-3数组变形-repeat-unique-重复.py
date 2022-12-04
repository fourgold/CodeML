import numpy as np

# print(np.repeat(3, 4Functions))  # 重复3 重复4遍
x = np.array([[1, 2], [3, 4]])
print(x)
print(np.repeat(x, 2))
print(np.repeat(x, 3, axis=0)) # 该轴的重复次数
print(np.repeat(x, [1, 4], axis=0))  # 指定 第个元素参数重复的次数 第二个参数第二个元素的重复次数
