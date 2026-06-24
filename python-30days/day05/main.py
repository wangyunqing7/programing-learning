"""第 05 天：任务列表（TODO 管理器）

掌握：list 增删改查、dataclass、JSON 持久化。
一个能增删、完成、列出、存盘的迷你 TODO。
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field, asdict
from pathlib import Path


@dataclass
class Task:
    title: str
    done: bool = False
    priority: int = 2  # 1 高 / 2 中 / 3 低


@dataclass
class TaskManager:
    tasks: list[Task] = field(default_factory=list)

    def add(self, title: str, priority: int = 2) -> None:
        title = title.strip()
        if not title:
            raise ValueError("任务标题不能为空")
        if any(t.title == title for t in self.tasks):
            raise ValueError(f"任务已存在：{title}")
        self.tasks.append(Task(title, priority=priority))

    def complete(self, title: str) -> None:
        for t in self.tasks:
            if t.title == title:
                t.done = True
                return
        raise KeyError(f"找不到任务：{title}")

    def remove(self, title: str) -> None:
        before = len(self.tasks)
        self.tasks = [t for t in self.tasks if t.title != title]
        if len(self.tasks) == before:
            raise KeyError(f"找不到任务：{title}")

    def list_all(self) -> list[Task]:
        # 按优先级、完成状态排序：未完成在前，优先级数字小的在前
        return sorted(self.tasks, key=lambda t: (t.done, t.priority))

    def save(self, path: Path) -> None:
        path.write_text(json.dumps([asdict(t) for t in self.tasks],
                                   ensure_ascii=False, indent=2), encoding="utf-8")

    @classmethod
    def load(cls, path: Path) -> "TaskManager":
        if not path.exists():
            return cls()
        data = json.loads(path.read_text(encoding="utf-8"))
        return cls(tasks=[Task(**d) for d in data])


def render(mgr: TaskManager) -> None:
    print(f"共 {len(mgr.tasks)} 项任务：")
    for i, t in enumerate(mgr.list_all(), 1):
        mark = "[x]" if t.done else "[ ]"
        print(f"  {i}. {mark} (P{t.priority}) {t.title}")


def main() -> None:
    mgr = TaskManager()
    mgr.add("学习 Python 基础", priority=1)
    mgr.add("写一个 TODO 程序", priority=1)
    mgr.add("复习 list 用法", priority=3)
    mgr.complete("学习 Python 基础")
    render(mgr)

    # 持久化到临时文件演示
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "tasks.json"
        mgr.save(p)
        loaded = TaskManager.load(p)
        print(f"\n从磁盘重新加载后任务数：{len(loaded.tasks)}")

    # 边界
    print()
    try:
        mgr.add("")
    except ValueError as e:
        print(f"边界测试：{e}")
    try:
        mgr.complete("不存在的任务")
    except KeyError as e:
        print(f"边界测试：{e}")


if __name__ == "__main__":
    main()
