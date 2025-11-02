"""
01_hello_world.py

This is the simplest Python program - the classic "Hello, World!" example.
It demonstrates how to use the print() function to display output.

Note: print() can take any number of parameters with different types (strings, integers,
floats, booleans, etc.), and they will be converted to strings and separated by spaces.
"""

# The print() function outputs text to the console/terminal
print("Hello, World!")  # Output: Hello, World!

# You can print multiple items - they'll be separated by spaces by default
print("Hello,", "Python!")  # Output: Hello, Python!

# You can print numbers directly
print(42)  # Output: 42

# You can combine text and numbers
print("The answer is:", 42)  # Output: The answer is: 42

# You can print floats and mix different types
print("Price:", 19.99, "USD")  # Output: Price: 19.99 USD

# Concatenation with + operator - NOTE: You CANNOT directly concatenate string and number
# print("Number: " + 42)  # This would cause TypeError: can only concatenate str to str

# To concatenate, you must convert the number to a string first
print("Number: " + str(42))  # Output: Number: 42
print("Price: $" + str(19.99))  # Output: Price: $19.99

# Or use f-strings (modern Python way, recommended)
print(f"The answer is: {42}")  # Output: The answer is: 42
print(f"Price: ${19.99} USD")  # Output: Price: $19.99 USD

