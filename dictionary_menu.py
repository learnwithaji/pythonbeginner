# Define the menu as a global variable
menu = {'Appam': 40, 'Puttu': 35, 'Dosa': 50, 'Idiyappam': 40, 'Parotta': 30}


# Function to add a new food item to the menu
def add_item():
    item_name = input("Enter the name of the new food item: ")
    item_price = float(input("Enter the price of the new food item: "))
    menu[item_name] = item_price


# Function to display the current menu
def display_menu():
    print("Current Menu:")
    for item, price in menu.items():
        print(item + " - " + str(price))


# Function to search for a food item and display its price
def search_item():
    item_name = input("Enter the name of the food item to search for: ")
    if item_name in menu:
        print("The price of " + item_name + " is " + str(menu[item_name]))
    else:
        print(item_name + " is not on the menu.")


# Function to remove a food item from the menu
def remove_item():
    item_name = input("Enter the name of the food item to remove: ")
    if item_name in menu:
        del menu[item_name]
        print(item_name + " has been removed from the menu.")
    else:
        print(item_name + " is not on the menu.")


# Function to calculate the total revenue earned
def calculate_revenue():
    total_revenue = 0
    for item, price in menu.items():
        quantity = int(input("How many " + item + "s were sold? "))
        total_revenue += price * quantity
    print("Total revenue: $" + str(total_revenue))


# Main function to run the program
while True:
    print("Please choose an option:")
    print("1. Add a new food item to the menu")
    print("2. Display the current menu")
    print("3. Search for a food item and display its price")
    print("4. Remove a food item from the menu")
    print("5. Calculate the total revenue earned")
    print("6. Exit the program")
    choice = input()

    if choice == "1":
        add_item()
    elif choice == "2":
        display_menu()
    elif choice == "3":
        search_item()
    elif choice == "4":
        remove_item()
    elif choice == "5":
        calculate_revenue()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
