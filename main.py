print("""Welcome to my first code of 2024!
            IT IS A BASIC CALCULATOR""")
first_number = int(input("Enter first number: "))
operand = input("Enter operand: ")
second_number = int(input("Enter second number: "))

if operand == "+":
    result = first_number + second_number
    print(f"Result: {result}")
elif operand == "-":
    result = first_number - second_number
    print(f"Result: {result}")
elif operand == "*":
    result = first_number * second_number
    print(f"Result: {result}")
elif operand == "/":
    result = first_number / second_number
    print(f"Result: {result}")
else:
    print("Kindly input a valid operand; either +, -, * or /")
