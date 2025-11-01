"""
04_user_input.py

This file demonstrates how to get input from the user using the input() function.
The input() function always returns a string, so we often need to convert it.
"""

# BASIC INPUT
# The input() function displays a prompt and waits for user input
# It always returns a string, even if the user types a number

name = input("Enter your name: ")
print(f"Hello, {name}!")

# Note: When running this in a script, the program will pause and wait
# for the user to type something and press Enter

# INPUT ALWAYS RETURNS A STRING
# Even if the user types a number, input() returns it as a string
age_string = input("\nEnter your age: ")
print(f"You entered: {age_string}")
print(f"Type: {type(age_string)}")

# To use it as a number, we need to convert it
age_int = int(age_string)
print(f"Age as integer: {age_int}")
print(f"Type: {type(age_int)}")

# CONVERTING INPUT TO DIFFERENT TYPES
# Get a number from the user
print("\n" + "="*50)
number_str = input("Enter a number: ")
number = int(number_str)  # Convert string to integer
doubled = number * 2
print(f"Double of {number} is {doubled}")

# Get a float from the user
print("\n" + "="*50)
price_str = input("Enter a price: ")
price = float(price_str)  # Convert string to float
total = price * 1.1  # Add 10% tax
print(f"Price with tax: ${total:.2f}")

# MULTIPLE INPUTS
# You can get multiple inputs sequentially
print("\n" + "="*50)
first = input("Enter first number: ")
second = input("Enter second number: ")
sum_result = int(first) + int(second)
print(f"{first} + {second} = {sum_result}")

# HANDLING ERRORS (preview - we'll cover this in detail later)
# If the user enters something that can't be converted, you'll get an error
# For example, trying to convert "hello" to an integer would fail
# We'll learn how to handle this in the error handling lesson

print("\n" + "="*50)
print("Note: In real programs, you should validate user input")
print("to ensure they enter the expected type of data.")

