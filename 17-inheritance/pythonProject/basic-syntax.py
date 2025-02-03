class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Employee Name: {self.name}, Salary: {self.salary}")

class Manager(Employee):
    pass

m1 = Manager("Alice", 80000)
m1.show_details()