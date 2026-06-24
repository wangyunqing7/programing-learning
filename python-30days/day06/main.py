"""第 06 天：联系人字典（通讯录）

掌握：dict 键值结构、模糊搜索、排序。
支持增删查、按名字模糊搜索、列出全部。
"""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Contact:
    name: str
    email: str
    phone: str = ""


@dataclass
class AddressBook:
    contacts: dict[str, Contact] = field(default_factory=dict)

    def add(self, c: Contact) -> None:
        if c.name in self.contacts:
            raise KeyError(f"已存在：{c.name}")
        self.contacts[c.name] = c

    def remove(self, name: str) -> None:
        if name not in self.contacts:
            raise KeyError(f"找不到：{name}")
        del self.contacts[name]

    def get(self, name: str) -> Contact | None:
        return self.contacts.get(name)

    def search(self, keyword: str) -> list[Contact]:
        """名字或邮箱里包含关键字就算命中（大小写不敏感）。"""
        kw = keyword.lower()
        return [c for c in self.contacts.values()
                if kw in c.name.lower() or kw in c.email.lower()]

    def list_sorted(self) -> list[Contact]:
        return sorted(self.contacts.values(), key=lambda c: c.name)


def render(contacts: list[Contact]) -> None:
    if not contacts:
        print("  （无结果）")
        return
    for c in contacts:
        print(f"  {c.name:<10} {c.email:<24} {c.phone}")


def main() -> None:
    book = AddressBook()
    book.add(Contact("Ada", "ada@example.com", "13800000001"))
    book.add(Contact("Linus", "linus@example.com", "13800000002"))
    book.add(Contact("Grace", "grace@example.com", "13800000003"))
    book.add(Contact("Alan", "alan@example.com", "13800000004"))

    print("全部联系人：")
    render(book.list_sorted())

    print("\n搜索 'a'：")
    render(book.search("a"))

    print("\n删除 Grace 后：")
    book.remove("Grace")
    render(book.list_sorted())

    # 边界
    try:
        book.add(Contact("Ada", "dup@example.com"))
    except KeyError as e:
        print(f"\n边界测试：{e}")


if __name__ == "__main__":
    main()
