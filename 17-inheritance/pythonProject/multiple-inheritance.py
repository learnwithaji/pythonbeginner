class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"Name: {self.name}")

class Employee:
    def __init__(self, salary):
        self.salary = salary

    def show_salary(self):
        print(f"Salary: {self.salary}")

class Manager(Person, Employee):
    def __init__(self, name, salary):
        Person.__init__(self, name)
        Employee.__init__(self, salary)

    def show_details(self):
        self.show_name()
        self.show_salary()

manager = Manager("Alice", 80000)

print("Manager Details:")
manager.show_details()
