# create a nested list of tourist places and their details
places = [["Munnar", "Idukki", "Tea plantations, trekking trails, and scenic views"],
          ["Kovalam", "Thiruvananthapuram", "Beaches, lighthouse, and water sports"],
          ["Alleppey", "Alappuzha", "Backwaters, houseboat rides, and beaches"],
          ["Wayanad", "Wayanad", "Hill station, wildlife sanctuary, and natural beauty"]]

print("Welcome to the Kerala Tourist Places program!")

# loop to display menu and process user's input
while True:
    print("\nEnter 1 to view details of a place")
    print("Enter 2 to add a new place")
    print("Enter 3 to exit")
    choice = input("\nEnter your choice: ")

    # option to view place details
    if choice == "1":
        place_name = input("\nEnter the name of the place: ")
        found = False
        for place in places:
            if place[0].lower() == place_name.lower():
                print(f"\nDetails of {place[0]}:")
                print(f"Location: {place[1]}")
                print(f"Famous for: {place[2]}")
                found = True
                break
        if not found:
            print("\nPlace not found in list!")

    # option to add a new place
    elif choice == "2":
        new_place = []
        new_place.append(input("\nEnter the name of the new place: "))
        new_place.append(input("Enter the location of the new place: "))
        new_place.append(input("Enter what the new place is famous for: "))
        places.append(new_place)
        print("\nPlace details added successfully!")

    # option to exit the program
    elif choice == "3":
        print("\nGoodbye!")
        break

    # invalid input
    else:
        print("\nInvalid choice! Please enter 1, 2, or 3.")
