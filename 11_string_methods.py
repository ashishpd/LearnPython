"""
11_string_methods.py

This file demonstrates common string methods in Python.
Strings have many built-in methods for manipulation, searching, and formatting.
"""

# CREATING STRINGS
text = "Hello, World!"
print(f"Original text: {text}")

# CASE METHODS

# upper() - converts to uppercase
print(f"\nupper(): {text.upper()}")

# lower() - converts to lowercase
print(f"lower(): {text.lower()}")

# capitalize() - first letter uppercase, rest lowercase
sentence = "hello world"
print(f"capitalize(): {sentence.capitalize()}")

# title() - first letter of each word uppercase
print(f"title(): {sentence.title()}")

# swapcase() - swaps case of all letters
mixed = "HeLLo WoRLd"
print(f"swapcase(): {mixed.swapcase()}")

# STRIPPING WHITESPACE

# strip() - removes whitespace from both ends
text = "  Hello, World!  "
print(f"\nOriginal: '{text}'")
print(f"strip(): '{text.strip()}'")

# lstrip() - removes whitespace from left
print(f"lstrip(): '{text.lstrip()}'")

# rstrip() - removes whitespace from right
print(f"rstrip(): '{text.rstrip()}'")

# FINDING AND REPLACING

text = "Hello, World! Hello!"

# find() - finds first occurrence (returns index or -1)
index = text.find("Hello")
print(f"\nfind('Hello'): {index}")

# rfind() - finds last occurrence
last_index = text.rfind("Hello")
print(f"rfind('Hello'): {last_index}")

# index() - similar to find(), but raises error if not found
index = text.index("World")
print(f"index('World'): {index}")

# count() - counts occurrences
count = text.count("Hello")
print(f"count('Hello'): {count}")

# replace() - replaces occurrences
new_text = text.replace("Hello", "Hi")
print(f"replace('Hello', 'Hi'): {new_text}")

# Replace with count limit
limited = text.replace("Hello", "Hi", 1)  # Replace only first occurrence
print(f"replace('Hello', 'Hi', 1): {limited}")

# CHECKING STRING PROPERTIES

# startswith() - checks if string starts with substring
text = "Hello, World!"
print(f"\nstartswith('Hello'): {text.startswith('Hello')}")
print(f"startswith('World'): {text.startswith('World')}")

# endswith() - checks if string ends with substring
print(f"endswith('!'): {text.endswith('!')}")
print(f"endswith('World'): {text.endswith('World')}")

# isdigit() - checks if all characters are digits
print(f"\n'123'.isdigit(): {'123'.isdigit()}")
print(f"'12a'.isdigit(): {'12a'.isdigit()}")

# isalpha() - checks if all characters are letters
print(f"'abc'.isalpha(): {'abc'.isalpha()}")
print(f"'abc123'.isalpha(): {'abc123'.isalpha()}")

# isalnum() - checks if all characters are alphanumeric
print(f"'abc123'.isalnum(): {'abc123'.isalnum()}")
print(f"'abc 123'.isalnum(): {'abc 123'.isalnum()}")

# isspace() - checks if all characters are whitespace
print(f"'   '.isspace(): {'   '.isspace()}")
print(f"'abc'.isspace(): {'abc'.isspace()}")

# SPLITTING AND JOINING

# split() - splits string into list
text = "apple,banana,cherry"
fruits = text.split(",")
print(f"\nsplit(','): {fruits}")

# split() with max splits
text = "one two three four"
words = text.split(" ", 2)  # Split into max 3 parts
print(f"split(' ', 2): {words}")

# splitlines() - splits by line breaks
lines = "Line 1\nLine 2\nLine 3".splitlines()
print(f"splitlines(): {lines}")

# join() - joins list elements into string
fruits = ["apple", "banana", "cherry"]
joined = ", ".join(fruits)
print(f"\njoin(', '): {joined}")

words = ["Hello", "World"]
sentence = " ".join(words)
print(f"join(' '): {sentence}")

# PADDING AND ALIGNMENT

text = "Hello"

# center() - centers string in specified width
print(f"\ncenter(15): '{text.center(15)}'")
print(f"center(15, '-'): '{text.center(15, '-')}'")

# ljust() - left-justifies string
print(f"ljust(10): '{text.ljust(10)}'")
print(f"ljust(10, '-'): '{text.ljust(10, '-')}'")

# rjust() - right-justifies string
print(f"rjust(10): '{text.rjust(10)}'")
print(f"rjust(10, '0'): '{text.rjust(10, '0')}'")

# zfill() - pads with zeros on the left
number = "42"
print(f"zfill(5): '{number.zfill(5)}'")

# STRING FORMATTING

# Old style: .format()
name = "Alice"
age = 30
message = "My name is {} and I'm {} years old.".format(name, age)
print(f"\n.format(): {message}")

# With named placeholders
message = "My name is {name} and I'm {age} years old.".format(name=name, age=age)
print(f".format(named): {message}")

# f-strings (formatted string literals) - Python 3.6+
message = f"My name is {name} and I'm {age} years old."
print(f"f-string: {message}")

# Formatting numbers in f-strings
pi = 3.14159
print(f"pi = {pi:.2f}")  # 2 decimal places
print(f"pi = {pi:10.2f}")  # 2 decimal places, width 10

number = 42
print(f"number = {number:05d}")  # Zero-padded, 5 digits

# MULTILINE STRINGS

# Triple quotes for multiline
multiline = """Line 1
Line 2
Line 3"""
print(f"\nMultiline string:\n{multiline}")

# Escape sequences
escaped = "This is a \"quote\" and this is a newline:\nSee?"
print(f"\nEscaped string:\n{escaped}")

# RAW STRINGS (r prefix)
# Useful for regex patterns or file paths
raw_string = r"C:\Users\Name\Documents"  # Backslashes not escaped
print(f"\nRaw string: {raw_string}")

# STRING REPETITION AND CONCATENATION
greeting = "Hello! " * 3
print(f"\nRepetition: {greeting}")

full_name = "John" + " " + "Doe"
print(f"Concatenation: {full_name}")

