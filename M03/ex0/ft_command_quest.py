import sys

def _program_name(raw: str) -> str:
    return raw.split("/")[-1]


def main(argv: list[str]) -> None:
    print("=== Command Quest ===")

    prog = _program_name(argv[0])
    argc = len(argv)

    if argc == 1:
        print("No arguments provided!")
        print(f"Program name: {prog}")
        print(f"Total arguments: {argc}")
        return

    print(f"Program name: {prog}")
    print(f"Arguments received: {argc - 1}")

    i = 1
    while i < argc:
        print(f"Argument {i}: {argv[i]}")
        i += 1

    print(f"Total arguments: {argc}")


if __name__ == "__main__":
    main(sys.argv)
