#include <iostream>
#include <sstream>
#include <string>

// 第 23 天：sstream
int main() {
    // ostringstream：拼接字符串
    std::ostringstream oss;
    oss << "学生：" << "Ada" << " 分数：" << 95;
    std::string result = oss.str();
    std::cout << result << std::endl;

    // istringstream：解析字符串
    std::string data = "Ada 95 88";
    std::istringstream iss(data);
    std::string name;
    int math, english;
    iss >> name >> math >> english;
    std::cout << name << " 总分 " << math + english << std::endl;

    // 字符串转数字
    std::istringstream num("42");
    int n;
    num >> n;
    std::cout << "解析的数字：" << n << std::endl;
    return 0;
}