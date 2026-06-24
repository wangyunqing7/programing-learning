#include <iostream>
#include <filesystem>
#include <vector>
#include <string>

namespace fs = std::filesystem;

// 第 21 天：filesystem
int main() {
    // 在临时目录创建演示结构
    fs::path tmp = fs::temp_directory_path() / "cpp30_demo";
    fs::create_directories(tmp / "sub");
    fs::ofstream(tmp / "a.txt") << "hello";
    fs::ofstream(tmp / "sub" / "b.txt") << "world";

    std::cout << "演示目录：" << tmp << std::endl;

    // 遍历
    int count = 0;
    for (const auto& entry : fs::recursive_directory_iterator(tmp)) {
        if (entry.is_regular_file()) {
            std::cout << "  " << entry.path().filename()
                      << " (" << entry.file_size() << " 字节)" << std::endl;
            count++;
        }
    }
    std::cout << "共 " << count << " 个文件" << std::endl;

    fs::remove_all(tmp);  // 清理
    return 0;
}