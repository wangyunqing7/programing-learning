#include <iostream>
#include <vector>
#include <algorithm>

// 第 15 天：lambda
int main() {
    std::vector<int> nums = {42, 7, 19, 88, 3, 56};

    // lambda 排序（降序）
    std::sort(nums.begin(), nums.end(), [](int a, int b) { return a > b; });
    std::cout << "降序：";
    for (auto n : nums) std::cout << n << " ";
    std::cout << std::endl;

    // count_if 统计满足条件的
    int threshold = 40;
    int cnt = std::count_if(nums.begin(), nums.end(),
                            [threshold](int n) { return n > threshold; });
    std::cout << "大于 " << threshold << " 的个数：" << cnt << std::endl;

    // find_if 找第一个
    auto it = std::find_if(nums.begin(), nums.end(), [](int n){ return n < 10; });
    if (it != nums.end()) std::cout << "第一个小于10的：" << *it << std::endl;
    return 0;
}