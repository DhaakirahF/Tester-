#code calculator tester
equation = input('Enter an equation (e.g., 2 + 3): ')
parts = equation.split()

if len(parts) == 3:
    num1 = float(parts[0])
    operator = parts[1]
    num2 = float(parts[2])

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    else:
        result = "Invalid operator"

    print(f"The result is: {result}")
else:
    print("Invalid equation format. Please enter in the format: number operator number")










