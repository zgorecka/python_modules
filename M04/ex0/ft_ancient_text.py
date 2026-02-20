def ft_acient_text() -> None:
    file_name = "ancient_fragment.txt"
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print(f"Accessing Storage Vault: {file_name}")
    try:
        with open(file_name, "r") as file:
            print("Connection established...")
            for line in file:
                print(line.strip())
        print("Data recovery complete. Storage unit disconnected.")
    except FileNotFoundError as e:
        print("Error: ", e)


if __name__ == "__main__":
    ft_acient_text()
