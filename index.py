#Basic calculator

#asking user to input two numbers
num1 = float(input("Enter First number: "))
num2 = float(input("Enter second number: "))

#asking user to choose operation
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero!"
else:
    result = "Invalid operation"

print(f"Result: {result}")