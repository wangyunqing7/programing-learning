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
    std::cout << "C++ Day 30: 学习仪表盘\n";
    std::vector<int> progress{10, 8, 9, 7}; std::cout << "finished=" << std::accumulate(progress.begin(), progress.end(), 0) << "\\n";
    return 0;
}
