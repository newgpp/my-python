import sys


def get_version():
    print(f"python version = {sys.version}")
    print(f"python version = {sys.version_info}")


def get_pep8_style():
    style = (
        "1. 使用 space(空格)来表示缩进, 而不要用tab(制表符)\n"
        "2. 和语法相关的每一层缩进都用4个空格来表示\n"
        "3. 每行的字符数不要超过79\n"
        "4. **对于占据多行的长表达式来说, 除了首行之外的其余各行都应该在通常的缩进"
        "级别之上再加4个空格**(使用小括号包裹的多行内容应该作4个空格的缩进)\n"
        "5. 文件中的函数与类之间应该用一个空行隔开\n"
        "6. 同一个类中，各方法之间应该用一个空行隔开\n"
        "7. **在使用下标获取列表元素、调用函数给关键字参数赋值的时候, 不要在两旁添加空格"
        "**(赋值要空格, 参数别空格, 索引紧贴写)\n"
        "8. 为变量赋值的时候, 赋值符号的左侧和右侧应该各自写上一个空格, 而且只写一个就好\n"
        "9. 函数、变量及属性应该用小写字母来拼写, 各单词之间以下划线相连\n"
        "10. 受保护的实例属性, 应该以单个下划线开头\n"
        "11. 私有的实例属性, 应该以两个下划线开头\n"
        "12. 类和异常, 应该以每个单词首字母均大写的形式来命名\n"
        "13. 模块级别的常量, 应该全部采用大写字母来拼写, 各单词之间以下划线相连\n"
        "14. 类中的实例方法(instance method), 应该把首个参数命名self, 表示该对象自身\n"
        "15. 类方法(class method)的首个参数, 应该命名cls, 以表示该类自身\n"
        "16. 采用内联形式的否定词, 不要把否定词放在前面 写 if a is not b \n"
        "而不是 if not a is b\n"
        "17. 不要通过长度检测的方法(如 if len(somelist) == 0 )来判断来判断somelist\n"
        "是否为[]或''等空值, 而是应该采用 if not somelist 这种写法来判断\n"
        "18. 不要编写单行的if语句、for循环、while循环及except复合语句\n"
        "19. import 语句应该总是放在文件开头\n"
        "20. from bar import foo 而不是 import foo\n"
        "21. import 应该按顺序分为三部分: 标准库、第三方、自用, 各import按照字母顺序排序\n"
    )
    print(style)



class User:
    count = 0  # 类变量

    def __init__(self, name):
        self.name = name
        User.count += 1

    def say_hello(self):
        print(f"Hello, my name is {self.name}")

    @classmethod
    def get_count(cls):
        return cls.count


def to_str(b_s) -> str:
    if isinstance(b_s, bytes):
        return b_s.decode("utf-8")
    else:
        return b_s


def to_bytes(b_s) -> bytes:
    if isinstance(b_s, str):
        return b_s.encode("utf-8")
    else:
        return b_s


def parse_url_qs():
    from urllib.parse import parse_qs
    url_qs = "red=5&blue=0&green="
    kv = parse_qs(url_qs, keep_blank_values=True)
    print(kv)
    # 获取red参数
    red = kv.get("red", [''])
    # [True_value] if [Condition] else [False_value]
    red = int(red[0]) if red[0] else 0
    print(red)


def check_falsy_scenarios():
    # 定义所有在 Python 中为 False 的典型对象
    falsy_values = [
        None,          # 无类型
        False,         # 布尔假
        0,             # 整数零
        0.0,           # 浮点零
        "",            # 空字符串
        [],            # 空列表
        (),            # 空元组
        {},            # 空字典
        set(),         # 空集合
        range(0)       # 空范围
    ]
    for val in falsy_values:
        # 核心逻辑：if val 为 False，则进入 else
        if val:
            result = "True (真)"
        else:
            result = "False (假)"
        print(f"{str(type(val)):<20} | {str(val):<10} | {result}")


    

if __name__ == '__main__':
    check_falsy_scenarios()