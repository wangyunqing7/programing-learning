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
    std::cout << "C++ Day 09: 类和封装\n";
    class Counter { int value = 0; public: void add(){ ++value; } int get() const { return value; } }; Counter c; c.add(); std::cout << c.get() << "\\n";
    return 0;
}
