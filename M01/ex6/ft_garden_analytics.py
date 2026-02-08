class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height

    def grow(self) -> None:
        self.height += 1

    def __str__(self) -> str:
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color
        self.blooming = False

    def bloom(self) -> None:
        self.blooming = True

    def __str__(self) -> str:
        status = " (blooming)" if self.blooming else ""
        return f"{self.name}: {self.height}cm, {self.color} flowers{status}"


class PrizeFlower(FloweringPlant):
    def __init__(
        self,
        name: str,
        height: int,
        color: str,
        prize_points: int,
    ) -> None:
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def __str__(self) -> str:
        base = super().__str__()
        return f"{base}, Prize points: {self.prize_points}"


class GardenManager:
    total_gardens = 0

    class GardenStats:
        @staticmethod
        def total_growth(plants: list[Plant]) -> int:
            return sum(p.height for p in plants)

        @staticmethod
        def count_types(plants: list[Plant]) -> str:
            r = sum(isinstance(p, Plant) and not
                    isinstance(p, FloweringPlant) for p in plants)
            f = sum(isinstance(p, FloweringPlant) and not
                    isinstance(p, PrizeFlower) for p in plants)
            p = sum(isinstance(p, PrizeFlower) for p in plants)
            return f"{r} regular, {f} flowering, {p} prize flowers"

    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants = []
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        for plant in self.plants:
            plant.grow()
            print(f"{plant.name} grew 1cm")

    @classmethod
    def create_garden_network(cls) -> None:
        print("Garden network created")

    @staticmethod
    def validate_height(height: int) -> bool:
        return height >= 0

    def report(self) -> None:
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant}")


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    alice = GardenManager("Alice")

    oak = Plant("Oak Tree", 0)
    rose = FloweringPlant("Rose", 0, "red")
    sunflower = PrizeFlower("Sunflower", 0, "yellow", 10)

    rose.bloom()
    sunflower.bloom()

    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)

    alice.grow_all()

    print(f"\n=== {alice.owner}'s Garden Report ===")

    alice.report()

    stats = GardenManager.GardenStats
    print(f"Plants added: {len(alice.plants)}, ", end='')
    print("Total growth:", stats.total_growth(alice.plants))
    print("Plant types:", stats.count_types(alice.plants))

    print("Height validation test:", GardenManager.validate_height(10))
    GardenManager.create_garden_network()
