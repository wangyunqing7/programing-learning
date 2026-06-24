from __future__ import annotations

import html
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
PYTHON_EXE = r"C:\Users\yunqing\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
NODE_EXE = r"C:\Users\yunqing\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe"
GXX_EXE = r"C:\Qt\Tools\mingw1310_64\bin\g++.exe"
GCC_EXE = r"C:\Qt\Tools\mingw1310_64\bin\gcc.exe"


PYTHON_DAYS = [
    ("Hello CLI", "print、变量和脚本入口"),
    ("温度换算器", "数字、表达式和格式化输出"),
    ("成绩判断器", "if/elif/else 条件分支"),
    ("乘法表生成器", "for 循环和字符串拼接"),
    ("任务列表", "list 的增删查改"),
    ("联系人字典", "dict 的键值结构"),
    ("单位换算函数", "函数定义、参数和返回值"),
    ("密码建议器", "random、字符串和函数组合"),
    ("文本统计器", "字符串处理和统计"),
    ("临时笔记文件", "pathlib 和文件读写"),
    ("JSON 任务数据", "json 序列化和反序列化"),
    ("安全除法", "异常处理"),
    ("银行账户类", "class 和对象状态"),
    ("图书 dataclass", "dataclass 和对象列表"),
    ("列表推导统计", "推导式和 statistics"),
    ("CLI 菜单模拟", "函数拆分和命令分发"),
    ("CSV 成绩表", "csv 模块"),
    ("日期计划表", "datetime 模块"),
    ("路径整理器", "pathlib 路径操作"),
    ("参数解析器", "argparse 基础"),
    ("日志记录器", "logging 模块"),
    ("递归目录摘要", "递归思想"),
    ("排序和搜索", "key 函数和查找"),
    ("支出统计器", "数据聚合"),
    ("文字冒险", "状态机思维"),
    ("配置读取器", "configparser"),
    ("SQLite 记账", "sqlite3 标准库"),
    ("单元测试示例", "unittest"),
    ("迷你包结构", "模块组织"),
    ("学习仪表盘", "综合复盘"),
]


WEB_DAYS = [
    ("个人名片", "HTML 结构、CSS 基础、JS 修改文本"),
    ("计数器", "按钮事件和 DOM 更新"),
    ("主题切换", "CSS class 和状态切换"),
    ("待办卡片", "数组渲染列表"),
    ("表单校验", "输入读取和错误提示"),
    ("图片画廊", "Grid 布局和数组数据"),
    ("进度条", "CSS 宽度和 JS 状态"),
    ("计算器", "输入、数字和函数"),
    ("颜色选择器", "input color 和 CSS 变量"),
    ("标签过滤", "filter 和数据属性"),
    ("模态框", "显示/隐藏交互"),
    ("标签页", "tab 状态切换"),
    ("折叠面板", "事件委托"),
    ("本地备忘录", "localStorage 基础"),
    ("键盘快捷键", "keydown 事件"),
    ("拖放排序演示", "drag/drop 事件"),
    ("Canvas 时钟", "canvas 绘图"),
    ("Fetch 模拟数据", "Promise 和异步渲染"),
    ("响应式导航", "媒体查询和菜单"),
    ("表格排序", "数组排序和表格渲染"),
    ("搜索高亮", "字符串匹配"),
    ("CSS 动画卡片", "transition 和 animation"),
    ("小测验", "状态、分数和条件渲染"),
    ("番茄钟", "计时器"),
    ("Markdown 预览", "文本转换"),
    ("购物清单", "表单、列表、合计"),
    ("天气卡片模拟", "组件化渲染"),
    ("可访问性表单", "label、aria 和焦点"),
    ("项目看板", "多列数据渲染"),
    ("个人作品集", "综合页面"),
]


CPP_DAYS = [
    ("Hello C++", "iostream 和 main"),
    ("数字计算", "变量、表达式和格式化输出"),
    ("条件判断", "if/else"),
    ("循环汇总", "for 循环"),
    ("vector 列表", "std::vector"),
    ("字符串处理", "std::string"),
    ("函数拆分", "函数和返回值"),
    ("结构体", "struct"),
    ("类和封装", "class"),
    ("构造函数", "constructor"),
    ("枚举", "enum class"),
    ("map 统计", "std::map"),
    ("文件输出", "fstream"),
    ("异常处理", "throw/catch"),
    ("lambda", "lambda 表达式"),
    ("algorithm", "std::sort 和 count_if"),
    ("模板函数", "template"),
    ("智能指针", "std::unique_ptr"),
    ("optional", "std::optional"),
    ("chrono", "时间处理"),
    ("filesystem", "路径处理"),
    ("random", "随机数"),
    ("sstream", "字符串流"),
    ("递归", "递归函数"),
    ("搜索算法", "find_if"),
    ("费用统计", "聚合计算"),
    ("小型任务模型", "结构体数组和函数"),
    ("配置解析", "键值解析"),
    ("命令调度", "函数对象"),
    ("学习仪表盘", "综合复盘"),
]


C_DAYS = [
    ("Hello C", "printf 和 main"),
    ("变量和计算", "基础类型"),
    ("条件判断", "if/else"),
    ("循环求和", "for 循环"),
    ("数组统计", "数组"),
    ("字符串长度", "char 数组"),
    ("函数", "函数参数和返回值"),
    ("结构体", "struct"),
    ("指针基础", "指针和地址"),
    ("数组和指针", "指针遍历"),
    ("枚举", "enum"),
    ("文件写入", "FILE I/O"),
    ("错误返回值", "错误处理习惯"),
    ("动态内存", "malloc/free"),
    ("qsort", "标准库排序"),
    ("字符串分割", "strtok"),
    ("函数指针", "回调"),
    ("递归", "递归函数"),
    ("位运算", "bit flags"),
    ("宏", "宏和常量"),
    ("头文件思维", "接口拆分概念"),
    ("小型通讯录", "结构体数组"),
    ("成绩统计", "聚合计算"),
    ("CSV 解析", "简单文本解析"),
    ("状态机", "枚举驱动状态"),
    ("环形缓冲区", "数组模拟队列"),
    ("命令分发", "函数表"),
    ("迷你数据库", "结构化记录"),
    ("调试输出", "断言和日志"),
    ("学习仪表盘", "综合复盘"),
]


def clean(text: str) -> str:
    return dedent(text).strip() + "\n"


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(clean(content), encoding="utf-8")


def day_dir(day: int) -> str:
    return f"day{day:02d}"


def shared_css() -> str:
    return """
    :root {
      font-family: "Segoe UI", "Microsoft YaHei", Arial, sans-serif;
      color: #182033;
      background: #f6f8fb;
    }
    body { margin: 0; background: #f6f8fb; }
    .page { width: min(980px, calc(100vw - 32px)); margin: 0 auto; padding: 28px 0 56px; }
    .topline { display: flex; justify-content: space-between; margin-bottom: 20px; color: #64748b; }
    a { color: #0f5cc0; text-decoration: none; }
    a:hover { text-decoration: underline; }
    h1 { margin: 0 0 20px; font-size: 34px; line-height: 1.2; }
    h2 { margin: 24px 0 10px; font-size: 22px; }
    p, li { font-size: 16px; line-height: 1.75; }
    code { font-family: Consolas, "Cascadia Code", monospace; background: #eef2f7; padding: 2px 5px; border-radius: 4px; }
    pre { overflow: auto; background: #101827; color: #dbeafe; padding: 16px; border-radius: 8px; }
    pre code { background: transparent; padding: 0; }
    section, .card { background: #fff; border: 1px solid #dbe3ef; border-radius: 8px; padding: 18px 22px; margin: 14px 0; }
    .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 12px; }
    .badge { display: inline-block; padding: 2px 8px; border-radius: 999px; background: #e0f2fe; color: #075985; font-size: 13px; }
    """


def docs_html(course_title: str, course_slug: str, day: int, title: str, concept: str, files: list[str], run_command: str) -> str:
    file_items = "\n".join(f"<li><code>{html.escape(name)}</code></li>" for name in files)
    return f"""
    <!doctype html>
    <html lang="zh-CN">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>{html.escape(course_title)} 第 {day:02d} 天 - {html.escape(title)}</title>
      <link rel="stylesheet" href="../assets/style.css">
    </head>
    <body>
      <main class="page">
        <nav class="topline"><a href="../index.html">返回课程目录</a><span>第 {day:02d} 天</span></nav>
        <h1>{html.escape(course_title)} 第 {day:02d} 天：{html.escape(title)}</h1>
        <section>
          <h2>今天目标</h2>
          <p>通过一个小项目掌握：<strong>{html.escape(concept)}</strong>。</p>
        </section>
        <section>
          <h2>项目文件</h2>
          <ul>{file_items}</ul>
        </section>
        <section>
          <h2>运行方式</h2>
          <p>进入当天目录后运行：</p>
          <pre><code>{html.escape(run_command)}</code></pre>
        </section>
        <section>
          <h2>学习建议</h2>
          <ul>
            <li>先运行项目，观察输出或页面效果。</li>
            <li>再阅读源码，把变量、函数、数据结构和控制流画出来。</li>
            <li>最后完成 README 里的今日练习，哪怕只改一小处也要重新运行。</li>
          </ul>
        </section>
        <section>
          <h2>常见错误</h2>
          <ul>
            <li>路径里有空格时，请在 PowerShell 中用引号包住路径。</li>
            <li>如果脚本被执行策略拦截，可以使用 <code>powershell -ExecutionPolicy Bypass -File .\\run.ps1</code>。</li>
            <li>修改代码后要重新运行或重新编译，不要只看旧输出。</li>
          </ul>
        </section>
      </main>
    </body>
    </html>
    """


def readme(course_title: str, day: int, title: str, concept: str, run_command: str, exercise: str) -> str:
    return f"""
    # {course_title} 第 {day:02d} 天：{title}

    ## 学习目标

    {concept}

    ## 运行

    ```powershell
    {run_command}
    ```

    ## 今日练习

    {exercise}

    ## 建议

    先运行，再改一处代码，然后重新运行验证。每天只追求一个明确概念，不要把项目改得过大。
    """


def course_index(course_title: str, items: list[tuple[str, str]], intro: str) -> str:
    cards = []
    for i, (title, concept) in enumerate(items, 1):
        cards.append(f"""
        <article class="card">
          <span class="badge">Day {i:02d}</span>
          <h2><a href="day{i:02d}/docs.html">{html.escape(title)}</a></h2>
          <p>{html.escape(concept)}</p>
        </article>
        """)
    return f"""
    <!doctype html>
    <html lang="zh-CN">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>{html.escape(course_title)}</title>
      <link rel="stylesheet" href="assets/style.css">
    </head>
    <body>
      <main class="page">
        <h1>{html.escape(course_title)}</h1>
        <section><p>{html.escape(intro)}</p></section>
        <div class="grid">{''.join(cards)}</div>
      </main>
    </body>
    </html>
    """


def top_index() -> str:
    courses = [
        ("Python 30 天学习项目", "python-30days/index.html", "标准库、脚本、文件、JSON、SQLite 和综合练习。"),
        ("JavaScript/CSS/HTML 30 天学习项目", "web-js-css-html-30days/index.html", "纯前端页面、DOM、事件、布局、动画和小应用。"),
        ("纯 C++ 30 天学习项目", "cpp-30days/index.html", "标准 C++17、容器、算法、类、文件和综合练习。"),
        ("C 语言 30 天学习项目", "c-30days/index.html", "C11 风格基础、指针、数组、结构体、文件和内存管理。"),
    ]
    cards = "".join(
        f"""
        <article class="card">
          <h2><a href="{href}">{html.escape(title)}</a></h2>
          <p>{html.escape(desc)}</p>
        </article>
        """
        for title, href, desc in courses
    )
    return f"""
    <!doctype html>
    <html lang="zh-CN">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>四套 30 天学习项目</title>
      <link rel="stylesheet" href="python-30days/assets/style.css">
    </head>
    <body>
      <main class="page">
        <h1>四套 30 天学习项目</h1>
        <section><p>这里汇总 Python、JavaScript/CSS/HTML、纯 C++、C 语言四套学习项目。每套 30 天，每天一个独立小项目。</p></section>
        <div class="grid">{cards}</div>
      </main>
    </body>
    </html>
    """


def python_body(day: int, title: str) -> str:
    snippets = {
        1: 'message = "Hello, Python 学习者"\nprint(message)\nprint("今天开始第 1 个脚本项目")',
        2: 'celsius = 26\nfahrenheit = celsius * 9 / 5 + 32\nprint(f"{celsius}°C = {fahrenheit:.1f}°F")',
        3: 'score = 86\nif score >= 90:\n    level = "优秀"\nelif score >= 75:\n    level = "良好"\nelse:\n    level = "继续练习"\nprint(f"分数 {score}：{level}")',
        4: 'for row in range(1, 6):\n    line = [f"{row}x{col}={row * col:2d}" for col in range(1, 6)]\n    print("  ".join(line))',
        5: 'tasks = ["安装 Python", "运行脚本"]\ntasks.append("修改列表")\nfor index, task in enumerate(tasks, start=1):\n    print(f"{index}. {task}")',
        6: 'contacts = {"Ada": "ada@example.com", "Linus": "linus@example.com"}\ncontacts["Grace"] = "grace@example.com"\nfor name, email in contacts.items():\n    print(f"{name}: {email}")',
        7: 'def kilometers_to_miles(km: float) -> float:\n    return km * 0.621371\n\nfor km in [1, 5, 10]:\n    print(f"{km} km = {kilometers_to_miles(km):.2f} miles")',
        8: 'import random\nimport string\nrandom.seed(30)\nchars = string.ascii_letters + string.digits\npassword = "".join(random.choice(chars) for _ in range(10))\nprint("建议密码:", password)',
        9: 'text = "Python makes small tools pleasant"\nwords = text.split()\nprint("单词数:", len(words))\nprint("最长单词:", max(words, key=len))',
        10: 'from pathlib import Path\nfrom tempfile import TemporaryDirectory\nwith TemporaryDirectory() as tmp:\n    note = Path(tmp) / "note.txt"\n    note.write_text("今天学习文件读写", encoding="utf-8")\n    print(note.read_text(encoding="utf-8"))',
        11: 'import json\ntasks = [{"title": "学习 json", "done": False}, {"title": "保存数据", "done": True}]\ntext = json.dumps(tasks, ensure_ascii=False, indent=2)\nprint(text)\nprint("已完成:", sum(1 for item in json.loads(text) if item["done"]))',
        12: 'def safe_divide(left: float, right: float) -> float | None:\n    try:\n        return left / right\n    except ZeroDivisionError:\n        return None\n\nprint("10 / 2 =", safe_divide(10, 2))\nprint("10 / 0 =", safe_divide(10, 0))',
        13: 'class BankAccount:\n    def __init__(self, owner: str, balance: float = 0):\n        self.owner = owner\n        self.balance = balance\n    def deposit(self, amount: float) -> None:\n        self.balance += amount\n\naccount = BankAccount("Ada", 100)\naccount.deposit(35)\nprint(account.owner, account.balance)',
        14: 'from dataclasses import dataclass\n@dataclass\nclass Book:\n    title: str\n    pages: int\nbooks = [Book("Python 入门", 180), Book("自动化脚本", 220)]\nprint(max(books, key=lambda book: book.pages))',
        15: 'import statistics\nnumbers = [12, 18, 21, 30, 33, 42]\nevens = [n for n in numbers if n % 2 == 0]\nprint("偶数:", evens)\nprint("平均值:", statistics.mean(numbers))',
        16: 'commands = {"add": "添加任务", "list": "列出任务", "done": "完成任务"}\ndef dispatch(command: str) -> str:\n    return commands.get(command, "未知命令")\nfor command in ["add", "list", "help"]:\n    print(command, "=>", dispatch(command))',
        17: 'import csv\nfrom io import StringIO\ndata = "name,score\\nAda,95\\nLinus,88\\n"\nrows = list(csv.DictReader(StringIO(data)))\nprint("最高分:", max(rows, key=lambda row: int(row["score"])))',
        18: 'from datetime import date, timedelta\ntoday = date.today()\nplan = [today + timedelta(days=offset) for offset in range(3)]\nfor item in plan:\n    print(item.isoformat())',
        19: 'from pathlib import Path\npaths = [Path("notes/day01.md"), Path("src/main.py"), Path("README.md")]\nfor path in paths:\n    print(path.suffix or "<no suffix>", path.name)',
        20: 'import argparse\nparser = argparse.ArgumentParser()\nparser.add_argument("--name", default="Python 学习者")\nargs = parser.parse_args([])\nprint(f"你好，{args.name}")',
        21: 'import logging\nlogging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")\nlogging.info("开始处理学习任务")\nlogging.warning("这是一个练习用警告")',
        22: 'def total_files(tree: dict) -> int:\n    return sum(1 if value == "file" else total_files(value) for value in tree.values())\nproject = {"src": {"main.py": "file"}, "README.md": "file"}\nprint("文件数量:", total_files(project))',
        23: 'students = [{"name": "Ada", "score": 95}, {"name": "Linus", "score": 88}]\nstudents.sort(key=lambda item: item["score"], reverse=True)\nprint(students)\nprint(next(item for item in students if item["name"] == "Ada"))',
        24: 'expenses = [{"tag": "book", "amount": 52}, {"tag": "food", "amount": 34}, {"tag": "book", "amount": 20}]\nsummary = {}\nfor item in expenses:\n    summary[item["tag"]] = summary.get(item["tag"], 0) + item["amount"]\nprint(summary)',
        25: 'state = "start"\ntransitions = {"start": "forest", "forest": "treasure", "treasure": "end"}\nwhile state != "end":\n    print("当前位置:", state)\n    state = transitions[state]\nprint("冒险结束")',
        26: 'import configparser\nconfig = configparser.ConfigParser()\nconfig["app"] = {"theme": "light", "font_size": "16"}\nprint(config["app"]["theme"], config["app"].getint("font_size"))',
        27: 'import sqlite3\nconnection = sqlite3.connect(":memory:")\nconnection.execute("create table expense(name text, amount integer)")\nconnection.executemany("insert into expense values (?, ?)", [("book", 52), ("tea", 18)])\nprint(connection.execute("select sum(amount) from expense").fetchone()[0])',
        28: 'import unittest\n\ndef add(left, right):\n    return left + right\n\nclass AddTest(unittest.TestCase):\n    def test_add(self):\n        self.assertEqual(add(2, 3), 5)\n\nresult = unittest.TextTestRunner(verbosity=1).run(unittest.defaultTestLoader.loadTestsFromTestCase(AddTest))\nprint("测试通过:", result.wasSuccessful())',
        29: 'class Toolkit:\n    @staticmethod\n    def slug(text: str) -> str:\n        return text.lower().replace(" ", "-")\nprint(Toolkit.slug("Mini Package Demo"))',
        30: 'skills = {"基础": 10, "文件": 4, "数据": 6, "测试": 2}\ncompleted = sum(skills.values())\nfor name, count in skills.items():\n    print(f"{name}: {count}")\nprint("总练习点:", completed)',
    }
    return (
        f'"""第 {day:02d} 天：{title}"""\n\n'
        "def main() -> None:\n"
        f"{indent(snippets[day], 4)}\n\n"
        'if __name__ == "__main__":\n'
        "    main()\n"
    )


def indent(text: str, spaces: int) -> str:
    pad = " " * spaces
    return "\n".join(pad + line if line else "" for line in text.splitlines())


def js_code(day: int, title: str, concept: str) -> str:
    return f"""
    const app = document.querySelector("#app");
    const state = {{
      day: {day},
      title: "{title}",
      concept: "{concept}",
      items: ["阅读代码", "修改样式", "观察交互"]
    }};

    function render() {{
      const list = state.items.map((item, index) => `<li>${{index + 1}}. ${{item}}</li>`).join("");
      app.innerHTML = `
        <section class="hero">
          <span>Day ${{String(state.day).padStart(2, "0")}}</span>
          <h1>${{state.title}}</h1>
          <p>${{state.concept}}</p>
          <button id="actionButton">完成一个练习步骤</button>
        </section>
        <section class="panel">
          <h2>今日清单</h2>
          <ul>${{list}}</ul>
        </section>
      `;

      document.querySelector("#actionButton").addEventListener("click", () => {{
        state.items.push(`新步骤 ${{state.items.length + 1}}`);
        render();
      }});
    }}

    render();
    """


def web_html(day: int, title: str) -> str:
    return f"""
    <!doctype html>
    <html lang="zh-CN">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>Web 第 {day:02d} 天 - {html.escape(title)}</title>
      <link rel="stylesheet" href="styles.css">
    </head>
    <body>
      <main id="app"></main>
      <script src="script.js"></script>
    </body>
    </html>
    """


def web_css(day: int) -> str:
    accent = ["#2563eb", "#16a34a", "#ea580c", "#9333ea", "#0f766e"][day % 5]
    return f"""
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      min-height: 100vh;
      font-family: "Segoe UI", "Microsoft YaHei", Arial, sans-serif;
      background: #f6f8fb;
      color: #172033;
    }}
    #app {{
      width: min(920px, calc(100vw - 32px));
      margin: 0 auto;
      padding: 40px 0;
    }}
    .hero, .panel {{
      background: white;
      border: 1px solid #dbe3ef;
      border-radius: 8px;
      padding: 24px;
      margin-bottom: 16px;
    }}
    .hero span {{
      color: {accent};
      font-weight: 700;
    }}
    h1 {{ margin: 8px 0 12px; font-size: 34px; }}
    p, li {{ line-height: 1.7; }}
    button {{
      border: 0;
      border-radius: 6px;
      padding: 10px 14px;
      background: {accent};
      color: white;
      cursor: pointer;
    }}
    button:hover {{ filter: brightness(0.94); }}
    """


def cpp_code(day: int, title: str) -> str:
    snippets = {
        1: 'std::cout << "Hello, C++ learner\\\\n";',
        2: 'double price = 42.5; int count = 3; std::cout << "total=" << price * count << "\\\\n";',
        3: 'int score = 86; std::cout << (score >= 60 ? "pass" : "retry") << "\\\\n";',
        4: 'int total = 0; for (int i = 1; i <= 10; ++i) total += i; std::cout << total << "\\\\n";',
        5: 'std::vector<std::string> tasks{"read", "code", "run"}; for (const auto &task : tasks) std::cout << task << "\\\\n";',
        6: 'std::string text = "Modern C++"; std::cout << text << " length=" << text.size() << "\\\\n";',
        7: 'auto square = [](int value) { return value * value; }; std::cout << square(7) << "\\\\n";',
        8: 'struct Task { std::string title; bool done; }; Task task{"learn struct", false}; std::cout << task.title << "\\\\n";',
        9: 'class Counter { int value = 0; public: void add(){ ++value; } int get() const { return value; } }; Counter c; c.add(); std::cout << c.get() << "\\\\n";',
        10: 'struct User { std::string name; explicit User(std::string n) : name(std::move(n)) {} }; User user{"Ada"}; std::cout << user.name << "\\\\n";',
        11: 'enum class Level { beginner, intermediate }; Level level = Level::beginner; std::cout << (level == Level::beginner) << "\\\\n";',
        12: 'std::map<std::string, int> scores{{"Ada", 95}, {"Linus", 88}}; std::cout << scores["Ada"] << "\\\\n";',
        13: 'std::ostringstream out; out << "note:" << 13; std::cout << out.str() << "\\\\n";',
        14: 'try { throw std::runtime_error("practice error"); } catch (const std::exception &error) { std::cout << error.what() << "\\\\n"; }',
        15: 'std::vector<int> numbers{1,2,3,4}; std::for_each(numbers.begin(), numbers.end(), [](int n){ std::cout << n * 2 << " "; }); std::cout << "\\\\n";',
        16: 'std::vector<int> numbers{4,1,3,2}; std::sort(numbers.begin(), numbers.end()); for (int n : numbers) std::cout << n << " "; std::cout << "\\\\n";',
        17: 'auto max_value = [](auto left, auto right) { return left > right ? left : right; }; std::cout << max_value(8, 12) << "\\\\n";',
        18: 'auto value = std::make_unique<int>(42); std::cout << *value << "\\\\n";',
        19: 'std::optional<int> found = 7; if (found) std::cout << *found << "\\\\n";',
        20: 'auto now = std::chrono::system_clock::now(); std::cout << (now.time_since_epoch().count() > 0) << "\\\\n";',
        21: 'std::filesystem::path path{"src/main.cpp"}; std::cout << path.filename().string() << "\\\\n";',
        22: 'std::mt19937 rng(30); std::uniform_int_distribution<int> dist(1, 6); std::cout << dist(rng) << "\\\\n";',
        23: 'std::istringstream input{"Ada 95"}; std::string name; int score; input >> name >> score; std::cout << name << ":" << score << "\\\\n";',
        24: 'std::function<int(int)> factorial = [&](int n){ return n <= 1 ? 1 : n * factorial(n - 1); }; std::cout << factorial(5) << "\\\\n";',
        25: 'std::vector<std::string> names{"Ada","Linus"}; auto it = std::find(names.begin(), names.end(), "Ada"); std::cout << (it != names.end()) << "\\\\n";',
        26: 'std::vector<double> expenses{12.5, 20.0, 8.5}; double sum = std::accumulate(expenses.begin(), expenses.end(), 0.0); std::cout << sum << "\\\\n";',
        27: 'struct Task { std::string title; bool done; }; std::vector<Task> tasks{{"model", false}, {"view", true}}; std::cout << tasks.size() << "\\\\n";',
        28: 'std::map<std::string, std::string> config{{"theme","light"}}; std::cout << config.at("theme") << "\\\\n";',
        29: 'std::map<std::string, std::function<void()>> commands; commands["hello"] = []{ std::cout << "hello command\\\\n"; }; commands["hello"]();',
        30: 'std::vector<int> progress{10, 8, 9, 7}; std::cout << "finished=" << std::accumulate(progress.begin(), progress.end(), 0) << "\\\\n";',
    }
    return f"""
    #include <algorithm>
    #include <chrono>
    #include <filesystem>
    #include <functional>
    #include <iostream>
    #include <map>
    #include <memory>
    #include <numeric>
    #include <optional>
    #include <random>
    #include <sstream>
    #include <stdexcept>
    #include <string>
    #include <utility>
    #include <vector>

    int main() {{
        std::cout << "C++ Day {day:02d}: {title}\\n";
        {snippets[day]}
        return 0;
    }}
    """


def c_code(day: int, title: str) -> str:
    snippets = {
        1: 'printf("Hello, C learner\\\\n");',
        2: 'int count = 3; double price = 12.5; printf("total=%.2f\\\\n", count * price);',
        3: 'int score = 86; printf("%s\\\\n", score >= 60 ? "pass" : "retry");',
        4: 'int sum = 0; for (int i = 1; i <= 10; ++i) sum += i; printf("%d\\\\n", sum);',
        5: 'int values[] = {3, 5, 8, 13}; int sum = 0; for (int i = 0; i < 4; ++i) sum += values[i]; printf("%d\\\\n", sum);',
        6: 'char text[] = "C language"; printf("%zu\\\\n", strlen(text));',
        7: 'printf("square=%d\\\\n", square(7));',
        8: 'Task task = {"learn struct", 0}; printf("%s %d\\\\n", task.title, task.done);',
        9: 'int value = 42; int *ptr = &value; printf("%d\\\\n", *ptr);',
        10: 'int values[] = {1, 2, 3}; int *ptr = values; printf("%d\\\\n", *(ptr + 2));',
        11: 'Level level = LEVEL_BEGINNER; printf("%d\\\\n", level == LEVEL_BEGINNER);',
        12: 'FILE *file = tmpfile(); fputs("temporary note", file); rewind(file); char buffer[64]; fgets(buffer, sizeof(buffer), file); printf("%s\\\\n", buffer); fclose(file);',
        13: 'int result = safe_divide(10, 0); printf("result=%d\\\\n", result);',
        14: 'int *values = malloc(3 * sizeof(int)); values[0] = 4; values[1] = 5; values[2] = 6; printf("%d\\\\n", values[1]); free(values);',
        15: 'int values[] = {4, 1, 3, 2}; qsort(values, 4, sizeof(int), compare_ints); for (int i = 0; i < 4; ++i) printf("%d ", values[i]); printf("\\\\n");',
        16: 'char text[] = "red,green,blue"; char *part = strtok(text, ","); while (part) { printf("%s ", part); part = strtok(NULL, ","); } printf("\\\\n");',
        17: 'int (*operation)(int) = square; printf("%d\\\\n", operation(8));',
        18: 'printf("%d\\\\n", factorial(5));',
        19: 'unsigned flags = 0; flags |= 1u << 2; printf("%u\\\\n", (flags & (1u << 2)) != 0);',
        20: 'printf("%d\\\\n", MAX_VALUE);',
        21: 'print_banner("header-style interface");',
        22: 'Contact contacts[2] = {{"Ada", "ada@example.com"}, {"Linus", "linus@example.com"}}; printf("%s\\\\n", contacts[0].email);',
        23: 'int scores[] = {90, 86, 95}; printf("%.2f\\\\n", average(scores, 3));',
        24: 'char line[] = "book,52"; char name[16]; int amount; sscanf(line, "%15[^,],%d", name, &amount); printf("%s %d\\\\n", name, amount);',
        25: 'State state = STATE_START; state = next_state(state); printf("%d\\\\n", state);',
        26: 'Ring ring = {{0}, 0, 0}; ring_push(&ring, 7); ring_push(&ring, 9); printf("%d\\\\n", ring_pop(&ring));',
        27: 'Command commands[] = {{"hello", say_hello}, {"bye", say_bye}}; commands[0].handler();',
        28: 'Record records[2] = {{1, "book"}, {2, "pen"}}; printf("%d:%s\\\\n", records[1].id, records[1].name);',
        29: 'debug_log("debug message"); assert(square(3) == 9);',
        30: 'int progress[] = {10, 8, 9, 7}; printf("%d\\\\n", sum_array(progress, 4));',
    }
    return f"""
    #include <assert.h>
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>

    #define MAX_VALUE 100

    typedef struct {{ char title[64]; int done; }} Task;
    typedef enum {{ LEVEL_BEGINNER, LEVEL_INTERMEDIATE }} Level;
    typedef struct {{ char name[32]; char email[64]; }} Contact;
    typedef enum {{ STATE_START, STATE_RUNNING, STATE_DONE }} State;
    typedef struct {{ int data[4]; int head; int tail; }} Ring;
    typedef struct {{ int id; char name[32]; }} Record;
    typedef void (*Handler)(void);
    typedef struct {{ const char *name; Handler handler; }} Command;

    int square(int value) {{ return value * value; }}
    int safe_divide(int left, int right) {{ return right == 0 ? 0 : left / right; }}
    int compare_ints(const void *left, const void *right) {{
        int a = *(const int *)left;
        int b = *(const int *)right;
        return (a > b) - (a < b);
    }}
    int factorial(int value) {{ return value <= 1 ? 1 : value * factorial(value - 1); }}
    void print_banner(const char *text) {{ printf("== %s ==\\n", text); }}
    double average(const int *values, int count) {{
        int total = 0;
        for (int i = 0; i < count; ++i) total += values[i];
        return count == 0 ? 0.0 : (double)total / count;
    }}
    State next_state(State state) {{ return state == STATE_START ? STATE_RUNNING : STATE_DONE; }}
    void ring_push(Ring *ring, int value) {{ ring->data[ring->tail % 4] = value; ring->tail++; }}
    int ring_pop(Ring *ring) {{ int value = ring->data[ring->head % 4]; ring->head++; return value; }}
    void say_hello(void) {{ printf("hello command\\n"); }}
    void say_bye(void) {{ printf("bye command\\n"); }}
    void debug_log(const char *message) {{ printf("[debug] %s\\n", message); }}
    int sum_array(const int *values, int count) {{ int total = 0; for (int i = 0; i < count; ++i) total += values[i]; return total; }}

    int main(void) {{
        printf("C Day {day:02d}: {title}\\n");
        {snippets[day]}
        return 0;
    }}
    """


def cmake_cpp(day: int) -> str:
    return f"""
    cmake_minimum_required(VERSION 3.16)
    project(CppDay{day:02d} LANGUAGES CXX)
    set(CMAKE_CXX_STANDARD 17)
    set(CMAKE_CXX_STANDARD_REQUIRED ON)
    add_executable(cpp_day{day:02d} main.cpp)
    """


def cmake_c(day: int) -> str:
    return f"""
    cmake_minimum_required(VERSION 3.16)
    project(CDay{day:02d} LANGUAGES C)
    set(CMAKE_C_STANDARD 11)
    set(CMAKE_C_STANDARD_REQUIRED ON)
    add_executable(c_day{day:02d} main.c)
    """


def generate_python() -> None:
    base = ROOT / "python-30days"
    write(base / "assets" / "style.css", shared_css())
    for day, (title, concept) in enumerate(PYTHON_DAYS, 1):
        folder = base / day_dir(day)
        write(folder / "main.py", python_body(day, title))
        run = f'& "{PYTHON_EXE}" .\\main.py'
        write(folder / "run.ps1", run)
        write(folder / "README.md", readme("Python 30 天学习项目", day, title, concept, ".\\run.ps1", "修改示例数据，重新运行并观察输出变化。"))
        write(folder / "docs.html", docs_html("Python 30 天学习项目", "python-30days", day, title, concept, ["main.py", "run.ps1", "README.md", "docs.html"], ".\\run.ps1"))
    write(base / "index.html", course_index("Python 30 天学习项目", PYTHON_DAYS, "每天一个标准库小项目，按脚本、数据、文件、测试和综合练习逐步推进。"))
    write(base / "README.md", "# Python 30 天学习项目\n\n从 day01 开始，每天运行对应目录里的 `run.ps1`。\n")


def generate_web() -> None:
    base = ROOT / "web-js-css-html-30days"
    write(base / "assets" / "style.css", shared_css())
    for day, (title, concept) in enumerate(WEB_DAYS, 1):
        folder = base / day_dir(day)
        write(folder / "index.html", web_html(day, title))
        write(folder / "styles.css", web_css(day))
        write(folder / "script.js", js_code(day, title, concept))
        run = 'Start-Process (Join-Path $PSScriptRoot "index.html")'
        write(folder / "run.ps1", run)
        write(folder / "README.md", readme("JavaScript/CSS/HTML 30 天学习项目", day, title, concept, ".\\run.ps1", "改一处 HTML 结构、一处 CSS 样式、一处 JS 状态，再刷新页面。"))
        write(folder / "docs.html", docs_html("JavaScript/CSS/HTML 30 天学习项目", "web-js-css-html-30days", day, title, concept, ["index.html", "styles.css", "script.js", "run.ps1", "README.md", "docs.html"], ".\\run.ps1"))
    write(base / "index.html", course_index("JavaScript/CSS/HTML 30 天学习项目", WEB_DAYS, "每天一个纯前端小页面，练习 HTML 结构、CSS 表达和 JavaScript 交互。"))
    write(base / "README.md", "# JavaScript/CSS/HTML 30 天学习项目\n\n每一天都是可直接用浏览器打开的静态页面。\n")


def generate_cpp() -> None:
    base = ROOT / "cpp-30days"
    write(base / "assets" / "style.css", shared_css())
    for day, (title, concept) in enumerate(CPP_DAYS, 1):
        folder = base / day_dir(day)
        write(folder / "main.cpp", cpp_code(day, title))
        write(folder / "CMakeLists.txt", cmake_cpp(day))
        run = f'New-Item -ItemType Directory -Force build | Out-Null\n& "{GXX_EXE}" -std=c++17 -Wall -Wextra .\\main.cpp -o .\\build\\cpp_day{day:02d}.exe\n& .\\build\\cpp_day{day:02d}.exe'
        write(folder / "run.ps1", run)
        write(folder / "README.md", readme("纯 C++ 30 天学习项目", day, title, concept, ".\\run.ps1", "修改 main.cpp 里的示例数据，重新编译并运行。"))
        write(folder / "docs.html", docs_html("纯 C++ 30 天学习项目", "cpp-30days", day, title, concept, ["main.cpp", "CMakeLists.txt", "run.ps1", "README.md", "docs.html"], ".\\run.ps1"))
    write(base / "index.html", course_index("纯 C++ 30 天学习项目", CPP_DAYS, "每天一个标准 C++17 控制台项目，覆盖语法、容器、类、算法和小型综合练习。"))
    write(base / "README.md", "# 纯 C++ 30 天学习项目\n\n每一天都可以直接运行 `run.ps1` 编译并执行。\n")


def generate_c() -> None:
    base = ROOT / "c-30days"
    write(base / "assets" / "style.css", shared_css())
    for day, (title, concept) in enumerate(C_DAYS, 1):
        folder = base / day_dir(day)
        write(folder / "main.c", c_code(day, title))
        write(folder / "CMakeLists.txt", cmake_c(day))
        run = f'New-Item -ItemType Directory -Force build | Out-Null\n& "{GCC_EXE}" -std=c11 -Wall -Wextra .\\main.c -o .\\build\\c_day{day:02d}.exe\n& .\\build\\c_day{day:02d}.exe'
        write(folder / "run.ps1", run)
        write(folder / "README.md", readme("C 语言 30 天学习项目", day, title, concept, ".\\run.ps1", "修改 main.c 里的数组或结构体数据，重新编译并运行。"))
        write(folder / "docs.html", docs_html("C 语言 30 天学习项目", "c-30days", day, title, concept, ["main.c", "CMakeLists.txt", "run.ps1", "README.md", "docs.html"], ".\\run.ps1"))
    write(base / "index.html", course_index("C 语言 30 天学习项目", C_DAYS, "每天一个 C 控制台小项目，覆盖基础语法、指针、结构体、文件、内存和综合练习。"))
    write(base / "README.md", "# C 语言 30 天学习项目\n\n每一天都可以直接运行 `run.ps1` 编译并执行。\n")


def main() -> None:
    generate_python()
    generate_web()
    generate_cpp()
    generate_c()
    write(ROOT / "learning-projects-index.html", top_index())
    print("Generated four 30-day learning project sets.")


if __name__ == "__main__":
    main()
