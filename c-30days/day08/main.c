#include <stdio.h>
#include <math.h>

/* 第 08 天：结构体
 * 用 struct 把相关数据打包。
 */
typedef struct {
    double x;
    double y;
} Point;

double distance(Point a, Point b) {
    double dx = a.x - b.x;
    double dy = a.y - b.y;
    return sqrt(dx * dx + dy * dy);
}

void print_point(Point p) {
    printf("(%.1f, %.1f)", p.x, p.y);
}

int main(void) {
    Point p1 = {3.0, 4.0};
    Point p2 = {0.0, 0.0};

    printf("点1：");
    print_point(p1);
    printf("  点2：");
    print_point(p2);
    printf("\n距离：%.2f\n", distance(p1, p2));
    return 0;
}