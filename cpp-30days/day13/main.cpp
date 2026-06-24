#include <iostream>
#include <fstream>
#include <string>

// 第 13 天：文件输出
int main() {
    const std::string path = "output.txt";

    // 写文件（RAII 自动关闭）
    {
        std::ofstream out(path);
        if (!out.is_open()) { std::cerr << "打开失败" << std::endl; return 1; }
        out << "姓名 数学 英语\n";
        out << "Ada 95 88\n";
        out << "Linus 78 65\n";
    }  // out 析构自动关闭

    // 读文件
    std::ifstream in(path);
    std::cout << "--- 文件内容 ---" << std::endl;
    std::string line;
    while (std::getline(in, line)) {
        std::cout << line << std::endl;
    }

    std::remove(path.c_str());
    return 0;
}