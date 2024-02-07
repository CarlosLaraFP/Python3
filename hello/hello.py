# source venv/bin/activate
# deactivate

from employee import Employee
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

import pandas as pd
import os

# Construct the absolute path to the CSV file
current_script_path = os.path.abspath(__file__)  # Gets the absolute path of the current script
project_directory = os.path.dirname(os.path.dirname(current_script_path))  # Navigate up twice to get the project directory
csv_path = os.path.join(project_directory, 'earthquakes.csv')  # Construct the full path to the CSV


earthquakes = pd.read_csv(csv_path)

print(earthquakes.head())

print(earthquakes.info()) # count and schema

print(earthquakes.describe())

import matplotlib.pyplot as plt
import seaborn as sns

# Histogram of a column
earthquakes['mag'].hist()
plt.show()

# Scatter plot for two variables
sns.scatterplot(x='depth', y='mag', data=earthquakes)
plt.show()

