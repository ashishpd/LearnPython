"""
21_generators.py

This file demonstrates generators in Python.
Generators are functions that return iterators using the yield keyword.
They're memory-efficient for processing large datasets.
"""

# BASIC GENERATOR FUNCTION
# Uses 'yield' instead of 'return'

def simple_generator():
    """A simple generator that yields values."""
    yield 1
    yield 2
    yield 3

gen = simple_generator()
print("Generator values:")
for value in gen:
    print(value)

# GENERATOR VS REGULAR FUNCTION
# Regular function returns all values at once
def get_squares(n):
    """Regular function - returns list."""
    result = []
    for i in range(n):
        result.append(i ** 2)
    return result

# Generator function - yields one at a time
def get_squares_gen(n):
    """Generator function - yields one at a time."""
    for i in range(n):
        yield i ** 2

print("\nRegular function (all at once):", get_squares(5))
print("Generator (lazy evaluation):")
for square in get_squares_gen(5):
    print(f"  {square}")

# MEMORY EFFICIENCY
# Generators use less memory - generate values on demand

import sys

# Regular list - stores all values in memory
numbers_list = [x**2 for x in range(1000)]
print(f"\nList size: {sys.getsizeof(numbers_list)} bytes")

# Generator - generates on demand
numbers_gen = (x**2 for x in range(1000))
print(f"Generator size: {sys.getsizeof(numbers_gen)} bytes")

# GENERATOR EXPRESSIONS
# Similar to list comprehensions, but with parentheses

# List comprehension (creates list)
squares_list = [x**2 for x in range(5)]
print(f"\nList: {squares_list}")

# Generator expression (creates generator)
squares_gen = (x**2 for x in range(5))
print(f"Generator: {list(squares_gen)}")

# INFINITE GENERATOR
# Generators can generate infinite sequences

def infinite_counter():
    """Generator that counts forever."""
    count = 0
    while True:
        yield count
        count += 1

# Use with caution - only iterate a limited number of times!
counter = infinite_counter()
print("\nFirst 5 values from infinite generator:")
for i in range(5):
    print(f"  {next(counter)}")

# GENERATOR WITH NEXT()
# Manually get next value from generator

def number_generator():
    yield 10
    yield 20
    yield 30

gen = number_generator()
print(f"\nFirst: {next(gen)}")
print(f"Second: {next(gen)}")
print(f"Third: {next(gen)}")
# print(next(gen))  # Would raise StopIteration

# SENDING VALUES TO GENERATOR
# Use .send() to send values back to generator

def echo_generator():
    """Generator that echoes values sent to it."""
    while True:
        value = yield
        print(f"Received: {value}")

gen = echo_generator()
next(gen)  # Initialize generator
gen.send("Hello")
gen.send("World")

# PRACTICAL EXAMPLE: Processing Large Files

def read_large_file(filepath):
    """Generator to read large file line by line."""
    with open(filepath, 'r') as file:
        for line in file:
            yield line.strip()

# Usage:
# for line in read_large_file("large_file.txt"):
#     process(line)

# GENERATOR PIPELINE
# Chain generators together

def numbers(n):
    for i in range(n):
        yield i

def squares(seq):
    for i in seq:
        yield i ** 2

def evens(seq):
    for i in seq:
        if i % 2 == 0:
            yield i

# Pipeline: numbers -> squares -> evens
result = list(evens(squares(numbers(10))))
print(f"\nPipeline result: {result}")

