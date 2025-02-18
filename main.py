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
@timer_decorator
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(f"5! = {factorial(5)}")  # 输出: factorial 耗时: ...秒
@timer_decorator
def process_data(data):
    time.sleep(2)  # 模拟数据处理时间
    return [d * 2 for d in data]

data = [1, 2, 3, 4, 5]
processed_data = process_data(data)
print(f"Processed Data: {processed_data}")  # 输出: process_data 耗时: ...秒
@timer_decorator
def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

file_content = read_file('file.txt')
print(f"File Content: {file_content[:100]}...")  # 输出: read_file 耗时: ...秒