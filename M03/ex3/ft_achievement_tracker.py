def ft_achievement_tracker() -> None:
    print("=== Achievement Tracker System ===\n")

    alice: set[str] = {
        "first_kill",
        "level_10",
        "treasure_hunter",
        "speed_demon"
    }

    bob: set[str] = {
        "first_kill",
        "level_10",
        "boss_slayer",
        "collector"
    }

    charlie: set[str] = {
        "level_10",
        "treasure_hunter",
        "boss_slayer",
        "speed_demon",
        "perfectionist"
    }

    print("Player alice achievements:", alice)
    print("Player bob achievements:", bob)
    print("Player charlie achievements:", charlie)

    print("\n=== Achievement Analytics ===")

    all_achievements = alice.union(bob).union(charlie)
    print("All unique achievements:", all_achievements)
    print("Total unique achievements:", len(all_achievements))

    common_all = alice.intersection(bob).intersection(charlie)
    print("\nCommon to all players:", common_all)

    rare = set()

    for achievement in all_achievements:
        count = 0
        if achievement in alice:
            count += 1
        if achievement in bob:
            count += 1
        if achievement in charlie:
            count += 1
        if count == 1:
            rare.add(achievement)

    print("Rare achievements (1 player):", rare)

    alice_bob_common = alice.intersection(bob)
    alice_unique = alice.difference(bob)
    bob_unique = bob.difference(alice)

    print("\nAlice vs Bob common:", alice_bob_common)
    print("Alice unique:", alice_unique)
    print("Bob unique:", bob_unique)


if __name__ == "__main__":
    ft_achievement_tracker()
