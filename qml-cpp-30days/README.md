# 30 天学习 QML + C++

这是为本机 Qt 6.11.1 + MinGW 环境生成的 30 天教程。

## 打开讲义

用浏览器打开：

```powershell
.\qml-cpp-30days\index.html
```

## 构建某一天

例如第 1 天：

```powershell
cd qml-cpp-30days\day01
.\run.ps1
```

如果只想构建不运行：

```powershell
cmake -S . -B build -G Ninja -DCMAKE_PREFIX_PATH=C:/Qt/6.11.1/mingw_64 -DCMAKE_MAKE_PROGRAM=C:/Qt/Tools/Ninja/ninja.exe -DCMAKE_CXX_COMPILER=C:/Qt/Tools/mingw1310_64/bin/g++.exe
cmake --build build
```

## 学习顺序

- day01-day15：QML 基础、C++ 对象、属性、信号、模型、JSON。
- day16-day30：逐步完成任务/笔记管理 App。

## 常见问题

如果直接运行 exe 提示缺少 Qt DLL，请先在当前 PowerShell 加入 Qt 路径：

```powershell
$env:Path = "C:\Qt\6.11.1\mingw_64\bin;C:\Qt\Tools\mingw1310_64\bin;" + $env:Path
```
