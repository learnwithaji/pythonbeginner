# Prompt the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform addition, subtraction, multiplication, and division
# Using the arithmetic operators +, -, *, and /
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

# Display the results using the print function
print("The sum of {} and {} is: {}".format(num1, num2, addition))
print("The difference between {} and {} is: {}".format(num1, num2, subtraction))
print("The product of {} and {} is: {}".format(num1, num2, multiplication))
print("The quotient of {} and {} is: {}".format(num1, num2, division))
