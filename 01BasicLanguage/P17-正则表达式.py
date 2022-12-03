import re


class Student:
    @staticmethod  # 静态方法 装饰器
    def eat():
        print('我要开动了~')

    @classmethod  # 类方法 装饰器
    def sleep(cls):  # cls表示当前调用的类对象
        print('我要就寝了~')


s = Student
s.eat()
s.sleep()