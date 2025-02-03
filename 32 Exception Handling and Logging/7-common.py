try:
    with open('nonexistent_file.txt', 'r') as file:
        content = file.read()

    number = int("abc")

    data = {"name": "Alice"}
    print(data["age"])

    numbers = [1, 2, 3]
    print(numbers[5])

    result = "Hello" + 5

    division = 10 / 0

except FileNotFoundError:
    print("Error: The file you are trying to open does not exist.")
except ValueError:
    print("Error: Invalid value provided. Could not convert string to int.")
except KeyError:
    print("Error: The key you are looking for is not in the dictionary.")
except IndexError:
    print("Error: List index out of range.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except Exception as e:
    print(str(e))
