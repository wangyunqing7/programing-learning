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
    std::cout << "C++ Day 17: 模板函数\n";
    auto max_value = [](auto left, auto right) { return left > right ? left : right; }; std::cout << max_value(8, 12) << "\\n";
    return 0;
}
