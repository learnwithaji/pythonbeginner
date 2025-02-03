from datetime import datetime
birthdate = input("Enter your date of birth (YYYY-MM-DD): ")
print(type(birthdate))
birth_date = datetime.strptime(birthdate, "%Y-%m-%d")
print(type(birth_date))

age = (datetime.now() - birth_date).days // 365 #floor division
print("Your Age:", age, "years")
