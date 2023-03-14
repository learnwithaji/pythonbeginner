# Prompt the user to enter the scores for the assignment and test
assignment_score = float(input("Enter the score for the assignment (out of 100): "))
test_score = float(input("Enter the score for the test (out of 100): "))

# Calculate the weighted average of the scores
assignment_weight = 0.4
test_weight = 0.6
weighted_average = (assignment_score * assignment_weight) + (test_score * test_weight)

# Assign a letter grade based on the final grade
if weighted_average >= 90:
    letter_grade = "A"
elif weighted_average >= 80:
    letter_grade = "B"
elif weighted_average >= 70:
    letter_grade = "C"
elif weighted_average >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# Print the final grade and letter grade to the console
print("Your final grade is {:.1f} and your letter grade is {}".format(weighted_average, letter_grade))
