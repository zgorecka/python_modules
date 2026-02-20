def ft_archive_creation() -> None:
    file_name = "new_discovery.txt"

    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print(f"Initializing new storage unit: {file_name}")

    try:
        with open(file_name, "w") as file:
            print("Storage unit created successfully...")
            print("Inscribing preservation data...")

            entries = [
                "[ENTRY 001] New quantum algorithm discovered",
                "[ENTRY 002] Efficiency increased by 347%",
                "[ENTRY 003] Archived by Data Archivist trainee"
            ]

            for entry in entries:
                file.write(entry + "\n")
                print(entry)
            print("Data inscription complete. Storage unit sealed.")
            print(f"Archive '{file_name}' ready for long-term preservation.")
    except OSError as e:
        print("Error: ", e)


if __name__ == "__main__":
    ft_archive_creation()