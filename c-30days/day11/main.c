#include <stdio.h>

/* 第 11 天：枚举
 * 用 enum 表示状态，提高可读性。
 */
typedef enum {
    STATE_OK = 0,
    STATE_WARNING = 1,
    STATE_ERROR = 2
} Status;

const char* status_name(Status s) {
    switch (s) {
        case STATE_OK:      return "正常";
        case STATE_WARNING: return "警告";
        case STATE_ERROR:   return "错误";
        default:            return "未知";
    }
}

Status check(int value) {
    if (value < 0)        return STATE_ERROR;
    else if (value > 100) return STATE_WARNING;
    else                  return STATE_OK;
}

int main(void) {
    int tests[] = {50, 120, -5};
    for (int i = 0; i < 3; i++) {
        Status s = check(tests[i]);
        printf("值 %3d -> 状态 %d (%s)\n", tests[i], s, status_name(s));
    }
    return 0;
}