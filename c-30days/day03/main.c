#include <stdio.h>

/* 第 03 天：条件判断
 * 根据分数评定等级。
 */
const char* grade_of(int score) {
    if (score >= 90) return "优秀";
    else if (score >= 80) return "良好";
    else if (score >= 60) return "及格";
    else return "不及格";
}

int main(void) {
    int scores[] = {95, 82, 68, 45};
    int n = sizeof(scores) / sizeof(scores[0]);

    for (int i = 0; i < n; i++) {
        printf("分数 %d：%s\n", scores[i], grade_of(scores[i]));
    }
    return 0;
}