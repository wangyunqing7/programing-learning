#include <iostream>
#include <vector>
#include <numeric>

// 第 04 天：循环汇总
int main() {
    std::vector<int> nums = {12, 45, 7, 23, 56, 89, 34};

    // range-for 求和
    int sum = 0;
    for (auto n : nums) sum += n;
    std::cout << "range-for 求和 = " << sum << std::endl;

    // accumulate 算法
    int total = std::accumulate(nums.begin(), nums.end(), 0);
    std::cout << "accumulate 求和 = " << total << std::endl;
    std::cout << "平均 = " << static_cast<double>(total) / nums.size() << std::endl;

    // 找最大
    auto maxit = std::max_element(nums.begin(), nums.end());
    std::cout << "最大 = " << *maxit << std::endl;
    return 0;
}