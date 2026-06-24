"""第 04 天：乘法表生成器

掌握：for 循环、嵌套循环、字符串对齐排版。
可配置范围（n×n），并对齐输出。
"""
from __future__ import annotations


def cell(a: int, b: int) -> str:
    """一个单元格：a×b=结果，右对齐到固定宽度。"""
    return f"{a}×{b}={a*b:>3}"


def table(n: int) -> list[str]:
    """生成 n×n 乘法表，每行一个字符串。"""
    if n <= 0:
        raise ValueError("范围必须为正整数")
    rows = []
    for a in range(1, n + 1):
        line = "  ".join(cell(a, b) for b in range(1, n + 1))
        rows.append(line)
    return rows


def print_table(n: int) -> None:
    for row in table(n):
        print(row)


def main() -> None:
    print("=== 9×9 乘法表 ===")
    print_table(9)

    print("\n=== 5×5 乘法表 ===")
    print_table(5)

    # 边界
    try:
        print_table(0)
    except ValueError as e:
        print(f"边界测试：{e}")


if __name__ == "__main__":
    main()
