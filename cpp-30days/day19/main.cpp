#include <iostream>
#include <optional>
#include <vector>
#include <string>

// 第 19 天：optional
std::optional<int> find_first_even(const std::vector<int>& v) {
    for (auto n : v) {
        if (n % 2 == 0) return n;  // 找到返回值
    }
    return std::nullopt;  // 找不到返回空
}

int main() {
    std::vector<int> a = {1, 3, 5, 8, 9};
    std::vector<int> b = {1, 3, 5};

    if (auto r = find_first_even(a)) {
        std::cout << "第一个偶数：" << *r << std::endl;
    }
    auto r2 = find_first_even(b);
    std::cout << "无偶数时：" << r2.value_or(-1) << std::endl;

    // has_value 检查
    std::cout << "a 有偶数？" << (find_first_even(a).has_value() ? "是" : "否") << std::endl;
    return 0;
}