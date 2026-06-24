#include <stdio.h>

/* 第 19 天：位运算
 * 标志位和位操作。
 */

/* 用位表示权限 */
#define PERM_READ   (1 << 0)  /* 1 */
#define PERM_WRITE  (1 << 1)  /* 2 */
#define PERM_EXEC   (1 << 2)  /* 4 */

int has_perm(int flags, int perm) {
    return (flags & perm) != 0;
}

int count_ones(unsigned int x) {
    int count = 0;
    while (x) {
        count += x & 1;
        x >>= 1;
    }
    return count;
}

int main(void) {
    int flags = PERM_READ | PERM_EXEC;  /* 读 + 执行 */
    printf("READ? %s\n",  has_perm(flags, PERM_READ)  ? "是" : "否");
    printf("WRITE? %s\n", has_perm(flags, PERM_WRITE) ? "是" : "否");
    printf("EXEC? %s\n",  has_perm(flags, PERM_EXEC)   ? "是" : "否");

    printf("\n移位：1 << 4 = %d（等于 16）\n", 1 << 4);
    printf("异或：0x55 ^ 0xFF = 0x%X\n", 0x55 ^ 0xFF);
    printf("13 的二进制有 %d 个 1\n", count_ones(13));
    return 0;
}