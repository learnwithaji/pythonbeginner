# Prompt the user to enter their height and weight
height_cm = float(input("Enter your height in centimeters: "))
weight = float(input("Enter your weight in kilograms: "))

# Convert height from centimeters to meters
height_m = height_cm / 100

# Calculate the BMI using the formula weight / height^2
bmi = weight / (height_m ** 2)

# Determine the BMI category based on the BMI value
if bmi < 18.5:
    category = "underweight"
elif bmi < 25:
    category = "normal weight"
elif bmi < 30:
    category = "overweight"
else:
    category = "obese"

# Display a message indicating the user's BMI and BMI category
print("Your BMI is {:.1f}, which means you are {}".format(bmi, category))
