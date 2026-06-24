#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/* 第 24 天：CSV 解析
 * 读取 CSV 文件并解析成结构体。
 */

/* 去掉行尾的换行符 */
void trim_newline(char *s) {
    size_t len = strlen(s);
    while (len > 0 && (s[len-1] == '\n' || s[len-1] == '\r')) {
        s[--len] = '\0';
    }
}

int main(void) {
    /* 先写一个 CSV 文件 */
    const char *path = "grades.csv";
    FILE *out = fopen(path, "w");
    fprintf(out, "Ada,95,88\nLinus,78,65\nGrace,55,72\n");
    fclose(out);

    /* 再读回来解析 */
    FILE *in = fopen(path, "r");
    if (!in) { printf("打开失败\n"); return 1; }

    char line[100];
    printf("%-10s %6s %6s %6s\n", "姓名", "数学", "英语", "合计");
    printf("------------------------------\n");

    while (fgets(line, sizeof(line), in)) {
        trim_newline(line);
        char *name = strtok(line, ",");
        char *m = strtok(NULL, ",");
        char *e = strtok(NULL, ",");
        if (name && m && e) {
            int math = atoi(m), eng = atoi(e);
            printf("%-10s %6d %6d %6d\n", name, math, eng, math + eng);
        }
    }
    fclose(in);
    remove(path);
    return 0;
}