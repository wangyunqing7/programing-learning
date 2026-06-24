#include <iostream>
#include <string>

// 第 06 天：字符串处理
int main() {
    std::string s = "Hello, C++ learner";

    std::cout << "长度：" << s.length() << std::endl;
    std::cout << "子串(0,5)：" << s.substr(0, 5) << std::endl;

    // find 查找
    auto pos = s.find("C++");
    if (pos != std::string::npos) {
        std::cout << "找到 C++ 在位置 " << pos << std::endl;
    }

    // 拼接和替换
    s += "!";
    s.replace(7, 3, "modern C++");
    std::cout << "处理后：" << s << std::endl;

    // 数字与字符串互转
    int n = 42;
    std::string num_str = std::to_string(n);
    int parsed = std::stoi("123abc");  // 解析到非数字为止
    std::cout << num_str << " / " << parsed << std::endl;
    return 0;
}