def match_value():
    status_code = 200
    match status_code:
        case 200 | 201 | 204:
            print("SUCCESS")
        case 404:
            print("Not Found")
        case _:
            pirnt("DEFAULT")


def get_status_value(status_code: int) -> str:
    match status_code:
        case 200 | 201 | 204:
            return "SUCCESS"
        case 404:
            return "Not Found"
        case _:
            return "DEFAULT"


def get_age_name(age: int) -> str:
    match age:
        case n if n < 18:
            return "未成年"
        case n if n >= 18:
            return "成年人"


def get_type(x: str | int) -> str:
    match x:
        case int():
            return "int"
        case str():
            return "str"


if __name__ == "__main__":
    v = get_type("19")
    print(v)
