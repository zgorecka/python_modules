def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        print(f"{str(seed_type.capitalize())} seeds: ")
        print(f"{quantity} {unit} available")
    elif unit == "grams":
        print(f"{str(seed_type.capitalize())} seeds: ")
        print(f"{quantity} {unit} total")
    elif unit == "area":
        print(f"{str(seed_type.capitalize())} seeds: ", end='')
        print(f"covers {quantity} square meters")
    else:
        print("Unknown unit type")
