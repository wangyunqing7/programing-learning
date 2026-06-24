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
    std::cout << "C++ Day 24: 递归\n";
    std::function<int(int)> factorial = [&](int n){ return n <= 1 ? 1 : n * factorial(n - 1); }; std::cout << factorial(5) << "\\n";
    return 0;
}
