class P1:
    def __init__(self, a, b):  # 初始化魔术方法
        print(f"a:{a} b:{b}")

    def __call__(self, *args, **kwargs):
        print("调用")
        print(self)
        print(args)
        print(kwargs)
        pass
