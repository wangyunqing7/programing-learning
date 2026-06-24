#include <stdio.h>

/* 第 05 天：数组统计
 * 计算数组的和、平均、最大、最小。
 */
int main(void) {
    int nums[] = {12, 45, 7, 23, 56, 89, 34};
    int n = sizeof(nums) / sizeof(nums[0]);

    int sum = 0, max = nums[0], min = nums[0];
    for (int i = 0; i < n; i++) {
        sum += nums[i];
        if (nums[i] > max) max = nums[i];
        if (nums[i] < min) min = nums[i];
    }

    printf("数组：");
    for (int i = 0; i < n; i++) printf(" %d", nums[i]);
    printf("\n");
    printf("元素个数：%d\n", n);
    printf("总和：%d  平均：%.2f\n", sum, (double)sum / n);
    printf("最大：%d  最小：%d\n", max, min);
    return 0;
}