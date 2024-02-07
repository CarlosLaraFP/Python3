from hello.employee import Employee
import datetime

# Creating an instance using the standard constructor
emp = Employee(name="John Doe", hire_date=datetime.date(2015, 6, 1), salary=50000)
print(emp)
print(f"Years of Service: {emp.years_of_service()}")

# Creating an instance using a class method
emp2 = Employee.from_name_and_years("Jane Smith", 5)
print(emp2)
print(f"Years of Service: {emp2.years_of_service()}")

# Using a static method
print(Employee.is_full_time(45))  # True
print(Employee.is_full_time(35))  # False
