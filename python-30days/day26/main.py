"""第 26 天：配置读取器"""

def main() -> None:
    import configparser
    config = configparser.ConfigParser()
    config["app"] = {"theme": "light", "font_size": "16"}
    print(config["app"]["theme"], config["app"].getint("font_size"))

if __name__ == "__main__":
    main()
