#include <iostream>
#include <vector>
#include <algorithm>

// 第 25 天：搜索算法
int main() {
    std::vector<int> v = {1, 3, 5, 7, 9, 11, 13};

    // 线性查找
    auto it = std::find(v.begin(), v.end(), 9);
    std::cout << "find 9：" << (it != v.end() ? "找到" : "无") << std::endl;

    // 二分查找（有序数组）
    bool exists = std::binary_search(v.begin(), v.end(), 7);
    std::cout << "binary_search 7：" << (exists ? "存在" : "不存在") << std::endl;

    // lower_bound：第一个 >= target 的位置
    auto lb = std::lower_bound(v.begin(), v.end(), 8);
    std::cout << "第一个 >= 8 的是：" << *lb << "（下标 " << lb - v.begin() << "）" << std::endl;

    // find_if 按条件
    auto first_big = std::find_if(v.begin(), v.end(), [](int x){ return x > 10; });
    std::cout << "第一个 >10 的：" << *first_big << std::endl;
    return 0;
}