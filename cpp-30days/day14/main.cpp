#include <iostream>
#include <stdexcept>
#include <string>

// 第 14 天：异常处理
double safe_divide(int a, int b) {
    if (b == 0) throw std::invalid_argument("除数为0");
    if (a % b != 0) throw std::runtime_error("不能整除");
    return static_cast<double>(a) / b;
}

int main() {
    std::pair<int,int> cases[] = {{10,2},{10,0},{10,3}};
    for (auto [a, b] : cases) {
        try {
            std::cout << a << "/" << b << " = " << safe_divide(a, b) << std::endl;
        } catch (const std::exception& e) {
            std::cout << a << "/" << b << " 失败：" << e.what() << std::endl;
        }
    }
    return 0;
}