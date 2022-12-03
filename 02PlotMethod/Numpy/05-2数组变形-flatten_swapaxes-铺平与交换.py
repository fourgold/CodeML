import numpy as np

a = np.array([[1, 2], [3, 4]])
print(a.flatten())  # 打平

# 转置
print(a.T)
print(np.dot(a, a.T))
