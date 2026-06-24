#include <iostream>
#include <string>

// 第 01 天：Hello C++
// 掌握 iostream 输出和基本变量。
int main() {
    std::cout << "Hello, C++ learner!" << std::endl;

    std::string name = "Ada";
    int day = 1;
    std::cout << "欢迎 " << name << " 开始第 " << day << " 天" << std::endl;

    // cout 可以链式输出多个值
    std::cout << "C++ 比 C 多了：类、引用、STL、异常、模板" << std::endl;
    return 0;
}