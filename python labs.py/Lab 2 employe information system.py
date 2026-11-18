
name = input("Enter Employee Name: ")
emp_id = int(input("Enter Employee ID: "))
salary = float(input("Enter Salary: "))
department = input("Enter Department: ")

active = input("Is Employee Active? (yes/no): ").lower() == "yes"

print("\n--- Employee Record ---")
print("Name:", name)
print("ID:", emp_id)
print("Salary:", salary)
print("Department:", department)
print("Active:", active)
