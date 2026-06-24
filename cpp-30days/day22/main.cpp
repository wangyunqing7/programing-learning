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
    std::cout << "C++ Day 22: random\n";
    std::mt19937 rng(30); std::uniform_int_distribution<int> dist(1, 6); std::cout << dist(rng) << "\\n";
    return 0;
}
