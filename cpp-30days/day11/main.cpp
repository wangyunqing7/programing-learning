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
    std::cout << "C++ Day 11: 枚举\n";
    enum class Level { beginner, intermediate }; Level level = Level::beginner; std::cout << (level == Level::beginner) << "\\n";
    return 0;
}
