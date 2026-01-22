import os
from pathlib import Path


def read_text():
    """获取当前文件所在目录上一级下的README.md文件全量读取"""
    cuttent_path = Path(__file__).resolve()
    print(f"当前文件目录:{cuttent_path}")
    base_path = cuttent_path.parent.parent
    file_path = base_path / "README.md"

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
        print(f"f type {type(f)}")
        print(f"text type {type(text)}")
        print(text)


def read_text_line():
    current_path = Path(__file__).resolve()
    base_path = current_path.parent.parent
    file_path = base_path / "README.md"

    with open(file_path, "r", encoding="utf-8") as f:
        for l in f:
            print(l.strip())


def read_text_line_with_index():
    current_path = Path(__file__).resolve()
    base_path = current_path.parent.parent
    file_path = base_path / "README.md"

    with open(file_path, "r", encoding="utf-8") as f:
        for index, l in enumerate(f, start=1):
            print(f"{index}: {l}")


def read_text_except():
    cp = Path(__file__).resolve()
    bp = cp.parent.parent
    fp = bp / "README1.md"

    try:
        with open(fp, "r", encoding="utf-8") as f:
            for l in f:
                print(l)
    except FileNotFoundError:
        print("文件未找到")
    except Exception as e:
        print(f"发生错误: {e}")


def read_text_line_while():
    cp = Path(__file__).resolve()
    bp = cp.parent.parent
    fp = bp / "README.md"
    with open(fp, "r", encoding="utf-8") as f:
        while True:
            line = f.readline()
            if not line:
                break
            print(line.strip())


if __name__ == "__main__":
    read_text_line_with_index()
