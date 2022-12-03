class Student:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    def get_name(self):
        return self.__name


stu = Student("张三", 18)

print(stu.get_name())

print(stu.name)