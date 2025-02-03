age = 16
try:
    if age < 18:
        raise ValueError("Age must be 18 or older.")
    else:
        print("You are eligible.")
except ValueError as e:
    print(f"Error: {e}")
