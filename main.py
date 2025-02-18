class AsyncConnection:
    async def __aenter__(self):
        print("连接建立")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("连接关闭")

async def main():
    async with AsyncConnection() as conn:
        print("使用连接中...")

import asyncio
asyncio.run(main())
# 输出:
# 连接建立
# 使用连接中...
# 连接关闭