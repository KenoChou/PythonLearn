def print_args(*args, **kwargs):
    print("位置参数:", args)
    print("关键字参数:", kwargs)

print_args(1, 2, a=3, b=4)
print_args('apple', 'banana', 'cherry', x=10, y=20, z=30)
def log_message(*args, **kwargs):
    print("日志消息:", args)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

log_message("Error", "File not found", filename="data.txt", line=42)
def query_database(table, *args, **kwargs):
    print(f"查询表: {table}")
    print("条件:", args)
    print("选项:", kwargs)

query_database("users", "age > 30", "country = 'US'", limit=10, order_by="age")
def create_html_element(tag, *content, **attributes):
    attrs = " ".join(f'{key}="{value}"' for key, value in attributes.items())
    inner_content = " ".join(content)
    print(f"<{tag} {attrs}>{inner_content}</{tag}>")

create_html_element("a", "Click here", href="https://example.com", target="_blank")
def calculate_sum(*args, **kwargs):
    total = sum(args)
    print("总和:", total)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

calculate_sum(1, 2, 3, 4, 5, operation="addition", description="Sum of numbers")
