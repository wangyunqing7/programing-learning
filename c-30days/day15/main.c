#include <stdio.h>
#include <stdlib.h>

/* 第 15 天：qsort
 * 用标准库排序，学会写比较函数。
 */

/* 整数升序比较 */
int cmp_int(const void *a, const void *b) {
    int x = *(const int *)a;
    int y = *(const int *)b;
    return (x > y) - (x < y);  /* 避免溢出 */
}

int main(void) {
    int arr[] = {42, 7, 19, 88, 3, 56, 21};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("排序前：");
    for (int i = 0; i < n; i++) printf(" %d", arr[i]);
    printf("\n");

    qsort(arr, n, sizeof(int), cmp_int);

    printf("排序后：");
    for (int i = 0; i < n; i++) printf(" %d", arr[i]);
    printf("\n");
    return 0;
}