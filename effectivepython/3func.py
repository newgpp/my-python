import asyncio
from datetime import datetime
import random
from typing import Union, Generator


def divide(a: float, b: float) -> float:
    """
    进行除法计算。

    :param a: 被除数
    :param b: 除数
    :return: 计算结果
    :raises ValueError: 当 b 为 0 时抛出
    """
    if b == 0:
        raise ValueError("b 不能为0")
    return a / b


def call_devide():
    try:
        r = divide(2.1, 0)
    except ValueError as e:
        print(f"参数错误: {e}")
    except Exception as e:
        print(f"非预期错误: {e}")
    else:
        # 只有成功拿到r才执行这里
        print(f"计算结果为: {r}")
    finally:
        # 无论如何都会清理，例如关闭进度条
        print("计算任务尝试完成")


def divide_safe(a: float, b: float) -> Union[float, ValueError]:
    """很多大型 Python 项目借鉴了 Rust 的思想"""
    """不再使用 raise 抛出崩溃，而是让函数返回一个包含“结果”或“错误”的对象"""
    if b == 0:
        return ValueError("b 不能为0")
    return a / b


def call_divide_safe():
    result = divide_safe(2.1, 0)
    if isinstance(result, ValueError):
        print(f"处理失败: {result}")
    else:
        print(f"处理成功: {result}")


def exception_showcase():
    cases = [
        ("ValueError", lambda: int("abc")),
        ("TypeError", lambda: "2" + 2),
        ("IndexError", lambda: [1, 2][5]),
        ("KeyError", lambda: {"name": "Alice"}["age"]),
        ("AttributeError", lambda: (10).append(5)),
        ("ZeroDivisionError", lambda: 1 / 0),
        ("FileNotFoundError", lambda: open("x.txt", "r")),
        ("NameError", lambda: undefined_variable),
    ]
    print(f"{'异常类型':<20} | {'触发代码示例':<30}")
    print("-" * 60)

    for name, func in cases:
        try:
            func()
        except Exception as e:
            error_type = type(e).__name__
            print(f"{error_type:<20} | {str(e)}")


async def fetch_api_data(name: str, delay: int) -> str:
    await asyncio.sleep(delay)
    return f"来自 {name} 的数据"


async def consume_fetch_api_data():
    # 直接调用并等待 (顺序执行) 这种方式会阻塞当前协程，直到结果返回
    print(f"开始时间 {datetime.now()}")
    data1 = await fetch_api_data("服务A", 1)
    print(f"收到: {data1}")

    # 并发调用 (推荐用于工程实践) 同时发射多个请求，极大提高效率
    results = await asyncio.gather(
        fetch_api_data("服务B", 2),
        fetch_api_data("服务C", 1)
    )
    print(f"\n收到结果列表: {results}")

    # 创建任务 (不阻塞后续代码) 创建任务后，函数会立即在后台运行，不会停下来等它
    task = asyncio.create_task(fetch_api_data("后台服务", 3))
    print("\n[后台任务已提交，我先去干别的事了...]")
    final_data = await task
    print(f"最后拿回: {final_data}")

    print(f"结束时间: {datetime.now()}")


def run_consume_fetch_api_data():
    asyncio.run(consume_fetch_api_data())


def fib_generator(limit: int) -> Generator:
    """
    生成器是一个利用 yield 关键字实现“按需取值”的函数，它在循环时才产生数据并记录运行状态，从而以极小的内存消耗处理海量甚至无限的数据流。
    """
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1


def square_generator():
    """生成器表达式（只在循环时计算，省内存）"""
    sg = (x**2 for x in range(10))
    print(type(sg))
    print(next(sg))
    print(next(sg))
    print(next(sg))
    print(next(sg))
    print(next(sg))


async def async_data_fetcher(cnt):
    """
    async 声明的函数会返回一个协程对象 (Coroutine)，它允许程序在执行耗时任务时暂时挂起并让出 CPU 控制权，从而在单线程下实现极高的并发效率。
    """
    for i in range(cnt):
        await asyncio.sleep(1)
        # 模拟产生数据包
        data = f"数据包-{i}(随机码:{random.randint(100, 999)})"
        yield data


async def async_consume():
    """
    async for 是专门用来遍历“异步生成器”的循环，它在每一轮迭代取值时都会自动执行隐式的 await，从而在等待下一条数据产出的过程中不阻塞程序运行。
    """
    print("--开始异步抓取数据--")

    async for i in async_data_fetcher(5):
        print(f"处理完成: {i}")
    
    print("--所有数据处理完毕--")


def run_data_fetcher_consume():
    """
    asyncio.run() 是连接同步与异步世界的“启动开关”，它负责创建全新的事件循环、驱动指定的协程运行至结束，并随后自动关闭循环以清理资源
    """
    asyncio.run(async_consume())


if __name__ == "__main__":
    run_consume_fetch_api_data()
