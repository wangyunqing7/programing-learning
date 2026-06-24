#include <iostream>
#include <vector>

// 第 24 天：递归
int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

int fib(int n) {
    if (n < 2) return n;
    return fib(n-1) + fib(n-2);
}

// 递归求数组最大值
int max_of(const std::vector<int>& v, size_t i) {
    if (i == v.size() - 1) return v[i];
    int rest = max_of(v, i + 1);
    return v[i] > rest ? v[i] : rest;
}

int main() {
    std::cout << "5! = " << factorial(5) << std::endl;
    std::cout << "fib(10) = " << fib(10) << std::endl;

    std::vector<int> v = {3, 7, 2, 9, 4};
    std::cout << "最大值 = " << max_of(v, 0) << std::endl;
    return 0;
}