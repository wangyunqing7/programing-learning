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
    std::cout << "C++ Day 20: chrono\n";
    auto now = std::chrono::system_clock::now(); std::cout << (now.time_since_epoch().count() > 0) << "\\n";
    return 0;
}
