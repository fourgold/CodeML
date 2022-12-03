import matplotlib.pyplot as plt
import numpy as np

# 用于显示模式
plt.figure()
data = np.array([[0, 50, 200], [200, 100, 0], [0, 150, 200]])
plt.imshow(data,cmap='Greys') # 可以传很多模式
plt.show()

