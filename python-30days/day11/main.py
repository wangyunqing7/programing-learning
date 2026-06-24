"""第 11 天：JSON 任务数据

掌握：json 序列化、嵌套结构、持久化。
一个带「项目 -> 任务」两级结构的待办，能增删查、存盘、读盘。
"""
from __future__ import annotations

import json
import tempfile
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Project:
    name: str
    tasks: list[dict] = field(default_factory=list)

    def add_task(self, title: str, done: bool = False) -> None:
        if any(t["title"] == title for t in self.tasks):
            raise ValueError(f"任务已存在：{title}")
        self.tasks.append({"title": title, "done": done})

    def done_count(self) -> int:
        return sum(1 for t in self.tasks if t["done"])


@dataclass
class Workspace:
    projects: dict[str, Project] = field(default_factory=dict)

    def add_project(self, name: str) -> None:
        if name in self.projects:
            raise KeyError(f"项目已存在：{name}")
        self.projects[name] = Project(name)

    def to_dict(self) -> dict:
        return {n: {"tasks": p.tasks} for n, p in self.projects.items()}

    @classmethod
    def from_dict(cls, data: dict) -> "Workspace":
        ws = cls()
        for name, body in data.items():
            p = Project(name)
            p.tasks = body.get("tasks", [])
            ws.projects[name] = p
        return ws

    def save(self, path: Path) -> None:
        path.write_text(json.dumps(self.to_dict(), ensure_ascii=False, indent=2),
                        encoding="utf-8")

    @classmethod
    def load(cls, path: Path) -> "Workspace":
        return cls.from_dict(json.loads(path.read_text(encoding="utf-8")))


def render(ws: Workspace) -> None:
    for name, p in ws.projects.items():
        print(f"[{name}] 完成 {p.done_count()}/{len(p.tasks)}")
        for t in p.tasks:
            print(f"   {'[x]' if t['done'] else '[ ]'} {t['title']}")


def main() -> None:
    ws = Workspace()
    ws.add_project("学习")
    ws.add_project("生活")
    ws.projects["学习"].add_task("看完 day11")
    ws.projects["学习"].add_task("写 JSON 练习", done=True)
    ws.projects["生活"].add_task("买菜")
    render(ws)

    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "ws.json"
        ws.save(p)
        again = Workspace.load(p)
        print(f"\n存盘后重载项目数：{len(again.projects)}")

    # 边界
    try:
        ws.projects["学习"].add_task("看完 day11")
    except ValueError as e:
        print(f"\n边界测试：{e}")


if __name__ == "__main__":
    main()
