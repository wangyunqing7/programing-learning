#include <iostream>
#include <string>

// 第 10 天：构造函数
class Book {
    std::string title;
    int pages;
public:
    // 初始化列表
    Book(std::string t, int p) : title(std::move(t)), pages(p) {
        std::cout << "构造：" << title << std::endl;
    }
    ~Book() {
        std::cout << "析构：" << title << std::endl;
    }
    void show() const { std::cout << "《" << title << "》" << pages << "页" << std::endl; }
};

int main() {
    Book b1("流畅的C++", 300);
    b1.show();

    {
        Book b2("临时书", 50);  // 出作用域自动析构
        b2.show();
    }  // b2 在这里析构
    std::cout << "回到 main" << std::endl;
    return 0;
}