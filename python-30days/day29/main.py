"""第 29 天：迷你包结构

掌握：多模块包、__init__.py、相对导入、__all__。
演示如何把功能拆成子模块并统一导出。

注意：直接运行本文件时，Python 不会把当前目录当成包，
所以这里用「直接 import 同级模块」的方式调用，
而 __init__.py 里的相对导入（from .stringkit import ...）
需要把 day29 当成包导入时才生效（例如 python -m day29.main）。
"""
from __future__ import annotations

import stringkit
import mathkit


def main() -> None:
    print("字符串工具：")
    print(f"  slug('Hello World') = {stringkit.slug('Hello World')!r}")
    print(f"  truncate('Python 30 天', 8) = {stringkit.truncate('Python 30 天', 8)!r}")

    print("\n数学工具：")
    print(f"  safe_divmod(17, 5) = {mathkit.safe_divmod(17, 5)}")
    print(f"  clamp(15, 0, 10) = {mathkit.clamp(15, 0, 10)}")

    # 边界
    print()
    try:
        mathkit.safe_divmod(1, 0)
    except ZeroDivisionError as e:
        print(f"边界测试：{e}")


if __name__ == "__main__":
    main()
