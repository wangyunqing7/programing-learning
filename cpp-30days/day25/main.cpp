#include <algorithm>
#include <chrono>
#include <filesystem>
#include <functional>
#include <iostream>
#include <map>
#include <memory>
#include <numeric>
#include <optional>
#include <random>
#include <sstream>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

int main() {
    std::cout << "C++ Day 25: 搜索算法\n";
    std::vector<std::string> names{"Ada","Linus"}; auto it = std::find(names.begin(), names.end(), "Ada"); std::cout << (it != names.end()) << "\\n";
    return 0;
}
