class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self._height = 0
        self._age = 0
        print(f"Plan created: {self.name}")

    def set_height(self, h: int) -> None:
        if h > 0:
            self.height = h
            print(f"Height updated: {h}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {h}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, a: int) -> None:
        if a > 0:
            self.age = a
            print(f"Age updated: {a} [OK]")
        else:
            print(f"Invalid operation attempted: age {a} [REJECTED]")
            print("Security: Negative age rejected")

    def get_height(self) -> int:
        return self.age

    def get_age(self) -> int:
        return self.age

    def get_info(self) -> str:
        return f"{self.name} ({self.height}cm, {self.age} days)"


if __name__ == "__main__":
    print("=== Garden Security System ===")
    p1 = Plant("Rose", 25, 30)
    p1.set_height(25)
    p1.set_age(30)
    p1.set_height(-5)
    print(f"Current plant: {p1.get_info()}")
