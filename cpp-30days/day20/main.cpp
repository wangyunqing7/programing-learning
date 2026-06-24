#include <iostream>
#include <chrono>
#include <thread>

// 第 20 天：chrono
int main() {
    auto start = std::chrono::steady_clock::now();

    // 模拟工作：累加
    long long sum = 0;
    for (int i = 0; i < 1000000; i++) sum += i;

    auto end = std::chrono::steady_clock::now();
    auto ms = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
    std::cout << "累加 100 万次耗时：" << ms.count() << " 微秒" << std::endl;
    std::cout << "sum = " << sum << std::endl;

    // 休眠（演示）
    auto t0 = std::chrono::steady_clock::now();
    std::this_thread::sleep_for(std::chrono::milliseconds(10));
    auto t1 = std::chrono::steady_clock::now();
    std::cout << "休眠约 " << std::chrono::duration_cast<std::chrono::milliseconds>(t1-t0).count() << " 毫秒" << std::endl;
    return 0;
}