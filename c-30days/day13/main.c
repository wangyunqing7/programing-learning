#include <stdio.h>

/* 第 13 天：错误返回值
 * 用返回码 + 输出参数处理错误。
 */

/* 返回 0 成功，非 0 失败；结果通过指针输出 */
int safe_divide(int a, int b, int *result) {
    if (b == 0) return -1;      /* 除零错误 */
    if (a % b != 0) return -2;  /* 不能整除 */
    *result = a / b;
    return 0;
}

const char* err_msg(int code) {
    switch (code) {
        case 0:   return "成功";
        case -1:  return "除零错误";
        case -2:  return "不能整除";
        default:  return "未知错误";
    }
}

int main(void) {
    int cases[][2] = {{10, 2}, {10, 0}, {10, 3}};
    for (int i = 0; i < 3; i++) {
        int result, code = safe_divide(cases[i][0], cases[i][1], &result);
        if (code == 0) {
            printf("%d / %d = %d\n", cases[i][0], cases[i][1], result);
        } else {
            printf("%d / %d 失败：%s\n", cases[i][0], cases[i][1], err_msg(code));
        }
    }
    return 0;
}