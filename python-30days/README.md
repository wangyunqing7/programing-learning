# Python 30 天学习项目

每天一个标准库迷你项目，从脚本入门到 SQLite、单元测试与综合复盘。

## 怎么学

进入任意一天的目录，直接运行：

```powershell
cd day05
python main.py
```

也可以打开 `dayNN/docs.html` 在浏览器里看当天的讲解、代码和运行结果。从 `index.html` 进入可以看到全部 30 天的卡片导航，按周分组。

## 课程结构

| 周 | 主题 | 天数 |
|----|------|------|
| 第 1 周 | 脚本与数据基础（print、循环、list、dict） | day01–07 |
| 第 2 周 | 函数、字符串与文件（random、pathlib、json、异常、class） | day08–14 |
| 第 3 周 | 推导、标准库与 CLI（推导式、csv、datetime、argparse、logging） | day15–21 |
| 第 4 周 | 进阶与综合（递归、sqlite3、unittest、包结构、综合） | day22–30 |

每天 `docs.html` 顶部有进度条，底部有前/后一天的导航。

## 每天的项目长什么样

每个 day 目录里：

- `main.py` —— 当天的迷你项目，可直接运行，带类型注解、边界处理和中文注释。
- `docs.html` —— 左右分栏教程页：左边是学习目标、知识点、易错点、课后练习，右边是代码和运行结果。

day29（迷你包结构）例外，它是一个真正的多模块包，含 `__init__.py`、`stringkit.py`、`mathkit.py` 和 `main.py`。

## 环境要求

- Python 3.10 及以上（部分代码用到了 `float | None`、`dict[str, int]` 等现代语法）
- 仅使用标准库，无需安装第三方包
- `docs.html` 的代码高亮通过 CDN 加载 highlight.js，首次打开需要联网
