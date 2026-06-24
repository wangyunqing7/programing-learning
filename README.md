# Programming Learning Projects

一个编程学习项目合集，包含 5 套 30 天练习课程。每一天都是一个独立、可运行的小项目，配有源码和图文教程页，适合按天学习和复习。

## 课程目录

| 课程 | 内容 | 运行方式 |
|------|------|---------|
| [`python-30days/`](python-30days/) | 30 天 Python 标准库项目 | `python main.py` |
| [`c-30days/`](c-30days/) | 30 天 C 语言控制台项目 | `gcc main.c -o a && ./a` |
| [`cpp-30days/`](cpp-30days/) | 30 天 C++ 控制台项目 | `g++ -std=c++17 main.cpp -o a && ./a` |
| [`qml-cpp-30days/`](qml-cpp-30days/) | 30 天 QML + C++ 混合开发 | CMake 构建（需 Qt 6） |
| [`web-js-css-html-30days/`](web-js-css-html-30days/) | 30 天 HTML / CSS / JS 前端 | 浏览器打开 `index.html` |

## 怎么学

每套课程都有：

- **卡片导航首页**：进入任意课程目录的 `index.html`，用浏览器打开，按周分组展示 30 天内容。
- **每天两个文件**：
  - 源码文件（`main.py` / `main.c` / `main.cpp` / `Main.qml` / `index.html` 等）—— 可直接编译运行
  - `docs.html` —— 左右分栏教程页（学习目标、知识点、易错点、课后练习 + 代码与运行结果），顶部有进度条，底部有前后导航

```powershell
# 打开某套课程的目录页
.\python-30days\index.html

# 运行某一天（以 Python 为例）
cd python-30days\day05
python main.py
```

## 课程主题概览

- **Python**：脚本基础 → 数据结构 → 函数/文件 → OOP/异常 → 标准库（csv/json/sqlite/unittest）→ 综合
- **C**：printf/变量 → 指针/结构体 → 动态内存/函数指针 → 文件/宏 → 通讯录/状态机/迷你数据库
- **C++**：iostream/vector → class/lambda → 智能指针/模板/optional → filesystem → 命令调度/综合
- **QML + C++**：QML 基础 → C++ 交互（Q_PROPERTY/信号）→ 自定义模型 → JSON → 完整任务管理 App
- **前端**：个人名片/计数器 → 表单/画廊 → 拖放/Canvas/Fetch → 动画/番茄钟/看板 → 作品集

## 本地环境

- Python 3.10+
- C/C++ 编译器（gcc / g++ / MinGW 均可，C++ 需 C++17）
- Qt 6.11（仅 QML + C++ 课程需要）
- 前端课程只需浏览器，无需任何环境

所有项目都仅使用各自语言的标准库，无需安装额外依赖。
