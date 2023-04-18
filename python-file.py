import os

# Define the file path to store the inventory
file_path = "inventory.txt"

# Define the function to read the inventory file and return a dictionary
def read_inventory():
    inventory = {}
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            for line in f:
                name, price, quantity = line.strip().split(",")
                inventory[name] = {
                    "price": float(price),
                    "quantity": int(quantity)
                }
    return inventory

# Define the function to write the inventory dictionary to the file
def write_inventory(inventory):
    with open(file_path, "w") as f:
        for name, info in inventory.items():
            price = info["price"]
            quantity = info["quantity"]
            f.write(f"{name},{price},{quantity}\n")

# Define the function to add a new product to the inventory
def add_product(inventory):
    name = input("Enter the product name: ")
    price = float(input("Enter the product price: "))
    quantity = int(input("Enter the product quantity: "))
    inventory[name] = {
        "price": price,
        "quantity": quantity
    }
    print(f"{name} added to the inventory.")

# Define the function to update the quantity of an existing product in the inventory
def update_quantity(inventory):
    name = input("Enter the product name: ")
    if name not in inventory:
        print(f"{name} not found in the inventory.")
        return
    quantity = int(input("Enter the new quantity: "))
    inventory[name]["quantity"] = quantity
    print(f"{name} quantity updated.")

# Define the function to display the current inventory
def display_inventory(inventory):
    if not inventory:
        print("Inventory is empty.")
        return
    print("Current inventory:")
    for name, info in inventory.items():
        price = info["price"]
        quantity = info["quantity"]
        print(f"{name}: ${price} ({quantity} in stock)")

# Main program loop
inventory = read_inventory()
while True:
    print("\n1. Add a new product")
    print("2. Update the quantity of an existing product")
    print("3. Display the current inventory")
    print("4. Save changes and exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_product(inventory)
    elif choice == "2":
        update_quantity(inventory)
    elif choice == "3":
        display_inventory(inventory)
    elif choice == "4":
        write_inventory(inventory)
        print("Changes saved.")
        break
    else:
        print("Invalid choice.")
