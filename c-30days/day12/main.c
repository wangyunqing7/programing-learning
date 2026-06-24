#include <stdio.h>

/* 第 12 天：文件写入
 * 把数据写到文件再读回来。
 */
int main(void) {
    const char *path = "output.txt";

    /* 写文件 */
    FILE *out = fopen(path, "w");
    if (out == NULL) {
        printf("无法打开 %s 写入\n", path);
        return 1;
    }
    fprintf(out, "姓名 数学 英语\n");
    fprintf(out, "Ada 95 88\n");
    fprintf(out, "Linus 78 65\n");
    fclose(out);
    printf("已写入 %s\n", path);

    /* 读文件 */
    FILE *in = fopen(path, "r");
    if (in == NULL) {
        printf("无法打开 %s 读取\n", path);
        return 1;
    }
    printf("--- 文件内容 ---\n");
    char line[100];
    while (fgets(line, sizeof(line), in) != NULL) {
        printf("%s", line);
    }
    fclose(in);

    /* 清理（实际项目可保留） */
    remove(path);
    return 0;
}