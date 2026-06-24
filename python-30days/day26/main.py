"""第 26 天：配置读取器

掌握：configparser、默认值、类型校验。
读取 INI 配置，补默认值，校验必填项。
"""
from __future__ import annotations

import configparser
from pathlib import Path
from tempfile import NamedTemporaryFile

DEFAULTS = {
    "app": {"name": "MyApp", "version": "1.0", "debug": "false"},
    "db": {"host": "localhost", "port": "5432"},
}

REQUIRED = {"db": ["host"]}


def write_sample(path: Path) -> None:
    content = """[app]
name = DemoApp
debug = true

[db]
host = 127.0.0.1
port = 6543
"""
    path.write_text(content, encoding="utf-8")


def load(path: Path) -> configparser.ConfigParser:
    cfg = configparser.ConfigParser()
    cfg.read_dict(DEFAULTS)  # 先塞默认值
    read_files = cfg.read(path, encoding="utf-8")
    if not read_files:
        raise FileNotFoundError(f"配置文件不存在：{path}")
    validate(cfg)
    return cfg


def validate(cfg: configparser.ConfigParser) -> None:
    for section, keys in REQUIRED.items():
        if not cfg.has_section(section):
            raise ValueError(f"缺少配置节：[{section}]")
        for k in keys:
            if not cfg.get(section, k):
                raise ValueError(f"[{section}].{k} 不能为空")


def render(cfg: configparser.ConfigParser) -> None:
    print("应用配置：")
    print(f"  名称：{cfg.get('app', 'name')}")
    print(f"  版本：{cfg.get('app', 'version')}")
    print(f"  调试：{cfg.getboolean('app', 'debug')}")
    print("数据库配置：")
    print(f"  主机：{cfg.get('db', 'host')}")
    print(f"  端口：{cfg.getint('db', 'port')}")


def main() -> None:
    with NamedTemporaryFile("w", suffix=".ini", delete=False, encoding="utf-8") as tmp:
        path = Path(tmp.name)
    write_sample(path)
    cfg = load(path)
    render(cfg)
    path.unlink()

    # 边界：文件不存在
    print()
    try:
        load(Path("not_exist.ini"))
    except FileNotFoundError as e:
        print(f"边界测试：{e}")


if __name__ == "__main__":
    main()
