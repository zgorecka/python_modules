def ft_crisis_response() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    file1 = "lost_archive.txt"
    print(f"CRISIS ALERT: Attempting access to '{file1}'...")

    try:
        with open(file1, "r") as f:
            f.read()
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")

    file2 = "classified_vault.txt"
    print(f"CRISIS ALERT: Attempting access to '{file2}'...")
    try:
        with open(file2, "r") as f:
            f.read()
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")

    file3 = "standard_archive.txt"
    print(f"ROUTINE ACCESS: Attempting access to '{file3}'...")
    try:
        with open(file3, "r") as f:
            content = f.read().strip()
            print(f"SUCCESS: Archive recovered - ``{content}''")
            print("STATUS: Normal operations resumed\n")
    except FileNotFoundError:
        print("RESPONSE: Standard archive missing\n")

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    ft_crisis_response()
