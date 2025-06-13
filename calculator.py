operator = input("Enter an operator (+ - * /): ")
number_1 = float(input("Enter the 1st number: "))
number_2 = float(input("Enter the 2nd number: "))

if operator == "+":
    result = number_1 + number_2
    print(round(result, 3))
elif operator == "-":
    result = number_1 - number_2
    print(round(result, 3))
elif operator == "*":
    result = number_1 * number_2
    print(round(result, 3))
elif operator == "/":
    result = number_1 / number_2
    print(round(result, 3))
else:
    print(f"{operator} is not a valid operator")
