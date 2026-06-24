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
    std::cout << "C++ Day 14: 异常处理\n";
    try { throw std::runtime_error("practice error"); } catch (const std::exception &error) { std::cout << error.what() << "\\n"; }
    return 0;
}
