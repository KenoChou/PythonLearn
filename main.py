def add_method(cls):
    def new_method(self):
        print("动态添加的方法")
    cls.new_method = new_method
    return cls

@add_method
class MyClass:
    pass

obj = MyClass()
obj.new_method()  # 输出: 动态添加的方法