"""
02a_fstrings.py

This file demonstrates f-strings (formatted string literals) in Python.
F-strings were introduced in Python 3.6 and provide a modern, readable way
to format strings by embedding expressions inside string literals.

F-strings are prefixed with 'f' or 'F' and use curly braces {} to embed expressions.
"""

# BASIC F-STRING SYNTAX

name = "Alice"
age = 30

# Simple variable interpolation
message = f"My name is {name} and I'm {age} years old."
print(message)  # Output: My name is Alice and I'm 30 years old.

# You can use expressions inside f-strings
print(f"Next year I'll be {age + 1}")  # Output: Next year I'll be 31
print(f"Name length: {len(name)}")  # Output: Name length: 5

# Different data types work automatically
price = 19.99
quantity = 3
print(f"Total: ${price * quantity}")  # Output: Total: $59.97

# BOOLEANS
is_active = True
print(f"User active: {is_active}")  # Output: User active: True

# NUMBER FORMATTING

pi = 3.14159265359

# Decimal places - use :.Nf where N is number of decimal places
print(f"Pi to 2 decimals: {pi:.2f}")  # Output: Pi to 2 decimals: 3.14
print(f"Pi to 4 decimals: {pi:.4f}")  # Output: Pi to 4 decimals: 3.1416

# Width and alignment - use :N for minimum width
number = 42
print(f"Number: {number:5}")  # Output: Number:    42 (right-aligned, width 5)
print(f"Number: {number:05}")  # Output: Number: 00042 (zero-padded, width 5)

# Combined width and decimal places
print(f"Price: ${price:10.2f}")  # Output: Price: $     19.99 (width 10, 2 decimals)

# Left alignment with <
print(f"Left: {number:<5}")  # Output: Left: 42    (left-aligned, width 5)

# Center alignment with ^
print(f"Center: {number:^5}")  # Output: Center:  42   (centered, width 5)

# Right alignment with > (default for numbers)
print(f"Right: {number:>5}")  # Output: Right:    42 (right-aligned, width 5)

# Formatting with padding characters
print(f"Number: {number:*>5}")  # Output: Number: ***42 (padded with *)
print(f"Number: {number:*<5}")  # Output: Number: 42*** (padded with *)
print(f"Number: {number:*^7}")  # Output: Number: **42*** (centered with *)

# INTEGERS WITH FORMATTING

# Different number bases
num = 42
print(f"Decimal: {num}")  # Output: Decimal: 42
print(f"Binary: {num:b}")  # Output: Binary: 101010
print(f"Octal: {num:o}")  # Output: Octal: 52
print(f"Hexadecimal: {num:x}")  # Output: Hexadecimal: 2a
print(f"Hexadecimal (uppercase): {num:X}")  # Output: Hexadecimal (uppercase): 2A

# Percentage formatting
ratio = 0.85
print(f"Success rate: {ratio:.1%}")  # Output: Success rate: 85.0%
print(f"Success rate: {ratio:.0%}")  # Output: Success rate: 85%

# Scientific notation
big_num = 1234567.89
print(f"Scientific: {big_num:.2e}")  # Output: Scientific: 1.23e+06
print(f"Scientific (uppercase): {big_num:.2E}")  # Output: Scientific (uppercase): 1.23E+06

# Thousands separator
large_number = 1234567
print(f"With commas: {large_number:,}")  # Output: With commas: 1,234,567

# STRING FORMATTING

text = "hello"
print(f"Uppercase: {text.upper()}")  # Output: Uppercase: HELLO
print(f"Capitalized: {text.capitalize()}")  # Output: Capitalized: Hello

# Truncating strings
long_text = "This is a very long string"
print(f"First 10 chars: {long_text[:10]}")  # Output: First 10 chars: This is a

# STRING EXPRESSIONS AND METHODS

# Calling methods directly in f-strings
print(f"Length of '{text}': {len(text)}")  # Output: Length of 'hello': 5
print(f"Uppercase version: {text.upper()}")  # Output: Uppercase version: HELLO

# Dictionary access
person = {"name": "Bob", "age": 25}
print(f"Name: {person['name']}, Age: {person['age']}")  # Output: Name: Bob, Age: 25

# List indexing
items = ["apple", "banana", "cherry"]
print(f"First item: {items[0]}")  # Output: First item: apple
print(f"Total items: {len(items)}")  # Output: Total items: 3

# CONDITIONAL EXPRESSIONS IN F-STRINGS

score = 85
print(f"Grade: {'Pass' if score >= 70 else 'Fail'}")  # Output: Grade: Pass

temperature = 25
print(f"Status: {'Hot' if temperature > 20 else 'Cold'}")  # Output: Status: Hot

# DATE AND TIME FORMATTING (requires datetime)

from datetime import datetime

now = datetime.now()
print(f"Current date: {now:%Y-%m-%d}")  # Output: Current date: 2024-01-15 (example)
print(f"Current time: {now:%H:%M:%S}")  # Output: Current time: 14:30:45 (example)
print(f"Full datetime: {now:%Y-%m-%d %H:%M:%S}")  # Output: Full datetime: 2024-01-15 14:30:45

# NESTED F-STRINGS AND QUOTES

# Using different quote types
print(f'Name: {name}')  # Single quotes work too
print(f"Name: {name}")  # Double quotes
print(f"""Multi-line
f-string with {name}""")  # Triple quotes for multi-line

# Escaping curly braces
print(f"{{literal braces}} and variable: {name}")  # Output: {literal braces} and variable: Alice

# To show a single curly brace, double it
print(f"Single brace: {{")  # Output: Single brace: {
print(f"Both braces: {{ and }}")  # Output: Both braces: { and }

# MULTILINE F-STRINGS

# You can break f-strings across multiple lines
first_name = "John"
last_name = "Doe"
full_name = f"{first_name} {last_name}"
print(f"Full name: {full_name}")

# Or use parentheses for implicit line continuation
message = (
    f"Name: {first_name}\n"
    f"Last: {last_name}\n"
    f"Full: {full_name}"
)
print(message)

# ADVANCED: FORMAT SPECIFIERS WITH ALIGNMENT

# Format specifier syntax: [fill][align][width][.precision][type]
items = [
    ("Apple", 1.99),
    ("Banana", 0.99),
    ("Cherry", 2.49)
]

print("\nShopping List:")
for item, price in items:
    print(f"{item:10} ${price:6.2f}")  # Output: Item name (width 10), price (width 6, 2 decimals)
# Output:
# Apple      $  1.99
# Banana     $  0.99
# Cherry     $  2.49

# REAL-WORLD EXAMPLES

# User greeting
username = "alice"
score = 95
print(f"Welcome, {username.capitalize()}! Your score: {score}/100")

# Receipt formatting
item = "Coffee"
qty = 2
unit_price = 4.50
total = qty * unit_price
print(f"\nReceipt:")
print(f"Item: {item}")
print(f"Quantity: {qty}")
print(f"Unit Price: ${unit_price:.2f}")
print(f"Total: ${total:.2f}")

# Status message
status = "active"
count = 42
print(f"Status: {status.upper()} | Count: {count:03d}")  # Output: Status: ACTIVE | Count: 042

# COMPARISON: F-STRINGS vs OTHER METHODS

# Old way 1: String concatenation
old_way1 = "Name: " + name + ", Age: " + str(age)  # Output: Name: Alice, Age: 30
print(f"Old way (concat): {old_way1}")

# Old way 2: .format()
old_way2 = "Name: {}, Age: {}".format(name, age)  # Output: Name: Alice, Age: 30
print(f"Old way (.format): {old_way2}")

# Modern way: f-string (preferred)
modern_way = f"Name: {name}, Age: {age}"  # Output: Name: Alice, Age: 30
print(f"Modern way (f-string): {modern_way}")

# F-strings are faster and more readable!

