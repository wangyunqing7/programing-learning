#include <iostream>
#include <vector>
#include <string>

// 第 17 天：模板函数
template <typename T>
T my_max(T a, T b) {
    return a > b ? a : b;
}

template <typename T>
T sum(const std::vector<T>& v) {
    T total = T();
    for (const auto& x : v) total += x;
    return total;
}

int main() {
    std::cout << "max(3, 7) = " << my_max(3, 7) << std::endl;
    std::cout << "max(2.5, 1.8) = " << my_max(2.5, 1.8) << std::endl;
    std::cout << R"(max("apple","banana") = )" << my_max(std::string("apple"), std::string("banana")) << std::endl;

    std::vector<int> nums = {1, 2, 3, 4, 5};
    std::cout << "sum = " << sum(nums) << std::endl;
    return 0;
}