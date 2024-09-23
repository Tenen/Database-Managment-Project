import json
import os
from tkinter import messagebox
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
EMPLOYEE_FILE_PATH = BASE_DIR / "data" / "employees.json" 
# Function to load employees from the JSON file
def load_employees():
    if os.path.exists(EMPLOYEE_FILE_PATH):
        with open(EMPLOYEE_FILE_PATH, 'r') as file:
            try:
                employees = json.load(file)
            except json.JSONDecodeError:
                employees = []
    else:
        employees = []
    return employees


# Function to save employees to the JSON file
def save_employees(employees):
    try:
        with open(EMPLOYEE_FILE_PATH, 'w') as file:
            json.dump(employees, file, indent=4)
    except IOError as e:
        print(f"Error saving employees: {e}")


# Function to add a new employee
def add_employee(FuncText,name, age, emp_id, salary,gender,number,email,yox):
    if FuncText == "Add":
        employees = load_employees()

        # Check for duplicate ID
        for employee in employees:
            if employee["ID"] == emp_id:
                print(f"Error: An employee with ID {emp_id} already exists.")
                print(
                    f"Existing Employee - Name: {employee['Name']}, Age: {employee['Age']}, ID: {employee['ID']}, Salary: {employee['Salary']},Gender: {employee['Gender']}, Number: {employee['Number']}, Email: {employee['Email']}, Years of Exp.: {employee['Years of Exp.']},")
                print("Please try again with a different ID.")
                messagebox.showwarning("Please try again with a different ID.", "Error: An employee with ID already exists")

                return  # Exit the function to prompt the user again in the main loop

        # Add new employee if ID is unique
        new_employee = {
            "Name": name,
            "Age": age,
            "ID": emp_id,
            "Salary": salary,
            "Gender": gender,
            "Number": number,
            "Email": email,
            "Years of Exp.": yox
        }
        employees.append(new_employee)
        save_employees(employees)
        print("Employee added successfully!")


# Function to edit an existing employee by ID or Name
def edit_employee(FuncText,identifier,name, age, emp_id, salary,gender,number,email,yox):
    if FuncText == "Edit":
        print("id is :" , identifier)

        employees = load_employees()
        matched_employees = [e for e in employees if int(e["ID"]) == int(identifier)]
    # identifier = int(identifier)
        if not matched_employees:
            print(f"No employee found with ID: {type(identifier)}")
            messagebox.showwarning("Erorr", "No employee found with ID,Select an item first")

            return

        if len(matched_employees) > 1:
            print("\nMultiple employees found:")
            for idx, employee in enumerate(matched_employees, start=1):
                print(
                    f"{idx}. Name: {employee['Name']}, Age: {employee['Age']}, ID: {employee['ID']}, Salary: {employee['Salary']}")
            choice = int(input("Select the employee number to edit: ")) - 1
            if 0 <= choice < len(matched_employees):
                employee = matched_employees[choice]
            else:
                print("Invalid selection.")
                messagebox.showwarning("Erorr", "Invalid selection.")
                
                return
        else:
            employee = matched_employees[0]

        if name:
            employee["Name"] = name
        if age:
            employee["Age"] = age
        if salary:
            employee["Salary"] = salary
        if emp_id:
            employee["ID"] = emp_id
        if gender:
            employee["Gender"] = gender
        if number:
            employee["Number"] = number
        if email:
            employee["Email"] = email
        if yox:
            employee["Years of Exp."] = yox


        save_employees(employees)
        print("Employee edited successfully.")


# Function to delete an employee by ID
def delete_employee(identifier):
    employees = load_employees()
    
    # Check if employee exists before deleting
    if any(emp['ID'] == str(identifier) for emp in employees):  # Assuming 'id' is lowercase
        # Find and remove the employee with the matching ID
        updated_data = [emp for emp in employees if emp['ID'] != str(identifier)]
        
        # Save the updated list of employees
        save_employees(updated_data)
        
        print("Employee deleted successfully.")
    else:
        print(f"No employee found with ID {identifier}.")
        messagebox.showwarning("Erorr", "Select an item first")


# Function to list all employees
def list_employees():
    employees = load_employees()
    if employees:
        print("\nCurrent Employee List:")
        for idx, employee in enumerate(employees, start=1):
            print(
                f"{idx}. Name: {employee['Name']}, Age: {employee['Age']}, ID: {employee['ID']}, Salary: {employee['Salary']}")
    else:
        print("No employees found.")
