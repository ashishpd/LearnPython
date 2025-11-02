"""
03_basic_operations.py

This file demonstrates basic operations in Python:
- Arithmetic operations
- String operations
- Type conversions
"""

# ARITHMETIC OPERATIONS
# Python supports standard mathematical operations

# Addition
result = 5 + 3
print("5 + 3 =", result)  # Output: 5 + 3 = 8

# Subtraction
result = 10 - 4
print("10 - 4 =", result)  # Output: 10 - 4 = 6

# Multiplication
result = 6 * 7
print("6 * 7 =", result)  # Output: 6 * 7 = 42

# Division (always returns a float)
result = 15 / 3
print("15 / 3 =", result)  # Output: 15 / 3 = 5.0
print("Type:", type(result))  # Output: Type: <class 'float'>

# Integer Division (floor division) - rounds down to nearest integer
result = 17 // 5
print("17 // 5 =", result)  # Output: 17 // 5 = 3  # Returns 3, not 3.4

# Modulo (remainder after division)
result = 17 % 5
print("17 % 5 =", result)  # Output: 17 % 5 = 2  # Returns 2 (the remainder)

# Exponentiation (power)
result = 2 ** 3
print("2 ** 3 =", result)  # Output: 2 ** 3 = 8  # 2 to the power of 3 = 8

# ORDER OF OPERATIONS (PEMDAS)
result = 2 + 3 * 4
print("\n2 + 3 * 4 =", result)  # Output: 2 + 3 * 4 = 14  # Multiplication happens first = 14

result = (2 + 3) * 4
print("(2 + 3) * 4 =", result)  # Output: (2 + 3) * 4 = 20  # Parentheses override = 20

# STRING OPERATIONS

# String concatenation (joining strings)
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print("\nFull name:", full_name)  # Output: Full name: John Doe

# String repetition (multiplying strings)
greeting = "Hello! " * 3
print("Repeated greeting:", greeting)  # Output: Repeated greeting: Hello! Hello! Hello!

# STRING AND NUMBER OPERATIONS
# You cannot directly add strings and numbers - you need to convert
age = 25
# This would cause an error: message = "I am " + age + " years old"

# Solution 1: Convert number to string using str()
message = "I am " + str(age) + " years old"
print("\nMessage:", message)  # Output: Message: I am 25 years old

# Solution 2: Use f-strings (formatted string literals) - Python 3.6+
message = f"I am {age} years old"
print("Message (f-string):", message)  # Output: Message (f-string): I am 25 years old

# TYPE CONVERSIONS
# Converting between different data types

# str() - converts to string
number = 42
number_str = str(number)
print("\nNumber as string:", number_str, "Type:", type(number_str))  # Output: Number as string: 42 Type: <class 'str'>

# int() - converts to integer (rounds down)
float_num = 3.7
int_num = int(float_num)
print("3.7 as integer:", int_num)  # Output: 3.7 as integer: 3

# float() - converts to float
int_num = 5
float_num = float(int_num)
print("5 as float:", float_num)  # Output: 5 as float: 5.0

# Note: Converting strings to numbers
# int("5") works, but int("5.5") doesn't - use float() first
string_num = "42"
converted = int(string_num)
print("'42' as integer:", converted)  # Output: '42' as integer: 42

string_num = "3.14"
converted = float(string_num)
print("'3.14' as float:", converted)  # Output: '3.14' as float: 3.14

