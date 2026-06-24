#include <iostream>
#include <vector>
#include <string>

// 第 05 天：vector 列表
int main() {
    std::vector<std::string> todos;

    todos.push_back("学习 vector");
    todos.push_back("写一个 TODO");
    todos.push_back("复习 STL");

    std::cout << "共 " << todos.size() << " 项任务：" << std::endl;
    for (size_t i = 0; i < todos.size(); i++) {
        std::cout << "  " << i + 1 << ". " << todos[i] << std::endl;
    }

    // at 会边界检查
    std::cout << "第1项：" << todos.at(0) << std::endl;

    todos.pop_back();  // 删除最后一个
    std::cout << "删除后剩 " << todos.size() << " 项" << std::endl;
    return 0;
}