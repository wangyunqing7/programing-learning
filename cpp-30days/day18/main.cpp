#include <iostream>
#include <memory>
#include <vector>

// 第 18 天：智能指针
class Resource {
public:
    Resource(int id) : id_(id) { std::cout << "获取资源 " << id_ << std::endl; }
    ~Resource() { std::cout << "释放资源 " << id_ << std::endl; }
    int id() const { return id_; }
private:
    int id_;
};

int main() {
    // unique_ptr：独占，出作用域自动释放
    {
        std::unique_ptr<Resource> p = std::make_unique<Resource>(1);
        std::cout << "使用资源 " << p->id() << std::endl;
    }  // 自动释放

    // shared_ptr：共享，引用计数
    std::shared_ptr<Resource> sp1 = std::make_shared<Resource>(2);
    std::cout << "引用计数：" << sp1.use_count() << std::endl;
    {
        auto sp2 = sp1;
        std::cout << "共享后计数：" << sp1.use_count() << std::endl;
    }
    std::cout << "sp2 离开后计数：" << sp1.use_count() << std::endl;
    return 0;
}