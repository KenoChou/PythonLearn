from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    try:
        f = open(filename, mode)
        yield f  # yield 前的代码相当于 __enter__，之后相当于 __exit__
    finally:
        f.close()

with file_manager("file.txt", "r") as f:
    print(f.read())