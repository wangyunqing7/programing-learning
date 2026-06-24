"""第 16 天：CLI 菜单模拟

掌握：函数分发、会话循环、字典做命令表。
一个用命令字符串驱动的任务管理会话。
"""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Session:
    tasks: list[str] = field(default_factory=list)
    running: bool = True

    def cmd_add(self, arg: str) -> str:
        if not arg:
            return "用法：add <任务>"
        self.tasks.append(arg)
        return f"已添加：{arg}"

    def cmd_list(self, arg: str) -> str:
        if not self.tasks:
            return "（空）"
        return "\n".join(f"{i}. {t}" for i, t in enumerate(self.tasks, 1))

    def cmd_done(self, arg: str) -> str:
        try:
            idx = int(arg) - 1
        except ValueError:
            return "用法：done <序号>"
        if not (0 <= idx < len(self.tasks)):
            return "序号超出范围"
        return f"完成：{self.tasks.pop(idx)}"

    def cmd_help(self, arg: str) -> str:
        return "命令：add <任务> | list | done <序号> | help | exit"

    def cmd_exit(self, arg: str) -> str:
        self.running = False
        return "再见"


# 命令名 -> 方法名 的分发表
COMMANDS = {
    "add": "cmd_add",
    "list": "cmd_list",
    "done": "cmd_done",
    "help": "cmd_help",
    "exit": "cmd_exit",
}


def run_script(session: Session, lines: list[str]) -> None:
    """用预设脚本驱动会话（演示用，不依赖真实 input）。"""
    for line in lines:
        parts = line.split(maxsplit=1)
        cmd = parts[0]
        arg = parts[1] if len(parts) > 1 else ""
        method = COMMANDS.get(cmd)
        if method is None:
            print(f"> {line}\n  未知命令：{cmd}")
            continue
        print(f"> {line}")
        print(" ", getattr(session, method)(arg))


def main() -> None:
    s = Session()
    run_script(s, [
        "help",
        "add 学完 day16",
        "add 写一个菜单",
        "list",
        "done 1",
        "list",
        "bogus",      # 未知命令
        "done 99",    # 越界
        "exit",
    ])


if __name__ == "__main__":
    main()
