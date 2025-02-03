class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Employee Name: {self.name}, Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def show_details(self):
        super().show_details()
        print(f"Department: {self.department}")

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def show_details(self):
        super().show_details()
        print(f"Programming Language: {self.programming_language}")

m1 = Manager("Alice", 80000, "HR")
m1.show_details()

d1 = Developer("Rahul", 80000, "Python")
d1.show_details()