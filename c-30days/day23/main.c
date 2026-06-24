#include <stdio.h>
#include <stdlib.h>

/* 第 23 天：成绩统计
 * 多科目结构体 + 聚合统计。
 */
typedef struct {
    char name[16];
    int math, english, science;
} Student;

int total(const Student *s) {
    return s->math + s->english + s->science;
}

int cmp_total(const void *a, const void *b) {
    return total(b) - total(a);  /* 降序 */
}

int main(void) {
    Student students[] = {
        {"Ada", 95, 88, 92},
        {"Linus", 78, 65, 85},
        {"Grace", 55, 72, 48},
        {"Alan", 88, 90, 76},
    };
    int n = sizeof(students) / sizeof(students[0]);

    /* 单科统计 */
    int math_sum = 0;
    for (int i = 0; i < n; i++) math_sum += students[i].math;
    printf("数学均分：%.1f\n", (double)math_sum / n);

    /* 按总分排序 */
    qsort(students, n, sizeof(Student), cmp_total);
    printf("\n总分排名：\n");
    for (int i = 0; i < n; i++) {
        printf("  %d. %-8s 总分 %d\n", i + 1, students[i].name, total(&students[i]));
    }
    return 0;
}