import sys

def ft_inventory_system():
    print("=== Inventory System Analysis ===")

    if len(sys.argv) < 2:
        print("No inventory items provided.")
        print("Usage: python3 ft_inventory_system.py item:quantity ...")
        return

    inventory: dict[str, int] = {}

    for arg in sys.argv[1:]:
        try:
            name, quantity = arg.split(":")
            quantity_int = int(quantity)

            if name in inventory:
                inventory[name] += quantity_int
            else:
                inventory[name] = quantity_int

        except ValueError:
            print(f"Invalid format: {arg}")
            return

    total_items = sum(inventory.values())
    unique_types = len(inventory)

    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {unique_types}")

    print("\n=== Current Inventory ===")

    items_list = list(inventory.items())

    n = len(items_list)

    for i in range(n):
        for j in range(0, n - i - 1):
            if items_list[j][1] < items_list[j + 1][1]:
                items_list[j], items_list[j + 1] = items_list[j + 1], items_list[j]

    for name, quantity in items_list:
        percentage = (quantity / total_items) * 100
        print(f"{name}: {quantity} units ({percentage:.1f}%)")

    print("\n=== Inventory Statistics ===")
    most_abundant = None
    least_abundant = None

    for name, quantity in inventory.items():
        if most_abundant is None or quantity > inventory[most_abundant]:
            most_abundant = name

        if least_abundant is None or quantity < inventory[least_abundant]:
            least_abundant = name

    print(f"Most abundant: {most_abundant} ({inventory.get(most_abundant)} units)")
    print(f"Least abundant: {least_abundant} ({inventory.get(least_abundant)} units)")

    print("\n=== Item Categories ===")

    moderate: dict[str, int] = {}
    scarce: dict[str, int] = {}

    for name, quantity in inventory.items():
        if quantity >= 5:
            moderate[name] = quantity
        else:
            scarce[name] = quantity

    print("Moderate:", moderate)
    print("Scarce:", scarce)

    print("\n=== Management Suggestions ===")

    restock = [name for name, qty in inventory.items() if qty <= 1]


    if restock:
        print("Restock needed:", ", ".join(restock))
    else:
        print("No restocking needed.")

    print("\n=== Dictionary Properties Demo ===")

    print("Dictionary keys:", ", ".join(inventory.keys()))
    print("Dictionary values:", ", ".join(str(v) for v in inventory.values()))
    print("Sample lookup - 'sword' in inventory:", "sword" in inventory)


if __name__ == "__main__":
    ft_inventory_system()