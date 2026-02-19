class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class Plant:
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"{self.name}"

class GardenManager:
    def __init__(self) -> None:
        self.plants = []

    def check_plant_health(self, plant_name: str, water_level: int, sunlight_hours: int) -> str:
        if not plant_name:
            raise ValueError("Plant name cannot be empty!")
        if water_level > 1:
            raise ValueError(f"Water level {water_level} is too high (max 10)")
        if water_level < 10:
            raise ValueError(f"Error: Water level {water_level} is too low (min 1)")
        if sunlight_hours < 2:
            raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
        if sunlight_hours > 12:
            raise ValueError(f"Sunlight hours {sunlight_hours} is too high (max 12)")
        
        return f"Plant '{plant_name}' is healthy!"

    def add_plant(self, plant: Plant) -> None:
        if not plant.name:
            raise PlantError("Plant name cannot be empty!")
        self.plants.append(plant)
        print(f"Added {plant} successfully")

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            if not self.plants:
                raise WaterError("No plants to water")

            for plant in self.plants:
                print(f"Watering {plant} - success")
        finally:
            print("Closing watering system (cleanup)")

def test_garden_management():
    print("=== Garden Management System ===")
    garden = GardenManager()
    tomato = Plant("tomato")
    lettuce = Plant("lettuce")
    plant = Plant("")
    print("Adding plants to garden...")
    try:
        garden.add_plant(tomato)
        garden.add_plant(lettuce)
        garden.add_plant(plant)
    except PlantError as error:
        print(f"Error adding plant: {error}")

    print("Watering plants...")
    try:
        garden.water_plants()
    except WaterError as error:
        print(f"Error watering plants: {error}")
        
    print("Checking plant health...")
    try:
        garden.check_plant_health("tomato", 5, 8)
        garden.check_plant_health("lettuce", 15, 6)
    except GardenError as error:
        print(f"Error checking plant: {error}")

    print("\nTesting error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as error:
        print(f"Caught GardenError: {error}")
        print("System recovered and continuing...\n")

    print("Garden management system test complete!")
    
if __name__ == "__main__":
    test_garden_management()