"""
24_packing_unpacking.py

This file demonstrates packing and unpacking in Python.
This allows flexible handling of function arguments and sequence assignment.
"""

# UNPACKING TUPLES/LISTS
# Assign multiple values at once

x, y = (1, 2)
print(f"x={x}, y={y}")

a, b, c = [10, 20, 30]
print(f"a={a}, b={b}, c={c}")

# SWAPPING VARIABLES
a, b = 5, 10
a, b = b, a  # Swap without temp variable
print(f"\nSwapped: a={a}, b={b}")

# UNPACKING WITH ASTERISK
# * collects extra values into a list

numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(f"\nFirst: {first}, Middle: {middle}, Last: {last}")

# *ARGS IN FUNCTIONS
# Collect positional arguments into tuple

def sum_all(*args):
    """Sum all arguments."""
    return sum(args)

print(f"\nSum: {sum_all(1, 2, 3, 4, 5)}")

# **KWARGS IN FUNCTIONS
# Collect keyword arguments into dictionary

def print_info(**kwargs):
    """Print all keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="NYC")

# COMBINING *ARGS AND **KWARGS

def flexible_function(*args, **kwargs):
    print(f"\nArgs: {args}")
    print(f"Kwargs: {kwargs}")

flexible_function(1, 2, 3, name="Alice", age=30)

# UNPACKING WHEN CALLING FUNCTIONS

def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
result = add(*numbers)  # Unpack list as arguments
print(f"\nSum: {result}")

person = {"name": "Alice", "age": 30, "city": "NYC"}
def create_person(name, age, city):
    return f"{name}, {age}, {city}"

print(create_person(**person))  # Unpack dict as keyword arguments

