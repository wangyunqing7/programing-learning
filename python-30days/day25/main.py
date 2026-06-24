"""第 25 天：文字冒险

掌握：状态机、字典描述转移、物品系统。
一个多房间、可拾取物品的迷你冒险。
"""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class World:
    rooms: dict[str, dict]
    transitions: dict[str, dict[str, str]]
    inventory: list[str] = field(default_factory=list)
    current: str = "entrance"


def describe(world: World) -> None:
    room = world.rooms[world.current]
    print(f"\n【{room['name']}】{room['desc']}")
    if room.get("item") and room["item"] not in world.inventory:
        print(f"  你看到：{room['item']}")
    exits = world.transitions.get(world.current, {})
    if exits:
        print(f"  出口：{', '.join(exits)}")


def act(world: World, action: str) -> None:
    parts = action.split(maxsplit=1)
    verb = parts[0]
    arg = parts[1] if len(parts) > 1 else ""

    if verb == "go":
        nxt = world.transitions.get(world.current, {}).get(arg)
        if nxt is None:
            print(f"  去不了：{arg}")
        else:
            world.current = nxt
    elif verb == "take":
        room = world.rooms[world.current]
        if room.get("item") == arg and arg not in world.inventory:
            world.inventory.append(arg)
            print(f"  拾取了：{arg}")
        else:
            print(f"  这里没有：{arg}")
    elif verb == "bag":
        print(f"  背包：{world.inventory or '空'}")
    else:
        print(f"  不会：{verb}")


def main() -> None:
    world = World(
        rooms={
            "entrance": {"name": "入口", "desc": "一扇古老的门。", "item": "torch"},
            "hall": {"name": "大厅", "desc": "空旷的大厅，有回声。"},
            "treasure": {"name": "宝物室", "desc": "金光闪闪！", "item": "gold"},
        },
        transitions={
            "entrance": {"north": "hall"},
            "hall": {"south": "entrance", "east": "treasure"},
            "treasure": {"west": "hall"},
        },
    )

    # 用脚本演示一局
    script = ["bag", "take torch", "go north", "go east", "take gold", "bag", "go west"]
    for action in script:
        print(f"\n> {action}")
        act(world, action)
    describe(world)


if __name__ == "__main__":
    main()
