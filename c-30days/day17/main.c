#include <stdio.h>

/* 第 17 天：函数指针
 * 把运算函数当参数传，实现策略模式。
 */

/* 定义函数指针类型 */
typedef int (*BinOp)(int, int);

int op_add(int a, int b) { return a + b; }
int op_sub(int a, int b) { return a - b; }
int op_mul(int a, int b) { return a * b; }

/* 用传入的函数做运算 */
int compute(int a, int b, BinOp op) {
    return op(a, b);
}

/* 对数组每个元素应用函数 */
void map(int *arr, int n, int (*f)(int)) {
    for (int i = 0; i < n; i++) arr[i] = f(arr[i]);
}

int square(int x) { return x * x; }

int main(void) {
    printf("compute(10,3, add) = %d\n", compute(10, 3, op_add));
    printf("compute(10,3, sub) = %d\n", compute(10, 3, op_sub));
    printf("compute(10,3, mul) = %d\n", compute(10, 3, op_mul));

    int arr[] = {1, 2, 3, 4};
    map(arr, 4, square);
    printf("平方后：");
    for (int i = 0; i < 4; i++) printf(" %d", arr[i]);
    printf("\n");
    return 0;
}