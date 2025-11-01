"""
20_decorators.py

This file demonstrates decorators in Python.
Decorators are functions that modify or enhance other functions.
They're a powerful way to add functionality to existing code.
"""

# BASIC DECORATOR
# A decorator is a function that takes another function as argument

def my_decorator(func):
    """A simple decorator that adds functionality."""
    def wrapper():
        print("Something before function")
        func()
        print("Something after function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Something before function
# Hello!
# Something after function

# DECORATOR WITH ARGUMENTS
# Handle functions with parameters

def smart_decorator(func):
    """Decorator that works with functions that have arguments."""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

@smart_decorator
def add(a, b):
    return a + b

print(f"\n{add(3, 4)}")

# TIMING DECORATOR (PRACTICAL EXAMPLE)

import time

def timing_decorator(func):
    """Decorator that measures function execution time."""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(0.1)
    return "Done"

slow_function()

# PRESERVING FUNCTION METADATA
# Use functools.wraps to preserve original function info

from functools import wraps

def preserving_decorator(func):
    """Decorator that preserves function metadata."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@preserving_decorator
def example():
    """This is an example function."""
    pass

print(f"\nFunction name: {example.__name__}")
print(f"Function docstring: {example.__doc__}")

# DECORATOR WITH ARGUMENTS
# Decorator that accepts its own arguments

def repeat(times):
    """Decorator that repeats function execution."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    print(f"Hello, {name}!")

print("\nRepeated greeting:")
greet("Alice")

# MULTIPLE DECORATORS
# Stack decorators (applied bottom to top)

def bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

def italic(func):
    def wrapper():
        return f"<i>{func()}</i>"
    return wrapper

@bold
@italic
def get_text():
    return "Hello, World!"

print(f"\nDecorated text: {get_text()}")

