from typing import Generator


def game_event_stream(limit: int) -> Generator[dict, None, None]:
    players = ["alice", "bob", "charlie"]
    actions = ["killed monster", "found treasure", "leveled up"]

    for i in range(1, limit + 1):
        event = {
            "id": i,
            "player": players[i % len(players)],
            "level": (i % 15) + 1,
            "action": actions[i % len(actions)],
        }
        yield event


def fibonacci() -> Generator[int, None, None]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def prime_numbers() -> Generator[int, None, None]:
    num = 2
    while True:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            yield num

        num += 1

def main() -> None:
    print("=== Game Data Stream Processor ===\n")

    event_count = 1000
    print(f"Processing {event_count} game events...\n")

    total_events = 0
    high_level_players = 0
    treasure_events = 0
    level_up_events = 0

    for event in game_event_stream(event_count):
        total_events += 1

        if event["level"] >= 10:
            high_level_players += 1

        if event["action"] == "found treasure":
            treasure_events += 1

        if event["action"] == "leveled up":
            level_up_events += 1

    print("=== Stream Analytics ===")
    print("Total events processed:", total_events)
    print("High-level players (10+):", high_level_players)
    print("Treasure events:", treasure_events)
    print("Level-up events:", level_up_events)

    print("\nMemory usage: Constant (streaming)")

    print("\n=== Generator Demonstration ===")

    fib = fibonacci()
    fib_numbers = []

    for i in range(10):
        fib_numbers.append(next(fib))

    print("Fibonacci sequence (first 10):", ", ".join(str(n) for n in fib_numbers))

    primes = prime_numbers()
    prime_list = []

    for i in range(5):
        prime_list.append(next(primes))

    print("Prime numbers (first 5):", ", ".join(str(p) for p in prime_list))



if __name__ == "__main__":
    main()