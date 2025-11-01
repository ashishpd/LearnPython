"""
23_list_slicing_advanced.py

This file demonstrates advanced list slicing techniques in Python.
Slicing is a powerful way to extract portions of sequences.
"""

# BASIC SLICING REVIEW
# [start:stop:step]

numbers = list(range(10))
print(f"Original: {numbers}")

# Basic slice
print(f"First 3: {numbers[0:3]}")
print(f"Last 3: {numbers[-3:]}")
print(f"All: {numbers[:]}")

# STEP PARAMETER
print(f"\nEvery 2nd: {numbers[::2]}")
print(f"Reverse: {numbers[::-1]}")
print(f"Every 3rd from end: {numbers[::-3]}")

# ADVANCED SLICING PATTERNS

# Split list into chunks
def chunk_list(lst, chunk_size):
    """Split list into chunks of specified size."""
    return [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]

numbers = list(range(10))
chunks = chunk_list(numbers, 3)
print(f"\nChunked list: {chunks}")

# Remove elements by slicing
numbers = [0, 1, 2, 3, 4, 5]
numbers = numbers[:2] + numbers[4:]  # Remove indices 2 and 3
print(f"\nRemoved middle: {numbers}")

# Replace section
numbers = [0, 1, 2, 3, 4, 5]
numbers[1:4] = [10, 20, 30]
print(f"Replaced section: {numbers}")

# NEGATIVE INDICES AND STEPS
data = list(range(20))
print(f"\nEvery 3rd from index 5: {data[5::3]}")
print(f"Last 5, every 2nd: {data[-5::2]}")
print(f"Reverse middle section: {data[5:15][::-1]}")

# MULTIDIMENSIONAL SLICING (nested lists)

matrix = [[i*3 + j for j in range(3)] for i in range(4)]
print(f"\nMatrix: {matrix}")
print(f"First row: {matrix[0]}")
print(f"First column: {[row[0] for row in matrix]}")
print(f"Submatrix: {[row[1:] for row in matrix[1:3]]}")

