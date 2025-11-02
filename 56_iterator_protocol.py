"""
56_iterator_protocol.py

This file demonstrates the iterator protocol in Python.
Covers __iter__, __next__, creating custom iterators.
"""

print("ITERATOR PROTOCOL")
print("=" * 50)

# BASIC ITERATOR
# Classes implementing iterator protocol

print("1. Custom Iterator:")

class CountDown:
    """Countdown iterator."""
    
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

countdown = CountDown(5)
print("   Countdown:")
for num in countdown:
    print(f"     {num}")

print()

# ITERABLE VS ITERATOR
print("2. Iterable vs Iterator:")
print("   Iterable: Has __iter__()")
print("   Iterator: Has __iter__() and __next__()")
print("   Iterators are also iterables\n")

# ITER() FUNCTION
print("3. iter() Function:")

numbers = [1, 2, 3]
iter_obj = iter(numbers)
print(f"   Next: {next(iter_obj)}")
print(f"   Next: {next(iter_obj)}")
print()

# ITERATOR UTILITIES
print("4. Iterator Utilities:")

from itertools import count, cycle, islice

# Count
counter = count(10, 2)
print(f"   Count: {list(islice(counter, 5))}")

# Cycle
cycler = cycle([1, 2, 3])
print(f"   Cycle: {list(islice(cycler, 7))}")

print()

print("Iterator protocol demonstration complete!")

