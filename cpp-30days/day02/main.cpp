#include <iostream>

// 第 02 天：数字计算
// 掌握 auto 和 const。
int main() {
    constexpr double PI = 3.14159265;
    auto radius = 5.0;            // auto 推断为 double
    auto area = PI * radius * radius;

    std::cout << "半径 " << radius << " 的圆面积 = " << area << std::endl;

    // 整数 vs 浮点
    auto a = 7, b = 2;
    std::cout << "7/2 = " << a / b << " (整数截断)" << std::endl;
    std::cout << "7.0/2 = " << 7.0 / b << std::endl;
    std::cout << "7%2 = " << a % b << std::endl;
    return 0;
}