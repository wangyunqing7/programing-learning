#include <stdio.h>

/* 第 10 天：数组和指针
 * 理解 arr[i] 和 *(arr+i) 的等价性。
 */

/* 用指针遍历数组 */
int sum_with_pointer(const int *begin, const int *end) {
    int total = 0;
    for (const int *p = begin; p != end; p++) {
        total += *p;
    }
    return total;
}

int main(void) {
    int arr[] = {10, 20, 30, 40, 50};
    int n = sizeof(arr) / sizeof(arr[0]);

    /* 下标访问 vs 指针访问 */
    printf("下标 arr[2] = %d\n", arr[2]);
    printf("指针 *(arr+2) = %d\n", *(arr + 2));  /* 等价 */

    /* 指针遍历求和 */
    int total = sum_with_pointer(arr, arr + n);
    printf("指针遍历求和 = %d\n", total);

    /* 指针算术 */
    int *p = arr;
    printf("p 指向 %d，p+1 指向 %d\n", *p, *(p + 1));
    return 0;
}