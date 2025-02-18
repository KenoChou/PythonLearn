def count_up_to(max):
    count = 1
    while count <= max:
        yield count  # 每次调用next()时返回当前count并暂停
        count += 1

counter = count_up_to(3)
print(next(counter))  # 1
print(next(counter))  # 2
print(next(counter))  # 3