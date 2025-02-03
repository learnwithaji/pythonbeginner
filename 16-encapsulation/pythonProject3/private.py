class Employee:
    def __init__(self, name, job_title, salary):
        self.name = name
        self.job_title = job_title
        self.salary = salary
        self.__bonus = 5000

    def display_info(self):
        print(f"Name: {self.name}, Job Title: {self.job_title}, Salary: {self.salary}")

    def print_bonus(self):
        return self.__bonus

    def change_bonus(self, new_bonus):

        self.__bonus = new_bonus

    def __calculate_bonus(self):
        bonus = 0
        return bonus

emp1 = Employee("John", 'Software Engineer', 10000)

print(emp1.name)
#print(emp1.__bonus)

print(emp1.print_bonus())
emp1.change_bonus(6000)
print(emp1.print_bonus())

