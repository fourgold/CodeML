from matplotlib import pyplot as plt
import numpy as np

plt.figure()
# plt.plot(x, y)
plt.yticks(ticks=[-1, -0.8, -0.5, -0.1, 1], labels=['a','b', 'c', 'd', 'e'])
ax = plt.gca()
ax.spines['right'].set_color('None')
ax.spines['top'].set_color('None')
ax.spines['left'].set_color('red')
ax.spines['bottom'].set_color('green')
# 选择坐标体系的左边框, 设置位置到数据为0的地方(即x轴原点) ax.spines['left'].set_position(('data', 0))
# 选择坐标体系的底边框, 设置位置到数据为-0.1的地方(即y轴的'd'点) ax.spines['bottom'].set_position(('data', -0.1)) plt.show()