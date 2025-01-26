import os


def load_names(filename):
    # Load names from a file.
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return [line.strip() for line in file.readlines()]
    return []

def save_names(filename, names):
    # Save names to a file.
    with open(filename, 'w') as file:
        for name in names:
            file.write(name + '\n')


def main():
    filename = "names.txt"
    names = load_names(filename)

    print("Hello, this is the name database. Please choose an action below.")
    print("1. Add name")
    print("2. Remove name")
    print("3. See names")
    print("4. Clear names")
    print("5. Exit (NOTE: MAKE SURE TO ACTUALLY USE THIS OR IT WILL NOT SAVE THE CHANGES)")

    while True:
        action = input("Choose an action (add, remove, see, clear, exit): ").lower()

        if action == "exit":
            save_names(filename, names)
            print("Goodbye!")
            break
        elif action == "add":
            nameInput = input("What name would you like to add? ")
            names.append(nameInput)
            print(f"Added: {nameInput}")
        elif action == "remove":
            if not names:
                print("No names to remove.")
            else:
                print("Which name to remove?")
                print(names)
                nameToRemove = input("Enter the name to remove: ")
                if nameToRemove in names:
                    names.remove(nameToRemove)
                    print(f"Removed: {nameToRemove}")
                else:
                    print("Name not found.")
        elif action == "see":
            if not names:
                print("No names to see.")
            else:
                print("Current names: " + ", ".join(names))
        elif action == "clear":
            names.clear()
            print("All names cleared.")
        else:
            print("Invalid action. Please choose again.")


if __name__ == "__main__":
    main()
