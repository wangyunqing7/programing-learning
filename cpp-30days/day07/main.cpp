#include <iostream>
#include <vector>

// 第 07 天：函数拆分
// 默认参数 + 引用传递 + 重载

// 默认参数
double power(double base, int exp = 2) {
    double result = 1;
    for (int i = 0; i < exp; i++) result *= base;
    return result;
}

// 传引用，能修改外部变量
void double_it(int& x) { x *= 2; }

// 函数重载：同名不同参数
void show(int x) { std::cout << "int: " << x << std::endl; }
void show(const std::string& s) { std::cout << "str: " << s << std::endl; }

int main() {
    std::cout << "power(3) = " << power(3) << std::endl;       // 默认平方
    std::cout << "power(2,10) = " << power(2, 10) << std::endl; // 2的10次方

    int v = 5;
    double_it(v);
    std::cout << "翻倍后 v = " << v << std::endl;

    show(42);
    show("hello");
    return 0;
}