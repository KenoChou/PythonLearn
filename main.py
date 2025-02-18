# 类似列表推导式，但返回生成器对象
squares = (x**2 for x in range(10))
print(next(squares))  # 0
print(next(squares))  # 1