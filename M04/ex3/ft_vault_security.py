def ft_vault_security() -> None:
    file_name = "security_protocols.txt"
    file_name_w = "classified_data.txt"

    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")

    try:
        with open(file_name, "r") as file:
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")
            content = file.read()
            print(content.strip())

        new_entry = "[CLASSIFIED] New security protocols archived\n"
        with open(file_name_w, "w") as file:
            print("\nSECURE PRESERVATION:")
            file.write(new_entry)
            print(new_entry.strip())

        print("Vault automatically sealed upon completion")
        print("All vault operations completed with maximum security.")
    except FileNotFoundError as e:
        print("Error: ", e)
    except IOError as e:
        print("Error", e)


if __name__ == "__main__":
    ft_vault_security()
