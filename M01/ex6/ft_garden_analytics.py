class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

        def grow(self) -> None:
            self.height += 1

    def get_info(self) -> str:
        return f"{self.name} ({self.height}cm, {self.age} days)"

class FloweringPlant(Plant):

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")


class PrizeFlower(Plant):

    def __init__(self, name: str, height: int, age: int, trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        shade = self.trunk_diameter * 1.56
        print(f"{self.name} provides {shade:.0f} square meters of shade")


class GardenManager:
    def __init__(self, name: str):
        self.name = name
        self.plants = []

    def add_plant(self, plant: Plant):
        self.plants.append(plant)
        print(f"Added Oak Tree to Alice's garden")

    def GardenStats() -> None:
        print("")

if __name__ == "__main__":
    g = GardenManager("dupsko")
    p1 = PrizeFlower("dupa", 10, 20, 1)
    g.add_plant(p1)