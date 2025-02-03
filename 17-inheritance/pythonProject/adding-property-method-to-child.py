class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Employee Name: {self.name}, Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department
        self.team_size = 0

    def show_team_size(self):
        print(f"{self.name} manages a team of {self.team_size} members.")

manager = Manager("Alice", 80000, "HR")
manager.team_size = 5

print("Manager Details:")
manager.show_details()
manager.show_team_size()
