#include <stdio.h>
#include <string.h>

/* 第 16 天：字符串分割
 * 用 strtok 切分 CSV 风格的字符串。
 */
int main(void) {
    char input[] = "Ada,95,Linus,78,Grace,88";
    char copy[100];
    strcpy(copy, input);  /* strtok 会修改，先备份 */

    printf("原始：%s\n", input);

    /* 用逗号分割 */
    printf("分割结果：");
    char *token = strtok(copy, ",");
    while (token != NULL) {
        printf(" [%s]", token);
        token = strtok(NULL, ",");  /* 后续传 NULL */
    }
    printf("\n");

    /* 解析 "key:value" 对 */
    char data[] = "name:Ada;age:20;city:Beijing";
    printf("\n键值对解析：\n");
    char *pair = strtok(data, ";");
    while (pair != NULL) {
        char *colon = strchr(pair, ':');
        if (colon) {
            *colon = '\0';
            printf("  %s = %s\n", pair, colon + 1);
        }
        pair = strtok(NULL, ";");
    }
    return 0;
}