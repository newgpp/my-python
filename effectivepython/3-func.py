from typing import Union

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
        ("KeyError", lambda: {"name":"Alice"}["age"]),
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




if __name__ == "__main__":
    exception_showcase()