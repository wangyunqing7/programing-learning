#include <stdio.h>

/* 第 07 天：函数
 * 把功能拆成函数，演示值传递。
 */

/* 函数原型声明 */
int add(int a, int b);
int factorial(int n);

int main(void) {
    printf("add(3, 4) = %d\n", add(3, 4));
    printf("factorial(5) = %d\n", factorial(5));

    /* 值传递：传进去的是副本 */
    int x = 10;
    int dummy = add(x, 0);  /* x 不会被修改 */
    printf("x 调用后还是 %d\n", x);
    return 0;
}

int add(int a, int b) {
    return a + b;
}

int factorial(int n) {
    int result = 1;
    for (int i = 2; i <= n; i++) result *= i;
    return result;
}