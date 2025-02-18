def repeat(n):
    """重复执行函数n次的装饰器"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
# 输出:
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!