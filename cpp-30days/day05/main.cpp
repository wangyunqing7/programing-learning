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
    std::cout << "C++ Day 05: vector 列表\n";
    std::vector<std::string> tasks{"read", "code", "run"}; for (const auto &task : tasks) std::cout << task << "\\n";
    return 0;
}
