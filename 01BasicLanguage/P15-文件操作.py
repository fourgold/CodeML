# 从文件的编码方式来看 文件可以氛围文本文件和二进制文件
from typing import Iterable,Iterator
file = open("/file。xml", mode='r', encoding='UTF-8')
print(file.name)
a = file.readline()
b = file.readline()
print(a)
print(b)
print(file.readline())

