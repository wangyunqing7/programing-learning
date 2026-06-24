#include <iostream>
#include <fstream>
#include <sstream>
#include <map>
#include <string>

// 第 28 天：配置解析
std::map<std::string, std::string> parse_config(const std::string& content) {
    std::map<std::string, std::string> cfg;
    std::istringstream iss(content);
    std::string line;
    while (std::getline(iss, line)) {
        auto eq = line.find('=');
        if (eq != std::string::npos) {
            std::string key = line.substr(0, eq);
            std::string val = line.substr(eq + 1);
            cfg[key] = val;
        }
    }
    return cfg;
}

int main() {
    std::string config = R"(name=MyApp
version=1.0
debug=true
port=8080)";

    auto cfg = parse_config(config);
    for (const auto& [k, v] : cfg) {
        std::cout << k << " = " << v << std::endl;
    }

    // 取值并转换
    int port = std::stoi(cfg["port"]);
    bool debug = (cfg["debug"] == "true");
    std::cout << "\n应用 " << cfg["name"] << " v" << cfg["version"]
              << " 端口 " << port << " 调试 " << (debug?"开":"关") << std::endl;
    return 0;
}