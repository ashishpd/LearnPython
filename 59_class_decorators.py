"""
59_class_decorators.py

This file demonstrates class decorators in Python.
Decorating classes with additional functionality.
"""

print("CLASS DECORATORS")
print("=" * 50)

# CLASS DECORATOR
print("1. Class Decorator:")

def add_method(cls):
    """Decorator that adds a method to class."""
    def new_method(self):
        return "Added by decorator"
    cls.new_method = new_method
    return cls

@add_method
class Example:
    pass

obj = Example()
print(f"   {obj.new_method()}\n")

print("Class decorators demonstration complete!")

