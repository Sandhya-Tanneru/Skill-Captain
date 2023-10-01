# Question:
# Create a Python program that performs the following operations on a given dictionary:
# Add a new key-value pair to the dictionary.
# Remove a specific key-value pair from the dictionary.
# Update the value of a specific key in the dictionary.
# Check if a key exists in the dictionary.
# Print all the keys in the dictionary.


def add_key_value_pair(key, value, dictionary):
    dictionary[key] = value
    return dictionary


def delete_key_value_pair(key, dictionary):
    del dictionary[key]
    return dictionary


def update_key_value_pair(key, value, dictionary):
    dictionary[key] = value
    return dictionary


def is_key(dictionary, key):
    if key in dictionary.keys():
        return True
    else:
        return False


def print_all_keys(dictionary):
    print(dictionary.keys())


dictionary_sample = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}


dictionary_sample = add_key_value_pair("F", 6, dictionary_sample)
print(dictionary_sample)

dictionary_sample = delete_key_value_pair("C", dictionary_sample)
print(dictionary_sample)

dictionary_sample = update_key_value_pair("D", 26, dictionary_sample)
print(dictionary_sample)

print(is_key(dictionary_sample, 'C'), is_key(dictionary_sample, 'A'))

print_all_keys(dictionary_sample)