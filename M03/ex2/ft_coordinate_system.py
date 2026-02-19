import sys
import math


def distance_3d(p1: tuple[float, float, float], p2: tuple[float, float, float]) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def parse_coords(text: str) -> tuple[int, int, int]:
    parts = text.split(",")
    if len(parts) != 3:
        raise ValueError(f"Expected 3 values separated by commas, got: {text!r}")
    x = int(parts[0])
    y = int(parts[1])
    z = int(parts[2])
    return (x, y, z)


def main(argv: list[str]) -> None:
    print("=== Game Coordinate System ===")

    origin = (0, 0, 0)

    pos_created = (10, 20, 5)
    print(f"Position created: {pos_created}")

    d1 = distance_3d(origin, (float(pos_created[0]), float(pos_created[1]), float(pos_created[2])))
    print(f"Distance between {origin} and {pos_created}: {d1:.2f}")

    good = "3,4,0"
    print(f'Parsing coordinates: "{good}"')
    parsed = parse_coords(good)
    print(f"Parsed position: {parsed}")

    d2 = distance_3d(origin, (float(parsed[0]), float(parsed[1]), float(parsed[2])))
    print(f"Distance between {origin} and {parsed}: {d2}")

    bad = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{bad}"')
    try:
        _ = parse_coords(bad)
    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")

    print("Unpacking demonstration:")
    x, y, z = parsed
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main(sys.argv)
