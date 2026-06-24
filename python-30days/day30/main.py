"""第 30 天：学习仪表盘

掌握：综合复盘、数据汇总、报表。
把 30 天的知识点按周汇总，输出一个学习仪表盘。
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Topic:
    day: int
    title: str
    skill: str


WEEKLY = {
    "第 1 周 · 脚本与数据基础": [
        Topic(1, "Hello CLI", "print/变量/入口"),
        Topic(2, "温度换算器", "运算/格式化"),
        Topic(3, "成绩判断器", "条件分支"),
        Topic(4, "乘法表", "循环/排版"),
        Topic(5, "任务列表", "list/JSON"),
        Topic(6, "联系人字典", "dict/搜索"),
        Topic(7, "单位换算", "函数分发"),
    ],
    "第 2 周 · 函数、字符串与文件": [
        Topic(8, "密码建议器", "random/字符串"),
        Topic(9, "文本统计器", "Counter/TopN"),
        Topic(10, "临时笔记", "pathlib/IO"),
        Topic(11, "JSON 任务", "json/嵌套"),
        Topic(12, "安全除法", "异常分类"),
        Topic(13, "银行账户类", "class/状态"),
        Topic(14, "图书 dataclass", "dataclass"),
    ],
    "第 3 周 · 推导、标准库与 CLI": [
        Topic(15, "列表推导统计", "推导式"),
        Topic(16, "CLI 菜单", "命令分发"),
        Topic(17, "CSV 成绩表", "csv"),
        Topic(18, "日期计划表", "datetime"),
        Topic(19, "路径整理器", "pathlib"),
        Topic(20, "参数解析器", "argparse"),
        Topic(21, "日志记录器", "logging"),
    ],
    "第 4 周 · 进阶与综合": [
        Topic(22, "递归目录摘要", "递归"),
        Topic(23, "排序和搜索", "sorted/bisect"),
        Topic(24, "支出统计器", "聚合"),
        Topic(25, "文字冒险", "状态机"),
        Topic(26, "配置读取器", "configparser"),
        Topic(27, "SQLite 记账", "sqlite3"),
        Topic(28, "单元测试", "unittest"),
        Topic(29, "迷你包结构", "包/导入"),
        Topic(30, "学习仪表盘", "综合"),
    ],
}


def dashboard() -> None:
    total = sum(len(v) for v in WEEKLY.values())
    print(f"Python 30 天学习仪表盘  共 {total} 天\n")
    for week, topics in WEEKLY.items():
        print(f"=== {week}（{len(topics)} 天）===")
        for t in topics:
            print(f"  Day {t.day:>2}  {t.title:<12} {t.skill}")
        print()


def main() -> None:
    dashboard()
    skills = {t.skill for topics in WEEKLY.values() for t in topics}
    print(f"累计掌握知识点：{len(skills)} 个")
    print("恭喜完成 30 天 Python 之旅！🎉")


if __name__ == "__main__":
    main()
