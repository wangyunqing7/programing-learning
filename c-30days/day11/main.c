#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_VALUE 100

typedef struct { char title[64]; int done; } Task;
typedef enum { LEVEL_BEGINNER, LEVEL_INTERMEDIATE } Level;
typedef struct { char name[32]; char email[64]; } Contact;
typedef enum { STATE_START, STATE_RUNNING, STATE_DONE } State;
typedef struct { int data[4]; int head; int tail; } Ring;
typedef struct { int id; char name[32]; } Record;
typedef void (*Handler)(void);
typedef struct { const char *name; Handler handler; } Command;

int square(int value) { return value * value; }
int safe_divide(int left, int right) { return right == 0 ? 0 : left / right; }
int compare_ints(const void *left, const void *right) {
    int a = *(const int *)left;
    int b = *(const int *)right;
    return (a > b) - (a < b);
}
int factorial(int value) { return value <= 1 ? 1 : value * factorial(value - 1); }
void print_banner(const char *text) { printf("== %s ==\n", text); }
double average(const int *values, int count) {
    int total = 0;
    for (int i = 0; i < count; ++i) total += values[i];
    return count == 0 ? 0.0 : (double)total / count;
}
State next_state(State state) { return state == STATE_START ? STATE_RUNNING : STATE_DONE; }
void ring_push(Ring *ring, int value) { ring->data[ring->tail % 4] = value; ring->tail++; }
int ring_pop(Ring *ring) { int value = ring->data[ring->head % 4]; ring->head++; return value; }
void say_hello(void) { printf("hello command\n"); }
void say_bye(void) { printf("bye command\n"); }
void debug_log(const char *message) { printf("[debug] %s\n", message); }
int sum_array(const int *values, int count) { int total = 0; for (int i = 0; i < count; ++i) total += values[i]; return total; }

int main(void) {
    printf("C Day 11: 枚举\n");
    Level level = LEVEL_BEGINNER; printf("%d\\n", level == LEVEL_BEGINNER);
    return 0;
}
