inventory = []
inventory = {}
print("--- Personal Inventory Manager ---")

print("n/Options: [1] Add, [2] Remove, [3] List, [4] Exit")
choice = input("Select an option: ")

while choice != "4":
    if choice == 1:
        name = input("Enter item name: ").strip().capitalize()
        qty = int(input(f"How many {name}s"))
        if name in inventory:
            inventory[name] += qty
            else:
                inventory[name] = qty
        print("n/Options: [1] Add, [2] Remove, [3] List, [4] Exit")
        choice = input("Select an option: ")
    
    if choice == 2:
        name = input("Which item would you like to remove? ").strip().capitalize()
