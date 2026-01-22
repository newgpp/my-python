import json
from typing import Any
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


class UserAccount:
    # =========================
    # 类变量（所有用户共享）
    # =========================
    total_users = 0
    MIN_AGE = 18

    def __init__(self, username: str, age: int):
        # 使用 static method 做“纯校验”
        if not self.is_valid_age(age):
            raise ValueError("年龄不合法，必须 >= 18")

        self.username = username
        self.age = age
        self.is_active = True

        # 使用 class method 修改“类级别状态”
        self._increase_user_count()

    # ==================================================
    # instance method（实例方法）
    # 👉 关注“某一个对象”的状态和行为
    # ==================================================
    def deactivate(self):
        """禁用当前用户（只影响当前实例）"""
        self.is_active = False
        print(f"用户 {self.username} 已被禁用")

    def greet(self):
        """当前用户的行为"""
        print(f"Hi, I'm {self.username}, {self.age} years old")

    # ==================================================
    # class method（类方法）
    # 👉 关注“整个类”的状态，而不是某一个对象
    # ==================================================
    @classmethod
    def _increase_user_count(cls):
        """统一管理用户总数"""
        cls.total_users += 1

    @classmethod
    def get_total_users(cls) -> int:
        """获取系统中创建过的用户数量"""
        return cls.total_users

    # ==================================================
    # static method（静态方法）
    # 👉 和类“逻辑相关”，但不依赖类 / 实例状态
    # ==================================================
    @staticmethod
    def is_valid_age(age: int) -> bool:
        """年龄是否合法（纯函数）"""
        return isinstance(age, int) and age >= UserAccount.MIN_AGE

    def to_dict(self) -> dict[str, Any]:
        return {"username": self.username, "age": self.age, "is_active": self.is_active}


def test_user_funciton() -> None:
    u1 = UserAccount("Alice", 20)
    u2 = UserAccount("Bob", 30)

    u1.greet()
    u2.deactivate()

    print(f"u1={u1.to_dict()}, u2={u2.to_dict()}")

    print(UserAccount.get_total_users())
    print(UserAccount.is_valid_age(15))


if __name__ == "__main__":
    test_user_funciton()
