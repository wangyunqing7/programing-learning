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
    std::cout << "C++ Day 07: 函数拆分\n";
    auto square = [](int value) { return value * value; }; std::cout << square(7) << "\\n";
    return 0;
}
