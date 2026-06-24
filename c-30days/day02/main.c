#include <stdio.h>

/* 第 02 天：变量和计算
 * 温度换算：摄氏转华氏。
 */
int main(void) {
    double celsius = 26.0;
    double fahrenheit = celsius * 9.0 / 5.0 + 32.0;

    printf("%.1f 摄氏度 = %.1f 华氏度\n", celsius, fahrenheit);

    /* 整数除法 vs 浮点除法 */
    int a = 5, b = 2;
    printf("整数除法 5/2 = %d\n", a / b);      /* 2 */
    printf("浮点除法 5.0/2.0 = %.2f\n", 5.0 / 2.0); /* 2.50 */
    printf("取余 5 %% 2 = %d\n", a % b);        /* 1 */

    return 0;
}