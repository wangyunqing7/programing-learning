"""第 06 天：联系人字典"""

def main() -> None:
    contacts = {"Ada": "ada@example.com", "Linus": "linus@example.com"}
    contacts["Grace"] = "grace@example.com"
    for name, email in contacts.items():
        print(f"{name}: {email}")

if __name__ == "__main__":
    main()
