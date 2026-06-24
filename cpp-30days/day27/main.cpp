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
    std::cout << "C++ Day 27: 小型任务模型\n";
    struct Task { std::string title; bool done; }; std::vector<Task> tasks{{"model", false}, {"view", true}}; std::cout << tasks.size() << "\\n";
    return 0;
}
