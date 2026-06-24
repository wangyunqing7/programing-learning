#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <functional>

// 第 27 天：小型任务模型
struct Task { std::string title; bool done; };

int main() {
    std::vector<Task> tasks = {{"学完 day27",false},{"写练习",false}};

    // 命令分发表
    std::map<std::string, std::function<void(std::vector<Task>&,const std::string&)>> cmds;

    cmds["add"] = [](std::vector<Task>& t, const std::string& arg){
        t.push_back({arg, false});
        std::cout << "已添加：" << arg << std::endl;
    };
    cmds["list"] = [](std::vector<Task>& t, const std::string&){
        for (size_t i = 0; i < t.size(); i++)
            std::cout << "  " << i+1 << ". [" << (t[i].done?"x":" ") << "] " << t[i].title << std::endl;
    };
    cmds["done"] = [](std::vector<Task>& t, const std::string& arg){
        size_t idx = std::stoul(arg) - 1;
        if (idx < t.size()) { t[idx].done = true; std::cout << "完成：" << t[idx].title << std::endl; }
    };

    // 模拟执行
    cmds["list"](tasks, "");
    cmds["add"](tasks, "复习 STL");
    cmds["done"](tasks, "1");
    cmds["list"](tasks, "");
    return 0;
}