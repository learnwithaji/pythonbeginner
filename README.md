# Sample programs to practice

Here is the sample programming questions to practice. Try them to code yourself. If you want help, you can download the program files (.py) from the repository.
File name of each program is given in the parenthesis.

### 1. Simple calculator (calculator.py)
Build a simple calculator program that can add, subtract, multiply, and divide two numbers.

### 2. Simple input/print program (userdata.py)
Create a program that asks the user for their name, age, and favorite color, and then prints out a message that includes this information.

### 3. Check prime number (checkprime.py)
Write a program that asks the user for a number, and then checks whether it is prime or not.

### 4. BMI Calculator (checkbmi.py)
In this program, the user enters their height and weight and the program calculates their Body Mass Index (BMI) and provides a message indicating whether they are underweight, normal weight, overweight, or obese.

### 5. Grade Calculator: (studentsgrade.py)
In this project, you will create a program that calculates a student's grade based on their scores on various assignments and tests. The program will use control structures to handle input validation and calculate the final grade based on a predefined grading scale.

Here are the requirements for the project:
1. Prompt the user to enter the number of assignments and tests.
2. For each assignment, prompt the user to enter the score and weight (as a percentage) of the assignment.
3. For each test, prompt the user to enter the score and weight (as a percentage) of the test. 4 Validate the user's input to ensure that they are valid numbers.
4. Calculate the weighted average of the assignment and test scores to determine the student's overall grade.
5. Assign a letter grade based on the final grade using a predefined grading scale (e.g., A for grades 90-100, B for grades 80-89, etc.).
6. Print the final grade and letter grade to the console.

To implement this project, you will need to use loops (for) to iterate over the assignments and tests and calculate the weighted average of the scores. You can also use conditional statements (if/elif/else) to assign the appropriate letter grade based on the final grade.

### 6. Write a program to write Fibonacci series (fibonacci.py)

The Fibonacci series is a sequence of numbers in which each number is the sum of the two preceding numbers. The series starts with 0 and 1, and each subsequent number is the sum of the two previous numbers. 

So the first few numbers in the Fibonacci series are 0, 1, 1, 2, 3, 5, 8, 13, 21, and so on. The series is named after Leonardo Fibonacci, an Italian mathematician who introduced the series to the western world in his book Liber Abaci, published in 1202. The Fibonacci series appears in many areas of mathematics and science, including number theory, geometry, and biology.

### 7. Python functions question (calculate_discounted_price.py)
Write a function calculate_discounted_price that takes in three parameters: price, discount_percentage, and tax_percentage. The function should calculate the discounted price by applying the discount percentage to the original price, and then adding the tax amount to the discounted price. The function should return the final discounted price.

### 8. Programming exercise using Python lists (python_lists.py)
Create a program that keeps a list of tourist places in Kerala and their details. The program should allow the user to enter a place name and display its details. The program should also have the option to add a new place and its details to the list.

### 9. Exercise demonstrate list comprehension (celsius_fahrenheit)
Suppose you have a list of temperatures in Celsius and you want to convert them to Fahrenheit using the formula F = C * 9/5 + 32. 
You can use list comprehension to create a new list of Fahrenheit temperatures in a single line of code.

### 10. Exercise demonstrate dictionary comprehension (dictionary_menu.py)
You are working in a restaurant and want to keep track of the food items being ordered by customers. Write a program that allows you to do the following:

1. Create an empty dictionary to store the food items and their prices.
2. Allow the user to add new food items to the dictionary along with their prices.
3. Display the current menu with all the food items and their prices.
4. Allow the user to search for a particular food item and display its price.
5. Allow the user to remove a food item from the menu.
6. Calculate the total revenue earned by the restaurant based on the number of items sold and their prices.

You can use the following menu items and their prices as a starting point:

menu = {'Appam': 40,
'Puttu': 35,
'Dosa': 50,
'Idiyappam': 40,
'Parotta': 30}

### 11. Basic file operations (python-file.py)

You are working for a supermarket and need to create a program that can read and write to a file containing the inventory of products in the store. The file should contain the following information for each product:

* Product name
* Price
* Quantity in stock

Your program should allow the user to perform the following actions:
1. Add a new product to the inventory
2. Update the quantity of an existing product in the inventory
3. Display the current inventory
4. Save changes to the file and exit the program

When the program starts, it should read the existing inventory file (if it exists) and load the product information into memory. When the user makes changes to the inventory, the program should update the in-memory data and also write the changes back to the file before exiting.

### 12. Creater a shopping cart module (shopping_cart.py, shopping.py)
Create a Python module called "shopping_cart" that simulates a retail shopping cart. Your module should contain the following five functions:

1. add_item(item_name: str, price: float) -> None: This function should add an item to the shopping cart. The item should be represented as a dictionary with keys "name" and "price".
2. remove_item(item_name: str) -> None: This function should remove an item from the shopping cart.
3. get_total() -> float: This function should return the total cost of all items in the shopping cart.
4. get_items() -> list: This function should return a list of all items in the shopping cart.
5. checkout() -> None: This function should print out a receipt with a list of all items in the shopping cart, their prices, and the total cost.

Your module should be able to handle multiple shopping carts, each with their own set of items.
To test your module, create a script that imports the shopping_cart module and uses it to simulate a few shopping transactions.
