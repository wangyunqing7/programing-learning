#include <stdio.h>

/* 第 25 天：状态机
 * 一个迷你文字冒险的状态机。
 */
typedef enum { S_START, S_FOREST, S_TREASURE, S_END } State;

const char* state_name(State s) {
    switch (s) {
        case S_START:    return "起点";
        case S_FOREST:   return "森林";
        case S_TREASURE: return "宝箱";
        case S_END:      return "结束";
    }
    return "?";
}

/* 模拟玩家的一系列输入 */
int main(void) {
    State state = S_START;
    char inputs[] = {'g', 'g', 't'};  /* g=go, t=take */
    int idx = 0, total = 3;

    while (state != S_END && idx < total) {
        char input = inputs[idx++];
        printf("[%s] 输入 %c -> ", state_name(state), input);

        switch (state) {
            case S_START:
                if (input == 'g') state = S_FOREST;
                break;
            case S_FOREST:
                if (input == 'g') state = S_TREASURE;
                break;
            case S_TREASURE:
                if (input == 't') { printf("拿到宝物！"); state = S_END; }
                break;
            default: break;
        }
        printf(" 现在 [%s]\n", state_name(state));
    }
    printf("冒险结束\n");
    return 0;
}