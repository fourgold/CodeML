from typing import Iterable

"""非可迭代对象"""
n1 = 2
n2 = 1.23
n3 = True
n4 = 1 + 2j

"""可迭代对象"""
s = 'abcd'
l = [2, 3, 4]
t = (2, 3, 4)
dic = {'a': 1, 'b': 2}
st = {2, 3, 4}
r = range(2, 5)

"""迭代器"""
rvsd = reversed([1, 2, 3, 4])
enum = enumerate('abcd')
zp = zip('abcd', 'efdg')

print(zp)

## __iter__ 可迭代协议
