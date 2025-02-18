# 定义一个装饰器：记录函数运行时间
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)  # 执行原函数
        end_time = time.time()
        print(f"{func.__name__} 耗时: {end_time - start_time:.2f}秒")
        return result
    return wrapper

# 使用装饰器
@timer_decorator
def my_function():
    time.sleep(1)

my_function()  # 输出: my_function 耗时: 1.00秒