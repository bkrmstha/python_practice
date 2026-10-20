class Employee:
    def __init__(self, employee_id, name, department, salary):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary
        
    def employee_info(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Monthly Salary: {self.salary}")
        print(f"Annual {self.calculate_annual_salary()}")
        print("\n")
        
    def calculate_annual_salary(self):
        annual_salary = self.salary * 12
        return annual_salary
    
employee1 = Employee(1001, "Bikram", "IT", 50000)
employee2 = Employee(1002, "Samikshya", "Account", 30000)
employee3 = Employee(1003, "Unish", "Finance", 46000)

employee1.employee_info()
employee2.employee_info()
employee3.employee_info()