class Demo:
    a = 9  # 类变量
    def func(self,a):
        print("abc")
        print(self.a)
        self.a = a
        print(self.a)

    @classmethod
    def func1(cls):
        print("func1")
        # print(a)

    @staticmethod
    def func2():
        print("abc")
        # print(a)

    def __init__(self, name):
        self.name = name


d = Demo("nn")
d.func(5)