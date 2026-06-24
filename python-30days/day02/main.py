"""第 02 天：温度换算器

掌握：数字运算、表达式、格式化输出。
支持摄氏 C、华氏 F、开尔文 K 三者互转，能批量换算并校验输入。
运行：python main.py
"""
from __future__ import annotations

# 绝对零度，低于它就没有物理意义
ABSOLUTE_ZERO_C = -273.15


def c_to_f(celsius: float) -> float:
    return celsius * 9 / 5 + 32


def f_to_c(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9


def c_to_k(celsius: float) -> float:
    return celsius + 273.15


def k_to_c(kelvin: float) -> float:
    return kelvin - 273.15


def convert(value: float, unit: str) -> dict[str, float]:
    """把某个温度换算成另外两个单位。

    先统一归一到摄氏度，再换算出去，避免写 6 个两两组合。
    """
    unit = unit.upper()
    if unit == "C":
        c = value
    elif unit == "F":
        c = f_to_c(value)
    elif unit == "K":
        c = k_to_c(value)
    else:
        raise ValueError(f"不认识的单位：{unit}（只支持 C/F/K）")

    if c < ABSOLUTE_ZERO_C:
        raise ValueError(f"{value}{unit} 低于绝对零度，不可能存在")

    return {"C": c, "F": c_to_f(c), "K": c_to_k(c)}


def format_row(value: float, unit: str, result: dict[str, float]) -> str:
    return (f"{value:>7.2f}{unit}  ->  "
            f"{result['C']:>7.2f}°C  "
            f"{result['F']:>7.2f}°F  "
            f"{result['K']:>7.2f}K")


def main() -> None:
    samples = [(0, "C"), (100, "C"), (32, "F"), (212, "F"), (300, "K")]

    print("温度换算表")
    print("-" * 52)
    for value, unit in samples:
        try:
            print(format_row(value, unit, convert(value, unit)))
        except ValueError as e:
            print(f"{value}{unit}: {e}")

    # 边界测试：低于绝对零度
    print()
    try:
        convert(-500, "C")
    except ValueError as e:
        print(f"边界测试：{e}")


if __name__ == "__main__":
    main()
