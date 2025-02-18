class LoggingDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"调用函数: {self.func.__name__}")
        return self.func(*args, **kwargs)

@LoggingDecorator
def say_hello():
    print("Hello!")

say_hello()  # 输出: 调用函数: say_hello → Hello!
@LoggingDecorator
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(f"5! = {factorial(5)}")  # 输出: 调用函数: factorial → 5! = 1