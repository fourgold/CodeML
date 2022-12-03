def outer(a):
    """闭包：
    在函数嵌套的前提下，内部函数使用了外部函数的变量（参数）
    外部函数的返回值是内部函数的引用
    """
    b = 999

    def inner(c):
        print(b + c)

    return inner


res = outer(2)
res(1)  # 执行过程使用了外部函数变量
print(res.__closure__[0].cell_contents)  # 查看外部函数的变量值


def outer1():
    funcs = []
    for k in range(3):
        def inner():
            return k * k

        print("闭包值：", inner.__closure__[0].cell_contents)
        funcs.append(inner)
    return funcs


# 闭包关闭时存储最后一个值 一种类型至存储一种 保存到函数中
for i in outer1():
    print(i())
