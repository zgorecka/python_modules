class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age
    
    def grow(self):
        self.height += 1

    def old(self):
        self.age += 1

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Sunflower", 80, 45)
    p3 = Plant("Cactus", 15, 120)

    print("=== Day 1 ===")
    p1.get_info()
    p2.get_info()
    p3.get_info()
    for i in range(0, 6):
        p1.grow()
        p1.old()
        p2.grow()
        p2.old()
        p3.grow()
        p3.old()
    print("=== Day 7 ===")
    p1.get_info()
    p2.get_info()
    p3.get_info()
    
