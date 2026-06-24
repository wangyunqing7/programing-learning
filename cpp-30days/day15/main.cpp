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
    std::cout << "C++ Day 15: lambda\n";
    std::vector<int> numbers{1,2,3,4}; std::for_each(numbers.begin(), numbers.end(), [](int n){ std::cout << n * 2 << " "; }); std::cout << "\\n";
    return 0;
}
