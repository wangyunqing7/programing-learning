"""第 12 天：安全除法

掌握：try/except、异常分类、自定义异常。
做一个能区分「除零」「类型错」「负数开方」的安全运算器。
"""
from __future__ import annotations


class InvalidInputError(ValueError):
    """业务层面的非法输入。"""


def safe_divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError(f"除数不能为 0：{a}/{b}")
    return a / b


def safe_sqrt(x: float) -> float:
    if x < 0:
        raise InvalidInputError(f"不能对负数开方：{x}")
    return x ** 0.5


def safe_eval(expr: str) -> float:
    """解析 'a op b' 形式，统一捕获各类异常。"""
    parts = expr.split()
    if len(parts) != 3:
        raise InvalidInputError(f"格式应为 'a op b'：{expr}")
    try:
        a, op, b = float(parts[0]), parts[1], float(parts[2])
    except ValueError:
        raise InvalidInputError(f"操作数不是数字：{expr}")
    if op == "/":
        return safe_divide(a, b)
    elif op == "sqrt":
        return safe_sqrt(a)
    else:
        raise InvalidInputError(f"不支持的运算：{op}")


def run(exprs: list[str]) -> None:
    for e in exprs:
        try:
            print(f"  {e} = {safe_eval(e):.4f}")
        except ZeroDivisionError as ex:
            print(f"  {e} -> [除零] {ex}")
        except InvalidInputError as ex:
            print(f"  {e} -> [输入错] {ex}")


def main() -> None:
    print("正常运算：")
    run(["10 / 2", "100 / 8", "9 sqrt 0"])

    print("\n异常运算：")
    run(["10 / 0", "abc / 2", "-16 sqrt 0", "10 % 3"])


if __name__ == "__main__":
    main()
