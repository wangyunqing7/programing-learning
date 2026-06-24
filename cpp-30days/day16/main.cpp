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
    std::cout << "C++ Day 16: algorithm\n";
    std::vector<int> numbers{4,1,3,2}; std::sort(numbers.begin(), numbers.end()); for (int n : numbers) std::cout << n << " "; std::cout << "\\n";
    return 0;
}
