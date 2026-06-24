"""第 13 天：银行账户类

掌握：class、对象状态、交易历史、封装。
一个有存取、透支保护、交易记录的账户。
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Account:
    owner: str
    balance: float = 0.0
    overdraft_limit: float = 0.0  # 允许透支额度
    history: list[str] = field(default_factory=list)

    def _log(self, msg: str) -> None:
        self.history.append(f"[{datetime.now():%H:%M:%S}] {msg}")

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("存款必须为正数")
        self.balance += amount
        self._log(f"存入 {amount:.2f}，余额 {self.balance:.2f}")

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("取款必须为正数")
        if self.balance - amount < -self.overdraft_limit:
            raise ValueError(f"超出透支额度：余额 {self.balance:.2f}，取 {amount:.2f}")
        self.balance -= amount
        self._log(f"取出 {amount:.2f}，余额 {self.balance:.2f}")

    def transfer(self, other: "Account", amount: float) -> None:
        self.withdraw(amount)
        other.deposit(amount)
        self._log(f"转给 {other.owner} {amount:.2f}")


def main() -> None:
    alice = Account("Alice", balance=500)
    bob = Account("Bob", balance=100, overdraft_limit=50)

    alice.deposit(200)
    alice.transfer(bob, 300)
    bob.withdraw(400)

    for acc in (alice, bob):
        print(f"{acc.owner} 余额：{acc.balance:.2f}")
        for line in acc.history:
            print("   ", line)
        print()

    # 边界：透支超额
    try:
        bob.withdraw(1000)
    except ValueError as e:
        print(f"边界测试：{e}")


if __name__ == "__main__":
    main()
