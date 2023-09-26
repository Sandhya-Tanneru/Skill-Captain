age = int(input("Enter your age: "))

if age < 18:
    print("You are a minor.")
elif 65 >= age >= 18:
    print("You are an adult.")
elif age > 65:
    print("You are a senior citizen.")
