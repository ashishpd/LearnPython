"""
48_debugging.py

This file demonstrates debugging techniques in Python.
Covers pdb (Python debugger), breakpoints, debugging strategies, and tools.
"""

import pdb
import sys

print("DEBUGGING IN PYTHON")
print("=" * 50)

# PRINT DEBUGGING
# Simple but effective

print("1. Print Debugging:")

def calculate_total(items):
    """Function with print debugging."""
    total = 0
    print(f"DEBUG: Starting calculation with {len(items)} items")
    
    for item in items:
        print(f"DEBUG: Processing item {item}")
        total += item
        print(f"DEBUG: Running total = {total}")
    
    print(f"DEBUG: Final total = {total}")
    return total

result = calculate_total([1, 2, 3, 4, 5])
print(f"   Result: {result}\n")

# PDB - PYTHON DEBUGGER
# Interactive debugger

print("2. Python Debugger (pdb):")

def buggy_function(x, y):
    """Function with potential bug."""
    result = x / y
    return result

# Set breakpoint
def example_with_breakpoint():
    """Example using breakpoint() (Python 3.7+)."""
    x = 10
    y = 2
    # breakpoint()  # Uncomment to enter debugger
    result = buggy_function(x, y)
    return result

print("   Commands:")
print("     - n (next) - Execute next line")
print("     - s (step) - Step into function")
print("     - c (continue) - Continue execution")
print("     - l (list) - Show code")
print("     - p variable - Print variable")
print("     - q (quit) - Quit debugger")
print("     - breakpoint() - Set breakpoint (Python 3.7+)")
print()

# PDB SET_TRACE
# Programmatic breakpoint

def example_pdb():
    """Example using pdb.set_trace()."""
    x = 5
    y = 3
    # pdb.set_trace()  # Uncomment to enter debugger
    result = x + y
    return result

print("3. pdb.set_trace():")
print("   Use pdb.set_trace() for manual breakpoints")
print("   Or use breakpoint() in Python 3.7+\n")

# DEBUGGER COMMANDS IN CODE
# Common debugging patterns

print("4. Debugging Patterns:")

# Check if debugging
def debug_function():
    """Function that checks if debugging."""
    if __debug__:
        print("   Running in debug mode")
    else:
        print("   Running in optimized mode (python -O)")

debug_function()
print()

# ASSERT STATEMENTS
# Use assertions for debugging

def process_age(age):
    """Process age with assertion."""
    assert age >= 0, f"Age must be non-negative, got {age}"
    assert age < 150, f"Age seems unrealistic: {age}"
    return age

print("5. Assertions:")
try:
    process_age(25)
    print("   Valid age processed")
    # process_age(-5)  # Would raise AssertionError
except AssertionError as e:
    print(f"   Assertion failed: {e}")
print()

# INSPECT MODULE
# Introspect objects

import inspect

def example_function(param1, param2=10):
    """Example function for inspection."""
    return param1 + param2

print("6. Inspect Module:")

# Get function signature
sig = inspect.signature(example_function)
print(f"   Signature: {sig}")

# Get source code
source = inspect.getsource(example_function)
print(f"   Source length: {len(source)} chars")

# Get file location
file_location = inspect.getfile(example_function)
print(f"   Defined in: {file_location}")
print()

# TRACEBACK
# Understanding error traces

print("7. Traceback:")

def function_a():
    return function_b()

def function_b():
    return function_c()

def function_c():
    raise ValueError("Error in function_c")

try:
    function_a()
except Exception as e:
    import traceback
    print(f"   Error: {e}")
    print("   Traceback:")
    traceback.print_exc()
    print()

# DEBUGGING WITH LOGGING
# Use logging for debugging

import logging

logging.basicConfig(level=logging.DEBUG)
debug_logger = logging.getLogger("debug")

def logged_function(x):
    """Function with debug logging."""
    debug_logger.debug(f"Entering function with x={x}")
    
    if x < 0:
        debug_logger.warning(f"Negative value: {x}")
    
    result = x * 2
    debug_logger.debug(f"Result: {result}")
    
    return result

print("8. Debugging with Logging:")
logged_function(5)
print()

# EXCEPTION HOOKS
# Custom exception handling

def custom_exception_hook(exc_type, exc_value, exc_traceback):
    """Custom exception handler."""
    print(f"   Custom handler: {exc_type.__name__}: {exc_value}")

# Set custom hook
original_hook = sys.excepthook
sys.excepthook = custom_exception_hook

print("9. Exception Hooks:")
print("   Custom exception handler installed")
print("   (Restored original hook)\n")

sys.excepthook = original_hook

# DEBUGGING TOOLS
print("10. Debugging Tools:")

tools = {
    "pdb": "Built-in Python debugger",
    "ipdb": "Enhanced pdb with IPython features",
    "pudb": "Full-screen debugger",
    "py-spy": "Sampling profiler",
    "memory_profiler": "Memory usage profiler",
    "cProfile": "Performance profiler",
    "logging": "Debugging with logs",
}

for tool, desc in tools.items():
    print(f"    {tool}: {desc}")

print()

# DEBUGGING STRATEGIES
print("11. Debugging Strategies:")
print("    ✓ Reproduce the bug consistently")
print("    ✓ Isolate the problem (binary search)")
print("    ✓ Check assumptions with assertions")
print("    ✓ Use version control (git bisect)")
print("    ✓ Read error messages carefully")
print("    ✓ Use debugger for complex issues")
print("    ✓ Log state at key points")
print("    ✓ Test with minimal examples")
print()

# COMMON BUGS AND FIXES
print("12. Common Bugs:")

# Type errors
def type_bug_example():
    """Common type-related bugs."""
    items = ["1", "2", "3"]
    # total = sum(items)  # TypeError: can't sum strings
    
    # Fix: Convert to numbers
    total = sum(int(item) for item in items)
    return total

print(f"    Type bug fix: {type_bug_example()}")

# Off-by-one errors
def off_by_one_example():
    """Common off-by-one errors."""
    items = [1, 2, 3, 4, 5]
    # Wrong: range(len(items)) might miss edge cases
    # Correct: use range(len(items)) or enumerate
    return [x * 2 for x in items]

print(f"    Off-by-one example: {off_by_one_example()}")

# None handling
def none_handling_example():
    """Proper None handling."""
    value = None
    # Wrong: result = value.upper()
    # Correct:
    result = value.upper() if value else "default"
    return result

print(f"    None handling: {none_handling_example()}\n")

# DEBUGGING EXAMPLE
print("13. Complete Debugging Example:")

def find_bug_in_code():
    """Code with a bug to find."""
    data = [1, 2, 3, 4, 5]
    total = 0
    
    for i in range(len(data) + 1):  # Bug: +1 causes IndexError
        try:
            total += data[i]
        except IndexError as e:
            print(f"   Bug found: {e}")
            # Fix: range(len(data))
    
    return total

try:
    find_bug_in_code()
except Exception as e:
    print(f"   Exception caught: {e}\n")

print("Debugging demonstration complete!")
print("\nQuick reference:")
print("  - breakpoint() or pdb.set_trace() - Enter debugger")
print("  - assert statement - Check assumptions")
print("  - logging.debug() - Debug logging")
print("  - inspect module - Introspect objects")
print("  - traceback - Error traces")

