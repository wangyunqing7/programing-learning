#include <iostream>
#include <random>
#include <string>

// 第 22 天：random
int random_int(int lo, int hi) {
    static std::mt19937 gen(std::random_device{}());
    std::uniform_int_distribution<int> dist(lo, hi);
    return dist(gen);
}

int main() {
    std::cout << "随机整数：";
    for (int i = 0; i < 5; i++) std::cout << " " << random_int(1, 100);
    std::cout << std::endl;

    // 生成随机密码
    const std::string chars = "abcdefghijklmnopqrstuvwxyz0123456789";
    std::string pwd;
    for (int i = 0; i < 8; i++) {
        pwd += chars[random_int(0, chars.size() - 1)];
    }
    std::cout << "随机密码：" << pwd << std::endl;

    // 模拟掷骰子 10000 次的分布
    int counts[6] = {};
    for (int i = 0; i < 10000; i++) counts[random_int(1,6)-1]++;
    std::cout << "骰子分布：";
    for (int c : counts) std::cout << " " << c;
    std::cout << std::endl;
    return 0;
}