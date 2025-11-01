"""
28_exception_types.py

This file demonstrates different exception types in Python.
Understanding exception types helps write better error handling code.
"""

# BUILT-IN EXCEPTION HIERARCHY
# All exceptions inherit from BaseException

# BaseException
#   ├── SystemExit
#   ├── KeyboardInterrupt
#   └── Exception
#       ├── StopIteration
#       ├── ArithmeticError
#       │   ├── ZeroDivisionError
#       │   └── OverflowError
#       ├── AssertionError
#       ├── AttributeError
#       ├── EOFError
#       ├── LookupError
#       │   ├── IndexError
#       │   └── KeyError
#       ├── NameError
#       ├── OSError
#       │   ├── FileNotFoundError
#       │   └── PermissionError
#       ├── TypeError
#       ├── ValueError
#       └── RuntimeError

# ARITHMETIC ERRORS

# ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")

# OverflowError (rare in modern Python)
try:
    import math
    huge = math.exp(1000)
except OverflowError as e:
    print(f"OverflowError: {e}")

# LOOKUP ERRORS

# IndexError - list index out of range
try:
    my_list = [1, 2, 3]
    print(my_list[10])
except IndexError as e:
    print(f"IndexError: {e}")

# KeyError - dictionary key not found
try:
    my_dict = {"a": 1, "b": 2}
    print(my_dict["c"])
except KeyError as e:
    print(f"KeyError: {e}")

# TYPE ERRORS

# TypeError - wrong type
try:
    result = "hello" + 5
except TypeError as e:
    print(f"TypeError: {e}")

# VALUE ERRORS

# ValueError - wrong value
try:
    number = int("not a number")
except ValueError as e:
    print(f"ValueError: {e}")

# ATTRIBUTE ERRORS

# AttributeError - attribute doesn't exist
try:
    "hello".nonexistent_method()
except AttributeError as e:
    print(f"AttributeError: {e}")

# NAME ERRORS

# NameError - name not defined
try:
    print(undefined_variable)
except NameError as e:
    print(f"NameError: {e}")

# OS ERRORS

# FileNotFoundError
try:
    with open("nonexistent.txt") as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")

# PermissionError
try:
    # Attempting to write to protected location
    with open("/etc/protected.txt", "w") as f:
        f.write("test")
except PermissionError as e:
    print(f"PermissionError: {e}")

# CREATING CUSTOM EXCEPTIONS

class CustomError(Exception):
    """Base class for custom exceptions."""
    pass

class ValidationError(CustomError):
    """Raised when validation fails."""
    def __init__(self, message, field):
        self.message = message
        self.field = field
        super().__init__(f"{field}: {message}")

def validate_age(age):
    """Validate age."""
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0:
        raise ValidationError("Age cannot be negative", "age")
    if age > 150:
        raise ValidationError("Age seems unrealistic", "age")
    return True

try:
    validate_age(-5)
except ValidationError as e:
    print(f"\nCustom ValidationError: {e}")

# CATCHING MULTIPLE EXCEPTIONS

try:
    # Code that might raise different errors
    value = int(input("Enter a number: "))
    result = 10 / value
    my_list = [1, 2, 3]
    print(my_list[result])
except (ValueError, ZeroDivisionError) as e:
    print(f"Input or division error: {e}")
except IndexError as e:
    print(f"Index error: {e}")
except Exception as e:
    print(f"Other error: {e}")

# CHECKING EXCEPTION TYPES

def handle_exception(e):
    """Handle different exception types."""
    if isinstance(e, ValueError):
        return "Value error occurred"
    elif isinstance(e, TypeError):
        return "Type error occurred"
    else:
        return "Unknown error occurred"

try:
    int("not a number")
except Exception as e:
    print(f"\n{handle_exception(e)}")

# EXCEPTION CHAINING

try:
    try:
        x = 1 / 0
    except ZeroDivisionError as e:
        raise ValueError("Invalid calculation") from e
except ValueError as e:
    print(f"\nChained exception: {e}")
    print(f"Original cause: {e.__cause__}")

