# C 语言 30 天学习项目

每天一个控制台小程序，从 Hello C 到指针、动态内存、函数指针、状态机和综合项目。

## 怎么学

进入任意一天的目录，编译并运行：

```powershell
cd day05
gcc -std=c11 -Wall main.c -o a
./a
```

部分天数用到数学库（如 day08 的 `sqrt`），需加 `-lm`：

```powershell
gcc -std=c11 -Wall main.c -o a -lm
./a
```

也可以打开 `dayNN/docs.html` 在浏览器里看当天的讲解、代码和运行结果。从 `index.html` 进入可以看到全部 30 天的卡片导航，按周分组。

## 课程结构

| 周 | 主题 | 天数 |
|----|------|------|
| 第 1 周 | 基础（printf、变量、条件、循环、数组、字符串、函数）| day01–07 |
| 第 2 周 | 数据与内存（结构体、指针、枚举、文件、错误、动态内存、qsort）| day08–15 |
| 第 3 周 | 综合技巧（字符串分割、函数指针、递归、位运算、宏、头文件）| day16–21 |
| 第 4 周 | 综合项目（通讯录、CSV、状态机、环形缓冲、命令分发、数据库、仪表盘）| day22–30 |

每天 `docs.html` 顶部有进度条，底部有前/后导航。

## 环境要求

- 任意 C11 编译器（gcc / clang / MSVC 均可）
- 用 CMake 的话，每天目录里有 `CMakeLists.txt`，也可用 `cmake -S . -B build && cmake --build build`
