#include <stdio.h>

/* 第 26 天：环形缓冲区
 * 定长环形队列，入队覆盖最旧数据。
 */
#define RING_SIZE 4

typedef struct {
    int data[RING_SIZE];
    int head;   /* 下一个写入位置 */
    int count;  /* 当前元素数 */
} Ring;

void ring_init(Ring *r) { r->head = 0; r->count = 0; }

void ring_push(Ring *r, int value) {
    r->data[r->head] = value;
    r->head = (r->head + 1) % RING_SIZE;
    if (r->count < RING_SIZE) r->count++;
}

void ring_print(Ring *r) {
    printf("[");
    /* 从最旧到最新输出 */
    int start = (r->count < RING_SIZE) ? 0 : r->head;
    for (int i = 0; i < r->count; i++) {
        int idx = (start + i) % RING_SIZE;
        printf(" %d", r->data[idx]);
    }
    printf(" ] (count=%d)\n", r->count);
}

int main(void) {
    Ring r;
    ring_init(&r);

    for (int i = 1; i <= 6; i++) {
        ring_push(&r, i);
        printf("push %d: ", i);
        ring_print(&r);
    }
    return 0;
}