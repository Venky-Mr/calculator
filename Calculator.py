import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def exponentiation(a, b):
    return a ** b


def division(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a/b


def modulo(a, b):
    if b == 0:
        return "Error: Modulo by zero"
    return a % b


def square_root(a):
    if a < 0:
        return "Error: cannot calculate square root of a negative number "
    return math.sqrt(a)


while True:
    print("""
    _-_-_- Wel come to my text based calculator app _-_-_-
    **** Here you can do some basic arithmetic operations ****
    **** Here's is the list of operators that you can use to do ****
                "+", "-", "/", "**", "sqrt", "*", "%", "
    
    """)
    result = None
    try:

        first_number = float(input("Enter first number: "))
        operator = input("Select the operator: ").strip().lower()
        if operator not in ["+", "-", "/", "**", "sqrt", "*", "%"]:
            raise ValueError("Invalid operator")
        if operator == "sqrt":
            result = square_root(first_number)
        else:
            second_number = float(input("Enter second number: "))
            if operator == "+":
                result = add(first_number, second_number)
            elif operator == "-":
                result = subtract(first_number, second_number)
            elif operator == "/":
                result = division(first_number, second_number)
            elif operator == "**":
                result = exponentiation(first_number, second_number)
            elif operator == "%":
                result = modulo(first_number, second_number)
            elif operator == "*":
                result = multiply(first_number, second_number)
        print("Result: ", result)
    except ValueError as e:
        print(f"Error: {e}")
        repeat = input("Do you wan to perform another calculation? (yes/no): ").strip().lower()
        if repeat != "yes":
            break


