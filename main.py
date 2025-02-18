# 自定义一个元类：强制类属性名大写
class UpperAttrMetaclass(type):
    def __new__(cls, name, bases, attrs):
        # 遍历属性，将非特殊属性名转为大写
        uppercase_attrs = {
            attr.upper() if not attr.startswith("__") else attr: value
            for attr, value in attrs.items()
        }
        return super().__new__(cls, name, bases, uppercase_attrs)

# 使用元类
class MyClass(metaclass=UpperAttrMetaclass):
    value = 10

print(MyClass.VALUE)  # 输出: 10（属性名被自动转为大写）