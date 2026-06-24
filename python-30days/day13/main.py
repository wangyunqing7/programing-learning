"""第 13 天：银行账户类"""

def main() -> None:
    class BankAccount:
        def __init__(self, owner: str, balance: float = 0):
            self.owner = owner
            self.balance = balance
        def deposit(self, amount: float) -> None:
            self.balance += amount

    account = BankAccount("Ada", 100)
    account.deposit(35)
    print(account.owner, account.balance)

if __name__ == "__main__":
    main()
