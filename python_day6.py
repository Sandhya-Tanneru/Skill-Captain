# Question:
# Write a program that takes two numbers as input from the user and performs division.
# Handle the potential division by zero error.

# Taking inputs from the user.
input_1 = int(input("Enter the Dividend"))
input_2 = int(input("Enter the Divisor"))

try:
    print(input_1/input_2)
except ZeroDivisionError as e:
    pass
