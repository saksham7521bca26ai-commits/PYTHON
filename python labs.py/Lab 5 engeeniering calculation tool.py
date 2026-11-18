
print("========================================================")
print("          ENGINEERING CALCULATION TOOL")
print("========================================================")

import math as f

value = float(input("Enter a numerical value: "))
exponent = float(input("Enter an exponent: "))
measurement = float(input("Enter a decimal measurement: "))

print("\n---------------- RESULTS ----------------")

# Mathematical calculations
power = f.pow(value, exponent)
absolute_value = abs(value)
rounded_value = round(measurement, 2)
ceil_value = f.ceil(measurement)
floor_value = f.floor(measurement)

print("Value           :", value)
print("Exponent        :", exponent)
print("Power           :", power)
print("Absolute Value  :", absolute_value)
print("Decimal Value   :", measurement)
print("Rounded Value   :", rounded_value)
print("Ceiling Value   :", ceil_value)
print("Floor Value     :", floor_value)

# Square root calculation
if value >= 0:
    square_root = f.sqrt(value)
    print("Square Root     :", square_root)
else:
    print("Square Root     : Not defined for negative values")

# Factorial calculation
if value >= 0 and value.is_integer():
    factorial = f.factorial(int(value))
    print("Factorial       :", factorial)
else:
    print("Factorial       : Requires a non-negative integer")

print("========================================================")
