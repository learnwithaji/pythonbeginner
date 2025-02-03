car_type = "SUV"
match car_type:
    case "Sedan":
        print("Eligible for basic insurance.")
    case "SUV":
        print("Eligible for premium insurance.")
    case "Convertible":
        print("Eligible for luxury insurance.")
    case _:
        print("Default insurance plan applies.")
