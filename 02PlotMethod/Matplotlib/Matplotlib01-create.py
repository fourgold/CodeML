from matplotlib import pyplot as plt
import numpy as np

# 隐式的创建画布
x = np.linspace(-3, 3, num=30)  # 等差数列 endPoint默认为true
y1 = 2 * x + 1
y2 = np.sin(x)
print(x)
print(y1)
plt.figure(num='编号')
plt.plot(x, y1, color='red', linestyle='-.')  # 颜色
plt.plot(x, y2, color='blue')
plt.show()


