"""
60_metaprogramming.py

This file demonstrates metaprogramming in Python.
Dynamic attribute access and modification.
"""

print("METAPROGRAMMING")
print("=" * 50)

# __GETATTR__
print("1. __getattr__:")

class Dynamic:
    def __getattr__(self, name):
        return f"Attribute '{name}' not found"

obj = Dynamic()
print(f"   {obj.missing_attribute}\n")

# __SETATTR__
print("2. __setattr__:")

class Validated:
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            print(f"   Setting {name} = {value}")
            super().__setattr__(name, value)

valid = Validated()
valid.value = 10
print()

# __CALL__
print("3. __call__:")

class Callable:
    def __call__(self, x):
        return x * 2

callable_obj = Callable()
print(f"   {callable_obj(5)}\n")

print("Metaprogramming demonstration complete!")

