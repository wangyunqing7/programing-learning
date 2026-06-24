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
    std::cout << "C++ Day 23: sstream\n";
    std::istringstream input{"Ada 95"}; std::string name; int score; input >> name >> score; std::cout << name << ":" << score << "\\n";
    return 0;
}
