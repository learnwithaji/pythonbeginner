class Employee:
    def __init__(self, name, job_title, salary):
        self.name = name
        self.job_title = job_title
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}, Job Title: {self.job_title}, Salary: {self.salary}")

emp1 = Employee("John", 'Software Engineer', 10000)
emp1.display_info()

print(emp1.name)