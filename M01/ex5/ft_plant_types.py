class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        return f"{self.name} ({self.height}cm, {self.age} days)"

class Flower(Plant):

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):

    def __init__(self, name: str, height: int, age: int, trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        shade = self.trunk_diameter * 1.56
        print(f"{self.name} provides {shade:.0f} square meters of shade")

class Vegetable(Plant):

    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        harvest_season: str,
        nutritional_value: str,
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")

    flowers = [
        Flower("Rose", 25, 30, "red"),
        Flower("Tulip", 20, 25, "yellow"),
    ]

    trees = [
        Tree("Oak", 500, 1825, 50),
        Tree("Pine", 450, 1500, 40),
    ]

    vegetables = [
        Vegetable("Tomato", 80, 90, "summer", "vitamin C"),
        Vegetable("Carrot", 40, 70, "autumn", "beta-carotene"),
    ]

    for flower in flowers:
        print(f"{flower.name} (Flower): {flower.height}cm, {flower.age} days, {flower.color} color")
        flower.bloom()
        print()

    for tree in trees:
        print(
            f"{tree.name} (Tree): {tree.height}cm, {tree.age} days, "
            f"{tree.trunk_diameter}cm diameter"
        )
        tree.produce_shade()
        print()

    for vegetable in vegetables:
        print(
            f"{vegetable.name} (Vegetable): {vegetable.height}cm, {vegetable.age} days, "
            f"{vegetable.harvest_season} harvest"
        )
        print(f"{vegetable.name} is rich in {vegetable.nutritional_value}\n")