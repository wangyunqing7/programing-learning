#include <iostream>
#include <map>
#include <string>
#include <functional>
#include <sstream>

// 第 29 天：命令调度
class Shell {
    std::map<std::string, std::function<void(const std::string&)>> cmds_;
public:
    void register_cmd(const std::string& name, std::function<void(const std::string&)> fn) {
        cmds_[name] = std::move(fn);
    }
    void run(const std::string& line) {
        std::istringstream iss(line);
        std::string cmd, arg;
        iss >> cmd;
        std::getline(iss, arg);
        if (!arg.empty() && arg[0] == ' ') arg = arg.substr(1);

        auto it = cmds_.find(cmd);
        if (it != cmds_.end()) it->second(arg);
        else std::cout << "未知命令：" << cmd << std::endl;
    }
};

int main() {
    Shell sh;
    sh.register_cmd("greet", [](const std::string& a){ std::cout << "你好，" << a << "！" << std::endl; });
    sh.register_cmd("calc", [](const std::string& a){
        std::istringstream iss(a); int x, y; char op;
        if (iss >> x >> op >> y) std::cout << x << op << y << "=" << (x+y) << std::endl;
    });
    sh.register_cmd("quit", [](const std::string&){ std::cout << "再见" << std::endl; });

    sh.run("greet Ada");
    sh.run("calc 3 + 5");
    sh.run("bogus");
    sh.run("quit");
    return 0;
}