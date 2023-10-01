# Question:
# Define a function called is_even that takes an integer as input and returns True if the number is even, and False otherwise.

def is_even(number):
    """Input: Integer
       Output: Returns True if the number is even"""

    if number % 2 == 0:
        return True
    else:
        return False


query_number = int(input('Enter a number'))
print(is_even(query_number))