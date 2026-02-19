import asyncio

async def call_api(name, duration):
    await asyncio.sleep(duration)
    return f"{name} 的数据"

async def main():
    async with asyncio.TaskGroup() as tg:
        # 1. 创建并追踪任务对象
        task1 = tg.create_task(call_api("A", 1))
        task2 = tg.create_task(call_api("B", 2))
    
    # 2. 退出上下文后，任务保证已完成，直接取值
    print(f"结果: {task1.result()}, {task2.result()}")

asyncio.run(main())

