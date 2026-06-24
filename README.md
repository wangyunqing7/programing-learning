# Programming Learning Projects

这是一个编程学习项目合集，包含多套 30 天练习课程。每一天都是一个独立小项目，配有代码、说明文档和运行脚本，适合按天学习和复习。

## 课程目录

- `qml-cpp-30days/`：30 天 QML + C++ 混合开发教程
- `python-30days/`：30 天 Python 标准库和脚本练习
- `web-js-css-html-30days/`：30 天 HTML、CSS、JavaScript 前端练习
- `cpp-30days/`：30 天纯 C++ 控制台项目
- `c-30days/`：30 天 C 语言控制台项目

## 学习入口

可以直接用浏览器打开总目录：

```powershell
.\learning-projects-index.html
```

也可以进入任意课程目录打开对应的 `index.html`。

## 运行示例

每一天都有自己的 `run.ps1`。例如运行 Python 第 1 天：

```powershell
cd python-30days\day01
.\run.ps1
```

如果 PowerShell 拦截脚本，可以使用：

```powershell
powershell -ExecutionPolicy Bypass -File .\run.ps1
```

## 本地环境

这些项目按当前 Windows 本地环境整理，主要使用：

- Python 3
- Node.js
- MinGW GCC/G++
- Qt 6.11.1，用于 QML + C++ 课程

## 说明

仓库只保留学习材料和可运行项目。生成脚本、临时规划文档、构建产物和缓存文件不会提交到仓库。
