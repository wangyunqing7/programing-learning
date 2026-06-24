#include <iostream>

// 第 11 天：枚举
enum class Color { Red, Green, Blue };
enum class Status { Pending = 0, Active = 1, Done = 2 };

std::string status_name(Status s) {
    switch (s) {
        case Status::Pending: return "待处理";
        case Status::Active:  return "进行中";
        case Status::Done:    return "已完成";
    }
    return "?";
}

int main() {
    Color c = Color::Green;
    Status s = Status::Active;

    // enum class 不会隐式转 int
    std::cout << "状态：" << status_name(s) << std::endl;
    std::cout << "颜色编号：" << static_cast<int>(c) << std::endl;

    // 安全比较
    if (s == Status::Active) {
        std::cout << "任务正在进行" << std::endl;
    }
    return 0;
}