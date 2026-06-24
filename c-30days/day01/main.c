#include <stdio.h>

/* 第 01 天：Hello C
 * 掌握 main 入口和 printf 输出。
 * 编译：gcc main.c -o hello && ./hello
 */
int main(void) {
    printf("Hello, C learner\n");
    printf("今天开始 30 天 C 语言之旅\n");

    /* printf 可以一次输出多个值 */
    int day = 1;
    printf("现在是第 %d 天\n", day);

    /* 返回 0 表示程序正常结束 */
    return 0;
}