import numpy as np

# todo 1.基本运算 算术和比较操作ndarrays被定义逐个元素操作
a = np.array([[1, 2], [3, 4], [5, 6]])
print(a + 2)

b = np.array([[1, 2], [3, 4], [5, 6]])

print(a + b)
print(a * b)
print(a < b)

# todo 2.广播 基本运算也是广播 让两个shape不同的数组变成相同shape的数组进行 ？
# a、如果数组的秩不同，将秩较小的数组进行扩展，直到两个数组的尺寸长度都一样。
# b、如果两个数组在某个维度上的长度是相同的，或者其中一个数组在该维度上的长度为1，那么我们就说这两个数组在该维度上是相容的。
# c、如果两个数组在所有维度上都是相容的，它们就能使用广播。
# d、广播之后，两个数组的尺寸将和较大的数组尺寸一样。
# e、在任何一个维度上，如果一个数组的长度为1，另一个数组长度大于1，那么在该维度上，就好像是对第一个数组进行了复制。
# 复制
# 0 1 2 3 + 0 1 2 3 = 0 1 2 3 + 0 1 2 3
# 4Functions 5 6 7             4Functions 5 6 7   0 1 2 3
print('\n广播')
a = np.arange(12).reshape((1, 3, 4))
print('a 待广播\n', a)
b = np.arange(4).reshape((1, 4))
print('a+b', a + b)
print('b 普通\n', b)
b = np.expand_dims(b, axis=0)
print('b 升维度\n', b, 'b的形状', b.shape) # 先升维度
b = np.repeat(b, 3, axis=1)
print('b 拓展维度\n', b, 'b的形状', b.shape) # 再复制
print('a+b', a + b)
print('all')
print('b change', np.repeat(np.expand_dims(np.arange(4).reshape((1, 4)), axis=0), 3, axis=1))

# todo 3.索引与切片 数组切片不会复制内部数据 只会生成原始数据的新视图 数组支持多维数组 多维度索引
print('\n索引切片')
arr = np.arange(2, 10)
print(arr)
item = arr[1]
part = arr[-2:1:-1]  # 开始 结束 步长
print('part', part)
print(arr)
arr[1] = 33
arr[3:] = [55, 55, 66, 77, 99]  # 可以对一部分进行操作
print('arr:', arr)
print('part', part)

x = np.array([[1, 2], [3, 4], [5, 6]])
print(x.shape)
print('x', x)
print('np array切片')
# print(x[0]) # 返回单个
# print(x[[1, 2]])  # 制定多重索引 返回数组

print(x[[0, 1, 2], [0, 1, 0]])  # 花式取数 operands 等价于x[0, 0]、x[1, 1]和 x[2, 0]组成的数组


