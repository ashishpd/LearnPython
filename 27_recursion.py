"""
27_recursion.py

This file demonstrates recursion in Python.
Recursion is when a function calls itself.
It's useful for problems that can be broken down into smaller, similar problems.
"""

# FACTORIAL (CLASSIC EXAMPLE)
# n! = n * (n-1) * (n-2) * ... * 1

def factorial(n):
    """Calculate factorial recursively."""
    # Base case
    if n <= 1:
        return 1
    # Recursive case
    return n * factorial(n - 1)

print(f"Factorial of 5: {factorial(5)}")

# FIBONACCI SEQUENCE
# Each number is sum of two preceding ones

def fibonacci(n):
    """Calculate nth Fibonacci number."""
    # Base cases
    if n <= 0:
        return 0
    if n == 1:
        return 1
    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"\nFibonacci sequence (first 10):")
for i in range(10):
    print(f"F({i}) = {fibonacci(i)}")

# POWER FUNCTION

def power(base, exponent):
    """Calculate base raised to exponent."""
    # Base case
    if exponent == 0:
        return 1
    # Recursive case
    return base * power(base, exponent - 1)

print(f"\n2^5 = {power(2, 5)}")

# SUM OF LIST

def sum_list(lst):
    """Sum elements in list recursively."""
    if not lst:  # Base case: empty list
        return 0
    # Recursive case: first element + sum of rest
    return lst[0] + sum_list(lst[1:])

numbers = [1, 2, 3, 4, 5]
print(f"\nSum of {numbers}: {sum_list(numbers)}")

# BINARY SEARCH (RECURSIVE)

def binary_search(arr, target, low=0, high=None):
    """Recursive binary search."""
    if high is None:
        high = len(arr) - 1
    
    # Base case: not found
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    # Base case: found
    if arr[mid] == target:
        return mid
    
    # Recursive cases
    if arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)

sorted_list = [1, 3, 5, 7, 9, 11, 13]
print(f"\nSearching for 7: index {binary_search(sorted_list, 7)}")

# TOWER OF HANOI

def tower_of_hanoi(n, source, destination, auxiliary):
    """Solve Tower of Hanoi recursively."""
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, destination)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, auxiliary, destination, source)

print("\nTower of Hanoi (3 disks):")
tower_of_hanoi(3, 'A', 'C', 'B')

# IMPORTANT NOTES
# 1. Always have a base case (stopping condition)
# 2. Recursive case must progress toward base case
# 3. Python has recursion limit (usually 1000)
# 4. Some problems are easier recursively, but iterative solutions may be more efficient

