try:
    num = int(input("输入数字："))
except ValueError:
    print("输入无效！")
else:
    print(f"输入的数字是：{num}")
finally:
    print("处理结束。")