#include <iostream>
#include <string>

// 第 03 天：条件判断
std::string grade_of(int score) {
    if (score >= 90) return "优秀";
    else if (score >= 80) return "良好";
    else if (score >= 60) return "及格";
    else return "不及格";
}

int main() {
    int scores[] = {95, 82, 68, 45};
    for (int s : scores) {  // 范围 for 循环
        std::cout << s << " -> " << grade_of(s) << std::endl;
    }

    // 三元运算符
    int n = 10;
    std::cout << n << " 是" << (n % 2 == 0 ? "偶数" : "奇数") << std::endl;
    return 0;
}