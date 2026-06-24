#include <iostream>
#include <string>

// 第 09 天：类和封装
class Account {
private:
    std::string owner;
    double balance;  // 私有：外部不能直接改

public:
    Account(std::string o, double init) : owner(o), balance(init) {}

    void deposit(double amount) {
        if (amount > 0) balance += amount;
    }

    bool withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            return true;
        }
        return false;
    }

    void show() const {
        std::cout << owner << " 余额：" << balance << std::endl;
    }
};

int main() {
    Account acc("Alice", 100);
    acc.deposit(50);
    acc.show();
    std::cout << "取 30：" << (acc.withdraw(30) ? "成功" : "失败") << std::endl;
    std::cout << "取 500：" << (acc.withdraw(500) ? "成功" : "余额不足") << std::endl;
    acc.show();
    return 0;
}