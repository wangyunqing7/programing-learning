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
    std::cout << "C++ Day 28: 配置解析\n";
    std::map<std::string, std::string> config{{"theme","light"}}; std::cout << config.at("theme") << "\\n";
    return 0;
}
