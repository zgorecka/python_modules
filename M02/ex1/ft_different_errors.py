def garden_operations() -> None:
    try:
        print("Testing ValueError...")
        temp = int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")
    try:
        print("Testing ZeroDivisionError...")
        temp = 20 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")
    try:
        print("Testing FileNotFoundError...")
        temp = open("missing.txt")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")
    try:
        print("Testing KeyError...")
        temp = {"": ""}
        print(temp["missing"])
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'\n")
    try:
        print("Testing multiple errors together...")
        int("xyz")
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
