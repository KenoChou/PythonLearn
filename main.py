class Animal:
    # 构造方法
    def __init__(self, name):
        self.name = name
    
    def bark(self,call):
        print(f"{self.name}：{call}！")
    def skill(self):
        print(f"{self.name}：我会吃饭！")

my_dog = Animal("旺财")
my_dog.bark("汪汪")  # 输出：旺财：汪汪！
class Cat(Animal):  # 继承Dog类
    def bark(self,call):
        print(f"{self.name}：{call}")

my_cat = Cat("小白")
my_cat.bark("喵喵")  # 输出：小白：喵喵！
my_cat.skill()  # 输出：小白：我会吃饭！
