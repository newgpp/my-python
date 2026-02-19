from __future__ import annotations

from functools import wraps
from typing import Any, Callable, Iterable


# 1) 默认参数、可变参数、仅限位置参数(/)、仅限关键字参数(*)
def greet(name: str, title: str = "同学") -> str:
    return f"你好，{title}{name}"


def sum_all(*nums: int) -> int:
    return sum(nums)


def build_profile(name: str, /, age: int, *, city: str = "北京") -> dict[str, Any]:
    # / 之前为“仅限位置参数”；* 之后为“仅限关键字参数”
    return {"name": name, "age": age, "city": city}


# 2) 参数解包/收集
def area(width: int, height: int) -> int:
    return width * height


def demo_unpacking():
    dims = (3, 4)
    print("area:", area(*dims))
    kwargs = {"name": "Alex", "age": 20, "city": "上海"}
    print("profile:", build_profile("Alex", age=20, city="上海"))
    print("profile2:", build_profile(**kwargs))


# 3) 装饰器：无参、带参、保持函数元信息
def timing(fn: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(fn)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        import time

        start = time.time()
        try:
            return fn(*args, **kwargs)
        finally:
            cost = (time.time() - start) * 1000
            print(f"{fn.__name__} 耗时 {cost:.2f}ms")

    return wrapper


def repeat(n: int) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(fn: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(fn)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            result = None
            for _ in range(n):
                result = fn(*args, **kwargs)
            return result

        return wrapper

    return decorator


@timing
@repeat(3)
def say_hi(name: str) -> str:
    msg = f"Hi, {name}"
    print(msg)
    return msg


# 4) 闭包与 nonlocal
def make_counter(start: int = 0) -> Callable[[], int]:
    count = start

    def inc() -> int:
        nonlocal count
        count += 1
        return count

    return inc


# 5) 属性装饰器：@property
class Temperature:
    def __init__(self, celsius: float) -> None:
        self._c = celsius

    @property
    def celsius(self) -> float:
        return self._c

    @celsius.setter
    def celsius(self, value: float) -> None:
        if value < -273.15:
            raise ValueError("低于绝对零度")
        self._c = value

    @property
    def fahrenheit(self) -> float:
        return self._c * 9 / 5 + 32


# 6) 生成器函数 + 生成器表达式
def fib(n: int) -> Iterable[int]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def gen_demo():
    print("fib:", list(fib(6)))
    squares = (x * x for x in range(5))
    print("squares:", list(squares))


# 7) 仅演示：函数注解
def add(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    print(greet("小明"))
    print("sum_all:", sum_all(1, 2, 3))
    print("build_profile:", build_profile("小明", age=18, city="深圳"))
    demo_unpacking()
    say_hi("Ken")
    counter = make_counter(10)
    print("counter:", counter(), counter(), counter())
    t = Temperature(25)
    print("temp:", t.celsius, t.fahrenheit)
    gen_demo()
    print("add:", add(2, 3))
