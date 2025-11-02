"""
72_generator_advanced.py

This file demonstrates advanced generator features.
Covers yield from, async generators, and generator delegation.
"""

print("ADVANCED GENERATORS")
print("=" * 50)

# YIELD FROM
print("1. yield from:")

def generator1():
    yield 1
    yield 2

def generator2():
    yield from generator1()
    yield 3

print(f"   {list(generator2())}\n")

# GENERATOR EXPRESSIONS
print("2. Generator Expressions:")

gen = (x**2 for x in range(5))
print(f"   {list(gen)}\n")

print("Advanced generators demonstration complete!")

