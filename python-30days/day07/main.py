"""第 07 天：单位换算函数

掌握：函数定义、参数、返回值，以及「函数表分发」模式。
用一张 {类别: {单位: 系数}} 的换算表统一处理长度、重量等线性换算。
"""
from __future__ import annotations

# 以某个基准单位为 1.0，其它单位给出相对系数
CONVERSIONS: dict[str, dict[str, float]] = {
    "length": {"m": 1.0, "km": 1000.0, "cm": 0.01, "mile": 1609.34, "ft": 0.3048},
    "weight": {"kg": 1.0, "g": 0.001, "lb": 0.453592, "oz": 0.0283495},
}


def convert(value: float, category: str, from_unit: str, to_unit: str) -> float:
    """先换算到基准单位，再换算到目标单位。"""
    table = CONVERSIONS.get(category)
    if table is None:
        raise ValueError(f"不支持的类别：{category}")
    if from_unit not in table or to_unit not in table:
        raise ValueError(f"单位不在 {category} 里：{from_unit}/{to_unit}")
    base = value * table[from_unit]
    return base / table[to_unit]


def batch(samples: list[tuple[float, str, str, str]]) -> None:
    for value, cat, fu, tu in samples:
        try:
            result = convert(value, cat, fu, tu)
            print(f"  {value} {fu} = {result:.4f} {tu}")
        except ValueError as e:
            print(f"  {value} {fu}->{tu}: {e}")


def main() -> None:
    print("长度换算：")
    batch([(1, "length", "km", "mile"),
           (100, "length", "m", "ft"),
           (5, "length", "mile", "km")])

    print("\n重量换算：")
    batch([(1, "weight", "kg", "lb"),
           (500, "weight", "g", "kg"),
           (10, "weight", "oz", "g")])

    # 边界
    print()
    batch([(1, "length", "m", "kg")])  # 单位跨类


if __name__ == "__main__":
    main()
