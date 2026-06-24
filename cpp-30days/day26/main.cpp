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
    std::cout << "C++ Day 26: 费用统计\n";
    std::vector<double> expenses{12.5, 20.0, 8.5}; double sum = std::accumulate(expenses.begin(), expenses.end(), 0.0); std::cout << sum << "\\n";
    return 0;
}
