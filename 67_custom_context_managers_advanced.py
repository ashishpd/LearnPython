"""
67_custom_context_managers_advanced.py

This file demonstrates advanced context manager patterns.
Covers async context managers, nested contexts, and advanced patterns.
"""

from contextlib import contextmanager, asynccontextmanager

print("ADVANCED CONTEXT MANAGERS")
print("=" * 50)

# ASYNC CONTEXT MANAGER
print("1. Async Context Manager:")

@asynccontextmanager
async def async_resource():
    print("   Acquiring async resource")
    yield "resource"
    print("   Releasing async resource")

# async with async_resource() as res:
#     pass

print()

# NESTED CONTEXTS
print("2. Nested Contexts:")

@contextmanager
def outer():
    print("   Outer enter")
    yield
    print("   Outer exit")

@contextmanager
def inner():
    print("   Inner enter")
    yield
    print("   Inner exit")

with outer():
    with inner():
        print("   Inside both")

print()

print("Advanced context managers demonstration complete!")

