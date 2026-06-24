#include <iostream>
#include <vector>
#include <string>

// 第 08 天：结构体
struct Student {
    std::string name;
    int score;
};

struct Point {
    double x, y;

    double distance_to(const Point& other) const {
        double dx = x - other.x, dy = y - other.y;
        return dx*dx + dy*dy;  // 距离平方，省去 sqrt
    }
};

int main() {
    // 聚合初始化
    Student s{"Ada", 95};
    std::cout << s.name << ": " << s.score << std::endl;

    Point a{3, 4}, b{0, 0};
    std::cout << "距离平方 = " << a.distance_to(b) << std::endl;

    // 结构体数组
    std::vector<Student> students = {{"Ada",95},{"Linus",78},{"Grace",55}};
    for (const auto& st : students) {
        std::cout << st.name << " " << st.score << std::endl;
    }
    return 0;
}