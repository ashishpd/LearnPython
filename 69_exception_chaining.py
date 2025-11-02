"""
69_exception_chaining.py

This file demonstrates exception chaining in Python.
Covers raise from, exception context, and chaining patterns.
"""

print("EXCEPTION CHAINING")
print("=" * 50)

# RAISE FROM
print("1. raise from:")

try:
    try:
        int("not a number")
    except ValueError as e:
        raise TypeError("Conversion failed") from e
except TypeError as e:
    print(f"   Exception: {e}")
    if e.__cause__:
        print(f"   Caused by: {e.__cause__}\n")

print("Exception chaining demonstration complete!")

