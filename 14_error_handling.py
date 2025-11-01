"""
14_error_handling.py

This file demonstrates error handling in Python using try/except blocks.
Proper error handling makes your programs more robust and user-friendly.
"""

# BASIC TRY-EXCEPT
# Try to execute code, catch errors if they occur

try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero!")

# MULTIPLE EXCEPT CLAUSES
# Handle different types of errors

try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(f"Result: {result}")
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# CATCHING ALL EXCEPTIONS (use sparingly!)
# Be specific about which exceptions you catch

try:
    # Some code that might fail
    value = int("not a number")
except Exception as e:
    print(f"An error occurred: {e}")

# GETTING ERROR INFORMATION
# Use 'as' to get the exception object

try:
    x = int("abc")
except ValueError as error:
    print(f"Error type: {type(error).__name__}")
    print(f"Error message: {error}")

# ELSE CLAUSE
# Runs if no exception occurred

try:
    number = int("42")
    result = number * 2
except ValueError:
    print("Invalid number!")
else:
    print(f"Success! Result: {result}")

# FINALLY CLAUSE
# Always executes, whether exception occurred or not
# Useful for cleanup (closing files, etc.)

try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    print("This always runs!")
    # File would be closed here in real code

# With statement handles this automatically:
try:
    with open("example.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")

# RAISING EXCEPTIONS
# You can raise exceptions yourself using 'raise'

def divide(a, b):
    """Divides a by b, raises error if b is 0."""
    if b == 0:
        raise ValueError("Division by zero is not allowed!")
    return a / b

try:
    result = divide(10, 0)
except ValueError as e:
    print(f"Error: {e}")

# COMMON BUILT-IN EXCEPTIONS

# ValueError - wrong value type or format
try:
    int("not a number")
except ValueError as e:
    print(f"\nValueError: {e}")

# TypeError - wrong type
try:
    "hello" + 5
except TypeError as e:
    print(f"TypeError: {e}")

# IndexError - index out of range
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

# AttributeError - attribute doesn't exist
try:
    "hello".nonexistent_method()
except AttributeError as e:
    print(f"AttributeError: {e}")

# FileNotFoundError - file doesn't exist
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")

# CREATING CUSTOM EXCEPTIONS
# Define your own exception classes

class InsufficientFundsError(Exception):
    """Raised when account has insufficient funds."""
    pass

def withdraw(balance, amount):
    """Withdraw money from account."""
    if amount > balance:
        raise InsufficientFundsError(f"Insufficient funds! Balance: ${balance}, Requested: ${amount}")
    return balance - amount

try:
    balance = withdraw(100, 150)
except InsufficientFundsError as e:
    print(f"\nCustom exception: {e}")

# EXCEPTION CHAINING
# When one exception causes another

try:
    try:
        x = 1 / 0
    except ZeroDivisionError:
        # Re-raise with additional context
        raise ValueError("Invalid calculation") from None
except ValueError as e:
    print(f"\nChained exception: {e}")

# ASSERT STATEMENTS
# Use for debugging - raises AssertionError if condition is False

def calculate_average(numbers):
    """Calculate average of numbers."""
    assert len(numbers) > 0, "List cannot be empty!"
    return sum(numbers) / len(numbers)

# This would raise AssertionError:
# result = calculate_average([])

# Good practice: Use assertions for debugging, exceptions for user errors

# BEST PRACTICES

# 1. Be specific about exceptions
# Bad:
# try:
#     # code
# except:
#     pass

# Good:
try:
    number = int(input("Enter number: "))
except ValueError:
    print("Invalid input!")

# 2. Don't catch exceptions you can't handle
# If you can't fix the problem, let it propagate

# 3. Use else for code that should run only if no exception
try:
    result = perform_operation()
except SomeError:
    handle_error()
else:
    process_result(result)  # Only runs if no exception

# 4. Use finally for cleanup
try:
    file = open("data.txt", "r")
    # process file
except IOError:
    print("File error!")
finally:
    file.close()  # Always closes, even if error occurred

# Or better, use 'with' statement which handles this automatically

