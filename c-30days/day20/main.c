#include <stdio.h>

/* 第 20 天：宏
 * 宏的定义与陷阱。
 */

#define PI 3.14159
#define MAX(a, b) ((a) > (b) ? (a) : (b))  /* 每个参数和整体都加括号 */
#define ARRAY_LEN(arr) (sizeof(arr) / sizeof((arr)[0]))

int main(void) {
    printf("PI = %f\n", PI);

    int x = 10, y = 20;
    printf("MAX(%d,%d) = %d\n", x, y, MAX(x, y));

    int arr[] = {1, 2, 3, 4, 5};
    printf("数组长度 = %zu\n", ARRAY_LEN(arr));

    /* 宏的陷阱：不加括号会出错 */
    printf("\n注意：MAX 宏已正确加括号，SQ(1+2) 类问题要用括号避免\n");
    return 0;
}