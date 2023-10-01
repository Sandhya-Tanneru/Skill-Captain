# Question:
# Create a Python program that converts a list into a set and vice versa.

def convert_list_to_set(query_list):
    """Converts a list to set"""
    return set(query_list)


def convert_set_to_list(query_set):
    """Converts a set to list"""
    return list(query_set)


# Defining a list with some arbitrary elements
number_list = [1, 3, 4, 5, 7, 8, 5, 3]

converted_set = convert_list_to_set(number_list)
converted_list = convert_set_to_list(converted_set)

print("Converted set: ", converted_set)
print("Converted list: ", converted_list)

