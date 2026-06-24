#include <iostream>
#include <vector>
#include <string>
#include <numeric>

// 第 30 天：学习仪表盘
struct Topic { int day; std::string title; std::string skill; };

struct Week { std::string name; std::vector<Topic> topics; };

int main() {
    std::vector<Week> weeks = {
        {"第 1 周 · 基础", {
            {1,"Hello C++","iostream"},{2,"数字计算","auto/const"},
            {3,"条件判断","if/else"},{4,"循环汇总","range-for"},
            {5,"vector","动态数组"},{6,"字符串","std::string"},{7,"函数","重载/默认参数"}
        }},
        {"第 2 周 · OOP与STL", {
            {8,"结构体","struct"},{9,"类和封装","class"},{10,"构造函数","初始化列表"},
            {11,"枚举","enum class"},{12,"map统计","std::map"},{13,"文件","fstream"},
            {14,"异常","try/catch"},{15,"lambda","匿名函数"},{16,"algorithm","STL算法"},
            {17,"模板","template"},{18,"智能指针","unique/shared"},{19,"optional","可选值"},
            {20,"chrono","计时"},{21,"filesystem","文件系统"}
        }},
        {"第 3-4 周 · 综合应用", {
            {22,"random","现代随机"},{23,"sstream","字符串流"},{24,"递归","分治"},
            {25,"搜索算法","二分查找"},{26,"费用统计","聚合"},{27,"任务模型","命令分发"},
            {28,"配置解析","key=value"},{29,"命令调度","function"},{30,"仪表盘","综合"}
        }}
    };

    int total = 0;
    std::cout << "=== C++ 30 天学习仪表盘 ===" << std::endl << std::endl;
    for (const auto& w : weeks) {
        std::cout << "【" << w.name << "】（" << w.topics.size() << " 天）" << std::endl;
        for (const auto& t : w.topics) {
            std::cout << "  Day " << t.day << "  " << t.title << " (" << t.skill << ")" << std::endl;
        }
        std::cout << std::endl;
        total += w.topics.size();
    }
    std::cout << "累计 " << total << " 天，恭喜完成 C++ 30 天之旅！" << std::endl;
    return 0;
}