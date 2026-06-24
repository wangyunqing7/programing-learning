#include <stdio.h>

/* 第 21 天：头文件思维
 * 演示声明与定义分离（这里用内联演示，真实项目拆 .h/.c）。
 */

/* ---- 相当于 mathutil.h 的内容 ---- */
#ifndef MATHUTIL_H
#define MATHUTIL_H
int max_int(int a, int b);   /* 声明 */
int min_int(int a, int b);
#endif
/* ---- 头文件结束 ---- */

/* ---- 相当于 mathutil.c 的定义 ---- */
int max_int(int a, int b) { return a > b ? a : b; }
int min_int(int a, int b) { return a < b ? a : b; }

int main(void) {
    printf("max(3,7) = %d\n", max_int(3, 7));
    printf("min(3,7) = %d\n", min_int(3, 7));

    /* 头文件的价值：别的 .c 文件只要 #include 就能用这些函数，
       无需知道实现细节。大型项目靠这个组织代码。 */
    printf("\n头文件让多个源文件共享声明，是 C 项目组织的基础。\n");
    return 0;
}