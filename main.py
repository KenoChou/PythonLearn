x = 10  # 全局变量
def func():
    x = 20  # 局部变量
    print(x) # 输出20

func()
print(x)     # 输出10