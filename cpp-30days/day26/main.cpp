#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <numeric>

// 第 26 天：费用统计
struct Expense {
    std::string date;
    std::string category;
    double amount;
};

int main() {
    std::vector<Expense> items = {
        {"06-01","book",72.0},{"06-01","food",34.0},
        {"06-02","food",56.0},{"06-03","transport",20.0},
        {"06-03","book",45.0}
    };

    // 按类别聚合
    std::map<std::string, double> by_cat;
    for (const auto& e : items) by_cat[e.category] += e.amount;

    double total = std::accumulate(items.begin(), items.end(), 0.0,
        [](double s, const Expense& e){ return s + e.amount; });

    std::cout << "总支出：" << total << std::endl;
    std::cout << "按类别：" << std::endl;
    for (const auto& [cat, amt] : by_cat) {
        std::cout << "  " << cat << " : " << amt << std::endl;
    }
    return 0;
}