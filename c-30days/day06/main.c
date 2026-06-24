#include <stdio.h>
#include <string.h>

/* 第 06 天：字符串长度
 * 掌握 C 字符串的基本操作。
 */
int main(void) {
    char greet[] = "Hello, C";
    printf("字符串：\"%s\"\n", greet);
    printf("strlen 长度：%zu\n", strlen(greet));      /* 不含 \0 */
    printf("sizeof 占用：%zu\n", sizeof(greet));      /* 含 \0 */

    /* strcpy 复制，strcat 拼接 */
    char buf[50];
    strcpy(buf, greet);
    strcat(buf, " learner");
    printf("拼接后：%s\n", buf);

    /* strcmp 比较 */
    printf("比较 \"abc\" 和 \"abd\"：%d\n", strcmp("abc", "abd")); /* 负数 */
    printf("比较 \"abc\" 和 \"abc\"：%d\n", strcmp("abc", "abc")); /* 0 表示相等 */
    return 0;
}