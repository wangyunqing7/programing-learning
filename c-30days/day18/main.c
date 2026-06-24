#include <stdio.h>

/* 第 18 天：递归
 * 阶乘、斐波那契、汉诺塔。
 */

int factorial(int n) {
    if (n <= 1) return 1;       /* 基线 */
    return n * factorial(n - 1); /* 递推 */
}

int fib(int n) {
    if (n < 2) return n;
    return fib(n - 1) + fib(n - 2);
}

/* 汉诺塔：把 n 个盘从 from 经 by 移到 to */
void hanoi(int n, char from, char by, char to) {
    if (n == 0) return;
    hanoi(n - 1, from, to, by);
    printf("  %c -> %c\n", from, to);
    hanoi(n - 1, by, from, to);
}

int main(void) {
    printf("5! = %d\n", factorial(5));
    printf("斐波那契前 10 项：");
    for (int i = 0; i < 10; i++) printf(" %d", fib(i));
    printf("\n\n汉诺塔 3 盘步骤：\n");
    hanoi(3, 'A', 'B', 'C');
    return 0;
}