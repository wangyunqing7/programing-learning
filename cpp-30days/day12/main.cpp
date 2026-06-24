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
    std::cout << "C++ Day 12: map 统计\n";
    std::map<std::string, int> scores{{"Ada", 95}, {"Linus", 88}}; std::cout << scores["Ada"] << "\\n";
    return 0;
}
