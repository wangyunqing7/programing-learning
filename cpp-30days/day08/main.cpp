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
    std::cout << "C++ Day 08: 结构体\n";
    struct Task { std::string title; bool done; }; Task task{"learn struct", false}; std::cout << task.title << "\\n";
    return 0;
}
