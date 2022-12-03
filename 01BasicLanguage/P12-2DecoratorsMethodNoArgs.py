import time


def timer(f):
    def inner(s):
        start = time.time()
        f(s)
        print(id(f))
        end = time.time()
        print("时间差", end - start)

    return inner


# 装饰设计模式 不改变原有函数 闭包 能够给没有参数的函数增加功能
@timer
def func1(s):  # 带参数
    """ 当装饰器装饰的函数被定义好时,
        会把该被装饰的函数作为参数传给装饰器调用
        返回引用，把返回值赋值给func1
    """
    time.sleep(s)
    print("func1 running")


func1(3)
