def list_unpacking():
    """*other 这种写法被称为扩展解包（Extended Iterable Unpacking），它能将列表中剩余的所有元素自动捕获并打包成一个新的列表"""
    lst = list(range(10))
    r_lst = sorted(lst, reverse=True)
    max_value, second_max_value, *other = r_lst
    print(f"最大值:{max_value}, 倒数第二大值:{second_max_value}")


def print_student(name, age, score):
    print(f"name={name}, age={age}, score={score}")


def dict_unpacking():
    """使用 ** 操作符将字典内的键值对“平铺展开”，通常用于在 {} 中合并多个字典或在函数调用中将字典转换为关键字参数传入"""
    d = {"name": "Alice", "age": 20, "score": 88}
    print_student(**d)
    d1 = {**d, "id": 123}
    print(d1)


def sort_students():
    """利用元组（Tuple）“从左往右依次比较”的特性，将复杂的业务优先级直接映射为元组中元素的顺序"""
    students = [
        {"name": "Alice", "age": 20, "score": 88},
        {"name": "Bob", "age": 19, "score": 95},
        {"name": "Charlie", "age": 20, "score": 95},
        {"name": "David", "age": 18, "score": 95},
        {"name": "Eve", "age": 20, "score": 88},
    ]
    # lambda表达式语法 lambda 参数: 表达式
    sorted_students = sorted(students, key=lambda s: (-s["score"], s["age"], s["name"]))
    for s in sorted_students:
        print(s)


def dict_has_order():
    """自 Python 3.7 起，dict 正式保证会永久保留键值对插入的原始顺序。"""
    d = {"name": "Alice", "age": 20, "score": 88}
    for k, v in d.items():
        print(k, v)


def dict_get_or():
    """dict.get(key, default) 用于安全地根据键取值"""
    d = {"name": "Alice", "age": 20, "score": 88}
    sex = d.get("sex", "male")
    print(sex)


if __name__ == "__main__":
    dict_get_or()
