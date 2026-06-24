#include <iostream>
#include <map>
#include <vector>
#include <string>

// 第 12 天：map 统计
int main() {
    std::vector<std::string> words = {"apple","banana","apple","cherry","banana","apple"};

    // 统计词频
    std::map<std::string, int> freq;
    for (const auto& w : words) {
        freq[w]++;  // 不存在则创建为0再+1
    }

    std::cout << "词频统计：" << std::endl;
    for (const auto& [word, count] : freq) {  // 结构化绑定 (C++17)
        std::cout << "  " << word << " : " << count << std::endl;
    }

    // 安全查询
    auto it = freq.find("grape");
    std::cout << "grape 存在？" << (it != freq.end() ? "是" : "否") << std::endl;
    return 0;
}