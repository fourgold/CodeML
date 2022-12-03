# 手写列表 迭代器
class MyList:
    def __init__(self, iterable):
        *self.iterable, = iterable
        self.index = 0

    def __str__(self):
        return f'{self.iterable}'

    def __iter__(self):
        return self

    def __next__(self):
        try:
            res = self.iterable[self.index]
            self.index += 1
            return res
        except IndexError:
            print("循环结束")
            raise StopIteration


tup = (1, 2, 3, 4)
r = MyList(tup)
for i in r:
    print(i)

# / 不可以传位置参数
