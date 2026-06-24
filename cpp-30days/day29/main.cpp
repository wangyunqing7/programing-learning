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
    std::cout << "C++ Day 29: 命令调度\n";
    std::map<std::string, std::function<void()>> commands; commands["hello"] = []{ std::cout << "hello command\\n"; }; commands["hello"]();
    return 0;
}
