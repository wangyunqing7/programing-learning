#include <stdio.h>
#include <string.h>

/* 第 27 天：命令分发
 * 用函数指针表实现命令行调度。
 */

void cmd_hello(const char *arg) { printf("你好，%s！\n", arg); }
void cmd_add(const char *arg) {
    /* arg 形如 "3 5" */
    int a, b;
    if (sscanf(arg, "%d %d", &a, &b) == 2)
        printf("%d + %d = %d\n", a, b, a + b);
    else
        printf("用法：add 数字 数字\n");
}
void cmd_quit(const char *arg) { printf("再见\n"); }

typedef struct {
    const char *name;
    void (*handler)(const char *);
} Command;

Command commands[] = {
    {"hello", cmd_hello},
    {"add",   cmd_add},
    {"quit",  cmd_quit},
};

void dispatch(const char *line) {
    char cmd[32], arg[64] = "";
    sscanf(line, "%31s %63[^
]", cmd, arg);

    for (int i = 0; i < 3; i++) {
        if (strcmp(cmd, commands[i].name) == 0) {
            commands[i].handler(arg);
            return;
        }
    }
    printf("未知命令：%s\n", cmd);
}

int main(void) {
    dispatch("hello Ada");
    dispatch("add 3 5");
    dispatch("add 10");
    dispatch("bogus");
    dispatch("quit");
    return 0;
}