from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def get_full_info(self):
        pass

    def get_basic_info(self):
        return f"Employee: {self.name}, ID: {self.employee_id}"

class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, salary):
        super().__init__(name, employee_id)
        self.salary = salary

    def calculate_salary(self):
        return f"Full-time salary: ${self.salary}"

    def get_full_info(self):
        return f"Full-time Employee: {self.name}, ID: {self.employee_id}, Salary: ${self.salary}"

class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hourly_wage, hours_worked):
        super().__init__(name, employee_id)
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked

    def calculate_salary(self):
        total_salary = self.hourly_wage * self.hours_worked
        return f"Part-time salary: ${total_salary}"

    def get_full_info(self):
        return f"Part-time Employee: {self.name}, ID: {self.employee_id}, Hourly Wage: ${self.hourly_wage}, Hours Worked: {self.hours_worked}"

full_time_emp = FullTimeEmployee("John Doe", "E001", 60000)
part_time_emp = PartTimeEmployee("Jane Smith", "E002", 20, 100)

print(full_time_emp.get_basic_info())
print(full_time_emp.get_full_info())
print(full_time_emp.calculate_salary())

print(part_time_emp.get_basic_info())
print(part_time_emp.get_full_info())
print(part_time_emp.calculate_salary())
