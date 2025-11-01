"""
12_list_comprehensions.py

This file demonstrates list comprehensions in Python.
List comprehensions provide a concise way to create lists.
They're more readable and often faster than traditional loops.
"""

# BASIC LIST COMPREHENSION
# Syntax: [expression for item in iterable]

# Traditional way (verbose)
squares_traditional = []
for x in range(1, 6):
    squares_traditional.append(x**2)
print(f"Traditional: {squares_traditional}")

# List comprehension (concise)
squares = [x**2 for x in range(1, 6)]
print(f"Comprehension: {squares}")

# LIST COMPREHENSION WITH CONDITIONS

# Filter with condition
# Syntax: [expression for item in iterable if condition]

# Traditional way
evens_traditional = []
for x in range(1, 11):
    if x % 2 == 0:
        evens_traditional.append(x)
print(f"\nTraditional evens: {evens_traditional}")

# List comprehension
evens = [x for x in range(1, 11) if x % 2 == 0]
print(f"Comprehension evens: {evens}")

# CONDITIONAL EXPRESSION IN LIST COMPREHENSION
# Apply different expressions based on condition

# If-else in expression
numbers = [1, 2, 3, 4, 5]
result = [x * 2 if x % 2 == 0 else x * 3 for x in numbers]
print(f"\nConditional expression: {result}")
# Explanation: double even numbers, triple odd numbers

# MULTIPLE ITERABLES
# Using multiple for clauses

# Cartesian product (combinations)
pairs = [(x, y) for x in [1, 2, 3] for y in ['a', 'b']]
print(f"\nPairs: {pairs}")

# Equivalent nested loops:
# pairs = []
# for x in [1, 2, 3]:
#     for y in ['a', 'b']:
#         pairs.append((x, y))

# FLATTENING A LIST
# Convert nested list to flat list

nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flat = [item for sublist in nested for item in sublist]
print(f"\nNested: {nested}")
print(f"Flattened: {flat}")

# WORKING WITH STRINGS

# Split and process
words = ["hello", "world", "python", "programming"]
lengths = [len(word) for word in words]
print(f"\nWord lengths: {lengths}")

# Filter words
long_words = [word for word in words if len(word) > 5]
print(f"Long words: {long_words}")

# Transform strings
uppercased = [word.upper() for word in words]
print(f"Uppercased: {uppercased}")

# DICTIONARY COMPREHENSIONS
# Similar syntax but creates dictionaries

# Basic dictionary comprehension
squares_dict = {x: x**2 for x in range(1, 6)}
print(f"\nSquares dict: {squares_dict}")

# With condition
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Even squares dict: {even_squares}")

# Transform existing dictionary
original = {"a": 1, "b": 2, "c": 3}
doubled = {k: v * 2 for k, v in original.items()}
print(f"Doubled values: {doubled}")

# Filter dictionary
filtered = {k: v for k, v in original.items() if v > 1}
print(f"Filtered dict: {filtered}")

# SET COMPREHENSIONS
# Creates sets (unique elements)

squares_set = {x**2 for x in range(1, 6)}
print(f"\nSquares set: {squares_set}")

# Filter set
even_set = {x for x in range(1, 11) if x % 2 == 0}
print(f"Even set: {even_set}")

# NESTED LIST COMPREHENSIONS
# Create nested structures

matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(f"\nMatrix: {matrix}")

# PRACTICAL EXAMPLES

# Extract numbers from string
text = "I have 3 cats and 2 dogs"
numbers = [int(char) for char in text if char.isdigit()]
print(f"\nNumbers from text: {numbers}")

# Filter and transform list
temperatures = [22, 25, 18, 30, 15, 28]
warm = [t for t in temperatures if t > 20]
print(f"Warm temperatures: {warm}")

# Process file extensions (simulated)
files = ["document.pdf", "image.jpg", "video.mp4", "data.txt"]
extensions = [f.split(".")[-1] for f in files]
print(f"Extensions: {extensions}")

# WHEN TO USE COMPREHENSIONS
# Use when:
# - The operation is simple and readable
# - You're creating a new list/dict/set
# - The logic is straightforward

# Avoid when:
# - The logic is complex (use regular loops)
# - You need side effects (use regular loops)
# - Readability suffers

# Complex example (might be better as regular loop)
data = [1, 2, 3, 4, 5]
result = [x**2 if x % 2 == 0 else x**3 for x in data if x > 1]
print(f"\nComplex comprehension: {result}")
# This could be more readable as:
# result = []
# for x in data:
#     if x > 1:
#         if x % 2 == 0:
#             result.append(x**2)
#         else:
#             result.append(x**3)

