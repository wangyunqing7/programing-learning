#include <stdio.h>

/* 第 30 天：学习仪表盘
 * 综合复盘 30 天 C 语言学习。
 */
typedef struct {
    int day;
    const char *title;
    const char *skill;
} Topic;

typedef struct {
    const char *week;
    Topic *topics;
    int count;
} Week;

Topic week1[] = {
    {1,"Hello C","printf/main"}, {2,"变量计算","运算符"},
    {3,"条件判断","if/else"}, {4,"循环求和","for/while"},
    {5,"数组统计","数组遍历"}, {6,"字符串","string.h"},
    {7,"函数","参数返回"},
};
Topic week2[] = {
    {8,"结构体","struct"}, {9,"指针","地址解引用"},
    {10,"数组指针","arr与ptr"}, {11,"枚举","enum"},
    {12,"文件写入","fopen"}, {13,"错误返回值","错误码"},
    {14,"动态内存","malloc/free"}, {15,"qsort","比较函数"},
};
Topic week3[] = {
    {16,"字符串分割","strtok"}, {17,"函数指针","回调"},
    {18,"递归","基线递推"}, {19,"位运算","位标志"},
    {20,"宏","#define"}, {21,"头文件","声明分离"},
};
Topic week4[] = {
    {22,"通讯录","结构数组"}, {23,"成绩统计","聚合"},
    {24,"CSV解析","文件+解析"}, {25,"状态机","switch"},
    {26,"环形缓冲","取模循环"}, {27,"命令分发","函数指针表"},
    {28,"迷你数据库","持久化"}, {29,"调试输出","条件编译"},
    {30,"仪表盘","综合"},
};

int main(void) {
    Week weeks[] = {
        {"第 1 周 · 基础", week1, 7},
        {"第 2 周 · 数据与内存", week2, 8},
        {"第 3 周 · 综合技巧", week3, 6},
        {"第 4 周 · 综合项目", week4, 9},
    };

    int total = 0;
    printf("=== C 语言 30 天学习仪表盘 ===\n\n");
    for (int w = 0; w < 4; w++) {
        printf("【%s】（%d 天）\n", weeks[w].week, weeks[w].count);
        for (int i = 0; i < weeks[w].count; i++) {
            Topic *t = &weeks[w].topics[i];
            printf("  Day %2d  %-12s %s\n", t->day, t->title, t->skill);
        }
        printf("\n");
        total += weeks[w].count;
    }
    printf("累计：%d 天，恭喜完成 C 语言 30 天之旅！\n", total);
    return 0;
}