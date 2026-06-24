#include <stdio.h>

/* 第 09 天：指针基础
 * 用指针让函数修改调用方的变量。
 */

/* 通过指针修改外部变量 */
void add_ten(int *p) {
    *p += 10;  /* 解引用并修改 */
}

void swap(int *a, int *b) {
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

int main(void) {
    int x = 5;
    printf("x = %d\n", x);
    add_ten(&x);  /* 传地址 */
    printf("add_ten 后 x = %d\n", x);

    int a = 1, b = 2;
    swap(&a, &b);
    printf("swap 后 a=%d, b=%d\n", a, b);
    return 0;
}