"""
07_functions.py

This file demonstrates functions in Python.
Functions are reusable blocks of code that perform a specific task.
They help organize code, avoid repetition, and make programs easier to understand.
"""

# DEFINING A FUNCTION
# Functions are defined using the 'def' keyword

def greet():
    """This is a docstring - it describes what the function does."""
    print("Hello, World!")  # Output: Hello, World!

# CALLING A FUNCTION
greet()

# FUNCTIONS WITH PARAMETERS
# Parameters are variables that receive values when the function is called

def greet_person(name):
    """Greets a specific person by name."""
    print(f"Hello, {name}!")  # Output: Hello, Alice! (or Hello, Bob!)

greet_person("Alice")
greet_person("Bob")

# FUNCTIONS WITH MULTIPLE PARAMETERS
def introduce(name, age):
    """Introduces someone with their name and age."""
    print(f"My name is {name} and I'm {age} years old.")  # Output: My name is Charlie and I'm 25 years old.

introduce("Charlie", 25)

# FUNCTIONS WITH RETURN VALUES
# The return statement sends a value back to the caller

def add(a, b):
    """Adds two numbers and returns the result."""
    result = a + b
    return result

sum_result = add(5, 3)
print(f"\n5 + 3 = {sum_result}")  # Output: 5 + 3 = 8

# You can return multiple values (as a tuple)
def get_name_and_age():
    """Returns multiple values."""
    name = "David"
    age = 30
    return name, age

name, age = get_name_and_age()
print(f"\nName: {name}, Age: {age}")  # Output: Name: David, Age: 30

# DEFAULT PARAMETERS
# Parameters can have default values

def greet_with_title(name, title="Mr"):
    """Greets someone with an optional title."""
    print(f"Hello, {title} {name}!")  # Output varies based on call

greet_with_title("Smith")  # Uses default title "Mr"  # Output: Hello, Mr Smith!
greet_with_title("Jones", "Dr")  # Overrides default with "Dr"  # Output: Hello, Dr Jones!
greet_with_title("Williams", "Ms")  # Overrides default with "Ms"  # Output: Hello, Ms Williams!

# KEYWORD ARGUMENTS
# You can specify parameters by name when calling the function

def create_profile(name, age, city, country):
    """Creates a user profile."""
    print(f"Profile: {name}, {age} years old, from {city}, {country}")  # Output varies based on call

# Call with positional arguments (order matters)
create_profile("Alice", 25, "New York", "USA")  # Output: Profile: Alice, 25 years old, from New York, USA

# Call with keyword arguments (order doesn't matter)
create_profile(age=30, name="Bob", country="Canada", city="Toronto")  # Output: Profile: Bob, 30 years old, from Toronto, Canada

# Mix positional and keyword arguments (positional must come first)
create_profile("Charlie", age=28, country="UK", city="London")  # Output: Profile: Charlie, 28 years old, from London, UK

# SCOPE - LOCAL VS GLOBAL VARIABLES

global_var = "I'm global"  # Global variable

def demonstrate_scope():
    """Demonstrates variable scope."""
    local_var = "I'm local"  # Local variable (only exists in this function)
    print(f"Inside function: {local_var}")  # Output: Inside function: I'm local
    print(f"Inside function: {global_var}")  # Output: Inside function: I'm global  # Can access global variables

demonstrate_scope()
# print(local_var)  # This would cause an error - local_var doesn't exist outside

# FUNCTION AS FIRST-CLASS OBJECTS
# Functions can be assigned to variables and passed around

def say_hello():
    return "Hello!"

def say_goodbye():
    return "Goodbye!"

# Assign function to variable
greeting_func = say_hello
print(f"\n{greeting_func()}")  # Output: Hello!

# Pass function as argument
def call_function(func):
    """Calls the function passed to it."""
    return func()

print(call_function(say_hello))  # Output: Hello!
print(call_function(say_goodbye))  # Output: Goodbye!

# NESTED FUNCTIONS
# Functions can be defined inside other functions

def outer_function(x):
    """Outer function that contains an inner function."""
    def inner_function(y):
        return y * 2
    
    return inner_function(x)

result = outer_function(5)
print(f"\nOuter function result: {result}")  # Output: Outer function result: 10

