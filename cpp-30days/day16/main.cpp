#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

// 第 16 天：algorithm
int main() {
    std::vector<int> v = {5, 2, 8, 1, 9, 3};

    auto print = [&v](const std::string& msg) {
        std::cout << msg;
        for (auto x : v) std::cout << " " << x;
        std::cout << std::endl;
    };

    print("原始：");
    std::sort(v.begin(), v.end());
    print("排序：");

    std::cout << "min=" << *std::min_element(v.begin(), v.end())
              << " max=" << *std::max_element(v.begin(), v.end()) << std::endl;
    std::cout << "sum=" << std::accumulate(v.begin(), v.end(), 0) << std::endl;

    // remove + erase 删除元素
    v.erase(std::remove(v.begin(), v.end(), 2), v.end());
    print("删除2后：");
    return 0;
}