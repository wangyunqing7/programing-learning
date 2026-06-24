"""第 27 天：SQLite 记账

掌握：sqlite3、建表、参数化查询、聚合。
用内存数据库做一个账本：记收入支出、查余额、按类别汇总。
"""
from __future__ import annotations

import sqlite3
from dataclasses import dataclass


@dataclass
class Ledger:
    conn: sqlite3.Connection

    @classmethod
    def open(cls) -> "Ledger":
        conn = sqlite3.connect(":memory:")
        conn.execute("""CREATE TABLE txns (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            kind TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL
        )""")
        return cls(conn)

    def add(self, kind: str, category: str, amount: float) -> None:
        if kind not in ("income", "expense"):
            raise ValueError("kind 必须是 income/expense")
        if amount <= 0:
            raise ValueError("金额必须为正")
        # 参数化查询，防止 SQL 注入
        self.conn.execute(
            "INSERT INTO txns (kind, category, amount) VALUES (?, ?, ?)",
            (kind, category, amount),
        )

    def balance(self) -> float:
        cur = self.conn.execute(
            "SELECT SUM(CASE kind WHEN 'income' THEN amount ELSE -amount END) FROM txns"
        )
        return cur.fetchone()[0] or 0.0

    def summary_by_category(self) -> list[tuple[str, float]]:
        cur = self.conn.execute(
            "SELECT category, SUM(amount) FROM txns WHERE kind='expense' GROUP BY category ORDER BY 2 DESC"
        )
        return cur.fetchall()

    def close(self) -> None:
        self.conn.close()


def main() -> None:
    ledger = Ledger.open()
    for cat, amt in [("salary", 5000), ("bonus", 800)]:
        ledger.add("income", cat, amt)
    for cat, amt in [("food", 120), ("book", 72), ("food", 56), ("transport", 30)]:
        ledger.add("expense", cat, amt)

    print(f"当前余额：{ledger.balance():.2f}")
    print("支出分类：")
    for cat, amt in ledger.summary_by_category():
        print(f"  {cat:<10} {amt:.2f}")

    # 边界
    print()
    try:
        ledger.add("expense", "x", -5)
    except ValueError as e:
        print(f"边界测试：{e}")
    ledger.close()


if __name__ == "__main__":
    main()
