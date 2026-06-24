# C++ 30 天学习项目

每天一个控制台小程序，从 Hello C++ 到 STL、lambda、智能指针、模板和综合项目。

## 怎么学

进入任意一天的目录，编译并运行（需要 C++17）：

```powershell
cd day05
g++ -std=c++17 -Wall main.cpp -o a
./a
```

也可以打开 `dayNN/docs.html` 在浏览器里看当天的讲解、代码和运行结果。从 `index.html` 进入可以看到全部 30 天的卡片导航，按周分组。

## 课程结构

| 周 | 主题 | 天数 |
|----|------|------|
| 第 1 周 | 基础（iostream、auto、条件、循环、vector、string、函数）| day01–07 |
| 第 2 周 | OOP 与 STL（struct、class、构造、enum、map、文件、异常、lambda、algorithm、模板、智能指针、optional、chrono、filesystem）| day08–21 |
| 第 3-4 周 | 综合应用（random、sstream、递归、搜索、统计、任务模型、配置、命令调度、仪表盘）| day22–30 |

每天 `docs.html` 顶部有进度条，底部有前/后导航。

## 环境要求

- C++17 及以上的编译器（g++ / clang++ / MSVC 均可）
- 部分天数（filesystem）需要链接，g++ 9+ 已默认支持
- 用 CMake 的话，每天目录里有 `CMakeLists.txt`
