"""
55_functools_advanced.py

This file demonstrates advanced functools utilities.
Covers partial, reduce, lru_cache, singledispatch, and more.
"""

from functools import partial, reduce, lru_cache, singledispatch, wraps, total_ordering

print("ADVANCED FUNCTOOLS")
print("=" * 50)

# PARTIAL
# Create functions with pre-filled arguments

print("1. partial (Pre-fill Arguments):")

def multiply(x, y):
    return x * y

# Create specialized functions
double = partial(multiply, 2)
triple = partial(multiply, 3)

print(f"   double(5): {double(5)}")
print(f"   triple(5): {triple(5)}\n")

# REDUCE
# Reduce iterable to single value

print("2. reduce:")

numbers = [1, 2, 3, 4, 5]
sum_result = reduce(lambda x, y: x + y, numbers)
product = reduce(lambda x, y: x * y, numbers)

print(f"   Sum: {sum_result}")
print(f"   Product: {product}\n")

# LRU_CACHE
# Memoization decorator

print("3. lru_cache (Memoization):")

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(f"   fibonacci(20): {fibonacci(20)}")
print(f"   Cache info: {fibonacci.cache_info()}\n")

# SINGLEDISPATCH
# Function overloading based on type

print("4. singledispatch:")

@singledispatch
def process(data):
    return f"Unknown type: {type(data)}"

@process.register
def _(data: int):
    return f"Processing integer: {data}"

@process.register
def _(data: str):
    return f"Processing string: {data}"

print(f"   {process(42)}")
print(f"   {process('hello')}\n")

# WRAPS
# Preserve function metadata

print("5. wraps (Preserve Metadata):")

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def example():
    """Example function."""
    pass

print(f"   Function name: {example.__name__}")
print(f"   Docstring: {example.__doc__}\n")

# TOTAL_ORDERING
# Auto-generate comparison methods

print("6. total_ordering:")

@total_ordering
class Student:
    def __init__(self, grade):
        self.grade = grade
    
    def __eq__(self, other):
        return self.grade == other.grade
    
    def __lt__(self, other):
        return self.grade < other.grade

s1 = Student(85)
s2 = Student(90)
print(f"   s1 < s2: {s1 < s2}")
print(f"   s1 >= s2: {s1 >= s2}\n")

print("Functools demonstration complete!")

