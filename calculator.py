print("Simple Calculator")
print("Operations: +, -, *, /, %, **")

# Taking inputs
num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

# Using if-else
if op == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif op == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif op == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

elif op == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")

elif op == '%':
    result = num1 % num2
    print(f"{num1} % {num2} = {result}")

elif op == '**':
    result = num1 ** num2
    print(f"{num1} ** {num2} = {result}")

else:
    print("Invalid operator!")
