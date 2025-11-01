"""
02_variables_and_types.py

This file introduces variables and basic data types in Python.
Variables are used to store data that can be used later in your program.
"""

# VARIABLES
# Variables are created by assigning a value to a name using the = operator
# Python automatically determines the type based on the value assigned

# INTEGER (int) - whole numbers
age = 25
count = -10
print("Age:", age)
print("Type of age:", type(age))  # type() function shows the data type

# FLOAT (float) - decimal numbers
price = 19.99
temperature = -5.5
print("\nPrice:", price)
print("Type of price:", type(price))

# STRING (str) - text, enclosed in quotes (single or double)
name = "Alice"
greeting = 'Hello'
message = "Python is fun!"
print("\nName:", name)
print("Type of name:", type(name))

# BOOLEAN (bool) - True or False (must be capitalized)
is_student = True
is_active = False
print("\nIs student:", is_student)
print("Type of is_student:", type(is_student))

# VARIABLE REASSIGNMENT
# You can change the value of a variable
x = 5
print("\nInitial x:", x)
x = 10  # x now has a new value
print("Updated x:", x)

# Variables can even change types (Python is dynamically typed)
y = 5
print("\ny is an integer:", y, type(y))
y = "five"  # Now y is a string
print("y is now a string:", y, type(y))

# NAMING VARIABLES
# Good practices:
# - Use descriptive names (not just x, y, z)
# - Start with a letter or underscore
# - Can contain letters, numbers, and underscores
# - Case-sensitive (age != Age)
user_name = "Bob"
total_count = 100
_is_valid = True

