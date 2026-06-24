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
    std::cout << "C++ Day 10: 构造函数\n";
    struct User { std::string name; explicit User(std::string n) : name(std::move(n)) {} }; User user{"Ada"}; std::cout << user.name << "\\n";
    return 0;
}
