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
    std::cout << "C++ Day 21: filesystem\n";
    std::filesystem::path path{"src/main.cpp"}; std::cout << path.filename().string() << "\\n";
    return 0;
}
