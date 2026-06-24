# 30 天学习 QML + C++

按 Qt 6.11、CMake、MinGW、Ninja 环境编写。前 15 天是独立练习（QML 基础 → C++ 交互 → 模型 → JSON），后 15 天持续完善一个任务/笔记管理 App。

## 怎么学

用浏览器打开讲义目录：

```powershell
.\qml-cpp-30days\index.html
```

进入任意一天可以看到左右分栏教程页（左侧学习目标/概念/常见错误/练习，右侧项目文件/运行方式/代码拆解），顶部有进度条，底部有前后导航。

## 课程结构

| 阶段 | 天数 | 主题 |
|------|------|------|
| 第 1 周 | day01–05 | QML 基础（窗口、属性、组件、Controls、动画）|
| 第 2 周 | day06–10 | C++ 与 QML 交互（Q_INVOKABLE、Q_PROPERTY、信号、传参）|
| 第 3 周 | day11–15 | 模型与 JSON（QStringListModel、QAbstractListModel、JSON 保存）|
| 第 4-5 周 | day16–30 | 完整 App（界面框架、增删改查、筛选、持久化、导入导出、部署）|

## 构建运行某一天

例如第 1 天：进入当天目录，用 CMake 构建后运行。

```powershell
cd qml-cpp-30days\day01

# 把 Qt 加入 PATH（每次新开终端都要做一次）
$env:Path = "C:\Qt\6.11.1\mingw_64\bin;C:\Qt\Tools\mingw1310_64\bin;C:\Qt\Tools\Ninja;" + $env:Path

# 配置并构建
cmake -S . -B build -G Ninja -DCMAKE_PREFIX_PATH=C:/Qt/6.11.1/mingw_64 -DCMAKE_MAKE_PROGRAM=C:/Qt/Tools/Ninja/ninja.exe -DCMAKE_CXX_COMPILER=C:/Qt/Tools/mingw1310_64/bin/g++.exe
cmake --build build

# 运行
& build\appDay01.exe
```

每天的可执行文件名按天递增（`appDay01.exe` … `appDay30.exe`）。

## 常见问题

- **找不到 Qt**：确认 CMake 命令带了 `-DCMAKE_PREFIX_PATH=C:/Qt/6.11.1/mingw_64`。
- **运行时缺少 DLL**：把 `C:\Qt\6.11.1\mingw_64\bin` 加入当前 PowerShell 的 `PATH`。
- **改了 C++ 头文件但界面没变**：重新构建。`Q_OBJECT` 类需要 moc 重新生成元对象代码。
- **改了 QML 模块名/URI**：要同时改 CMakeLists（`qt_add_qml_module` 的 URI）、main.cpp（`loadFromModule`）和 QML 内的 import。
