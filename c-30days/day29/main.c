#include <stdio.h>

/* 第 29 天：调试输出
 * 用宏实现可开关的日志。
 */

/* 定义 DEBUG 启用调试日志（编译时加 -DDEBUG）*/
#define DEBUG 1

/* 调试日志宏：带文件名和行号 */
#if DEBUG
    #define LOGD(fmt, ...) fprintf(stderr, "[DEBUG %s:%d] " fmt "\n", __FILE__, __LINE__, ##__VA_ARGS__)
#else
    #define LOGD(fmt, ...)  /* 发布版什么都不做 */
#endif

#define LOGI(fmt, ...) printf("[INFO] " fmt "\n", ##__VA_ARGS__)

int divide(int a, int b) {
    LOGD("调用 divide(%d, %d)", a, b);
    if (b == 0) {
        LOGD("除零，返回 0");
        return 0;
    }
    int result = a / b;
    LOGD("结果 = %d", result);
    return result;
}

int main(void) {
    LOGI("程序开始");
    LOGD("这是一条调试信息");

    printf("10 / 2 = %d\n", divide(10, 2));
    printf("10 / 0 = %d\n", divide(10, 0));

    LOGI("程序结束");
    return 0;
}