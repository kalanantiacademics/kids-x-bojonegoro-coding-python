def add_contact():
    print("\n--- Add Contact ---")
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    with open('phonebook.txt', 'a') as file:
        file.write(f"{name},{phone}\n")
    print(f"[{name}] has been saved!")

def show_contacts():
    print("\n--- Phone Book ---")
    with open('phonebook.txt', "r") as file:
        lines = file.readlines()

    if not lines:
        print("Your phone book is empty.")
    else:
        for index, line in enumerate(lines, start=1):
            name, phone = line.strip().split(",")
            print(f"{index}. Name: {name} | Phone: {phone}")

def delete_contact():
    print("\n--- Delete Contact ---")
    name_to_delete = input("Enter the exact name to delete: ")

    with open('phonebook.txt', "r") as file:
        lines = file.readlines()
    found = False

    with open('phonebook.txt', "w") as file:
        for line in lines:
            if not line.startswith(name_to_delete + ","):
                file.write(line)
            else:
                found = True
    if found:
        print(f"[{name_to_delete}] has been deleted.")
    else:
        print(f"Contact [{name_to_delete}] not found.")

while True:
    print("=== MENU ===")
    print("1. Add Contact")
    print("2. Show Contacts")
    print("3. Delete Contact")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")
    if choice == '1':
        add_contact()
    elif choice == '2':
        show_contacts()
    elif choice == '3':
        delete_contact()
    elif choice == '4':
        print("Exiting phone book. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")