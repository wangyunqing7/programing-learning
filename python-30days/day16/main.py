"""第 16 天：CLI 菜单模拟"""

def main() -> None:
    commands = {"add": "添加任务", "list": "列出任务", "done": "完成任务"}
    def dispatch(command: str) -> str:
        return commands.get(command, "未知命令")
    for command in ["add", "list", "help"]:
        print(command, "=>", dispatch(command))

if __name__ == "__main__":
    main()
