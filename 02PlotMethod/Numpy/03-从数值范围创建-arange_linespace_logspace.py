import numpy as np

# todo 1.arange(start,stop,dtype) 返回均匀数组
print(np.arange(3))
print(np.arange(3.0))
print(np.arange(3, 7))
print(np.arange(3, 7, 2))

# todo 2.linspace(start,stop,num=50,endPoint=True,retsep=False,dtype=None) 等差数组
# 把给定区间分成num个均匀间隔的样本，构成数组并返回
print(np.linspace(1, 100, num=50, dtype=np.int32))

# todo 3.logspace(start,stop,num=50,endPoint=True,base=10.0,dtype=None) 等比数组 ？
print('logspace')
print(np.logspace(1,100,num=4,base=2))