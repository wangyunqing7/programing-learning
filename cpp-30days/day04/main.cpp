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
    std::cout << "C++ Day 04: 循环汇总\n";
    int total = 0; for (int i = 1; i <= 10; ++i) total += i; std::cout << total << "\\n";
    return 0;
}
