"""第 24 天：支出统计器

掌握：数据聚合、分类汇总、报表。
按类别、按日期聚合一笔支出清单，输出月度报表。
"""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Expense:
    date: str  # YYYY-MM-DD
    category: str
    amount: float


def by_category(items: list[Expense]) -> dict[str, float]:
    agg: dict[str, float] = defaultdict(float)
    for e in items:
        agg[e.category] += e.amount
    return dict(sorted(agg.items(), key=lambda kv: -kv[1]))


def by_day(items: list[Expense]) -> dict[str, float]:
    agg: dict[str, float] = defaultdict(float)
    for e in items:
        agg[e.date] += e.amount
    return dict(sorted(agg.items()))


def report(items: list[Expense]) -> None:
    if not items:
        print("（无支出）")
        return
    total = sum(e.amount for e in items)
    print(f"总支出：{total:.2f}\n")
    print("按类别：")
    for cat, amt in by_category(items).items():
        pct = amt / total * 100
        bar = "█" * int(pct / 5)
        print(f"  {cat:<8} {amt:>8.2f}  {pct:5.1f}% {bar}")
    print("\n按日期：")
    for day, amt in by_day(items).items():
        print(f"  {day}  {amt:>8.2f}")


def main() -> None:
    items = [
        Expense("2026-06-01", "book", 72),
        Expense("2026-06-01", "food", 34),
        Expense("2026-06-02", "food", 56),
        Expense("2026-06-03", "transport", 20),
        Expense("2026-06-03", "book", 45),
    ]
    report(items)

    print()
    report([])  # 边界


if __name__ == "__main__":
    main()
