import sys


def main(argv: list[str]) -> None:
    print("=== List Metrics ===")

    if len(argv) == 1:
        print("No numbers provided!")
        return

    numbers = []

    for arg in argv[1:]:
        try:
            numbers.append(int(arg))
        except ValueError:
            print(f"Error: '{arg}' is not a valid integer.")
            return

    total = sum(numbers)
    average = total / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)

    print(f"Numbers: {numbers}")
    print(f"Sum: {total}")
    print(f"Average: {average}")
    print(f"Min: {minimum}")
    print(f"Max: {maximum}")


if __name__ == "__main__":
    main(sys.argv)
