#include <stdio.h>

/* 第 04 天：循环求和
 * 计算 1+2+...+n，演示 for 和 while。
 */
int main(void) {
    int n = 100;

    /* for 循环求和 */
    int sum = 0;
    for (int i = 1; i <= n; i++) {
        sum += i;
    }
    printf("for: 1 到 %d 的和 = %d\n", n, sum);

    /* while 循环求和 */
    int i = 1, sum2 = 0;
    while (i <= n) {
        sum2 += i;
        i++;
    }
    printf("while: 1 到 %d 的和 = %d\n", n, sum2);

    /* break 提前退出 */
    for (int k = 1; k <= 10; k++) {
        if (k * k > 30) {
            printf("第一个平方超过 30 的是 %d\n", k);
            break;
        }
    }
    return 0;
}