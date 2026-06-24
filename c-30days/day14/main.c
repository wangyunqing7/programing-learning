#include <stdio.h>
#include <stdlib.h>

/* 第 14 天：动态内存
 * 用 malloc 创建运行时才知大小的数组。
 */
int main(void) {
    int n = 5;

    /* 动态分配 n 个 int */
    int *arr = malloc(n * sizeof(int));
    if (arr == NULL) {
        printf("内存分配失败\n");
        return 1;
    }

    /* 赋值 */
    for (int i = 0; i < n; i++) {
        arr[i] = (i + 1) * (i + 1);  /* 平方数 */
    }
    printf("初始数组：");
    for (int i = 0; i < n; i++) printf(" %d", arr[i]);
    printf("\n");

    /* 扩容到 8 */
    int *bigger = realloc(arr, 8 * sizeof(int));
    if (bigger == NULL) {
        free(arr);
        return 1;
    }
    arr = bigger;
    for (int i = n; i < 8; i++) arr[i] = (i + 1) * (i + 1);
    printf("扩容后：");
    for (int i = 0; i < 8; i++) printf(" %d", arr[i]);
    printf("\n");

    /* 必须释放 */
    free(arr);
    printf("内存已释放\n");
    return 0;
}