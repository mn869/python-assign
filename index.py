#python-assign

# Simple Calculator Program

# Asking user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Asking user to choose an operation
operation = input("Enter an operation (+, -, *, /): ")

# Performing the operation based on user input
if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

elif operation == '/':
    if num2 != 0:  # Check for division by zero
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Invalid operation! Please choose +, -, *, or /.")

