from typing import List


# Create a class called Employee with a static method called calculate_payroll 
# that takes a list of Employee instances and returns the total amount to be paid to all employees. 
# Each Employee instance has two attributes: name and salary.

class Employee:
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary

    @staticmethod
    def calculate_payroll(employee_list: List['Employee']) -> float:
        summed_salaries = 0
        for employee in employee_list:
            summed_salaries += employee.salary
            return summed_salaries
        
employee_list = [Employee(name="Antanas", salary=1000),
                 Employee(name="Linas", salary=600),
                 Employee(name="Toma", salary=100)
]

print(Employee.calculate_payroll(employee_list))

