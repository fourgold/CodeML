import time


class Wrapper:
    def __init__(self, name):
        self.name = name

    def __call__(self, f):
        f()


@Wrapper('张三')
def func1(sp):
    time.sleep(sp)
    print("函数结束")

