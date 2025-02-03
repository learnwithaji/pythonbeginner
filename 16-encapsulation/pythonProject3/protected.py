class Employee:
    def __init__(self, name, job_title, salary):
        self.name = name
        self.job_title = job_title
        self.salary = salary
        self._bonus_percent = 10

    def display_info(self):
        print(f"Name: {self.name}, Job Title: {self.job_title}, Salary: {self.salary}")

    def print_bonus(self):
        return self.salary * self._bonus_percent / 100

emp1 = Employee("Bob", 'Software Engineer', 10000)

print(emp1.name)
print(emp1._bonus_percent)