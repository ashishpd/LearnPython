"""
08_lists.py

This file demonstrates lists in Python.
Lists are ordered collections of items that can be changed (mutable).
They can contain any type of data, including mixed types.
"""

# CREATING LISTS
# Lists are created using square brackets []

# Empty list
empty_list = []
print("Empty list:", empty_list)

# List of numbers
numbers = [1, 2, 3, 4, 5]
print("Numbers:", numbers)

# List of strings
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)

# Mixed types (Python allows this!)
mixed = [1, "hello", 3.14, True]
print("Mixed types:", mixed)

# LIST INDEXING
# Access items by their position (index starts at 0)

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(f"\nFirst fruit: {fruits[0]}")    # First item (index 0)
print(f"Second fruit: {fruits[1]}")     # Second item (index 1)
print(f"Last fruit: {fruits[4]}")      # Last item (index 4)
print(f"Last fruit: {fruits[-1]}")     # Negative index: -1 is last item
print(f"Second to last: {fruits[-2]}") # -2 is second to last

# LIST SLICING
# Get a portion of the list using slicing [start:stop:step]

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"\nOriginal: {numbers}")
print(f"First 3: {numbers[0:3]}")      # Items 0, 1, 2
print(f"Items 2-5: {numbers[2:5]}")    # Items 2, 3, 4
print(f"Last 3: {numbers[-3:]}")       # Last 3 items
print(f"All but last: {numbers[:-1]}") # All except last
print(f"Every 2nd item: {numbers[::2]}") # Step by 2
print(f"Reverse: {numbers[::-1]}")     # Reverse the list

# MODIFYING LISTS

# Change an item
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"
print(f"\nModified list: {fruits}")

# Add items

# append() - adds to the end
fruits.append("date")
print(f"After append: {fruits}")

# insert() - inserts at a specific position
fruits.insert(1, "apricot")  # Insert at index 1
print(f"After insert: {fruits}")

# extend() - adds multiple items from another list
more_fruits = ["elderberry", "fig"]
fruits.extend(more_fruits)
print(f"After extend: {fruits}")

# Remove items

# remove() - removes first occurrence of value
fruits.remove("cherry")
print(f"\nAfter remove: {fruits}")

# pop() - removes and returns item at index (default: last item)
last_fruit = fruits.pop()
print(f"Popped item: {last_fruit}")
print(f"After pop(): {fruits}")

popped = fruits.pop(0)  # Remove first item
print(f"Popped first: {popped}")
print(f"After pop(0): {fruits}")

# del - removes item by index
del fruits[0]
print(f"After del fruits[0]: {fruits}")

# clear() - removes all items
fruits.clear()
print(f"After clear: {fruits}")

# LIST METHODS

fruits = ["apple", "banana", "cherry", "apple"]

# count() - counts occurrences
print(f"\nCount of 'apple': {fruits.count('apple')}")

# index() - finds first index of value
print(f"Index of 'banana': {fruits.index('banana')}")

# sort() - sorts the list in place
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()
print(f"Sorted numbers: {numbers}")
numbers.sort(reverse=True)  # Sort in descending order
print(f"Reverse sorted: {numbers}")

# sorted() - returns new sorted list (doesn't modify original)
fruits = ["cherry", "apple", "banana"]
sorted_fruits = sorted(fruits)
print(f"Original: {fruits}")
print(f"Sorted copy: {sorted_fruits}")

# reverse() - reverses the list in place
fruits.reverse()
print(f"Reversed: {fruits}")

# COPYING LISTS

# Shallow copy (both reference same list - changes affect both!)
original = [1, 2, 3]
copy_wrong = original
copy_wrong.append(4)
print(f"\nOriginal: {original}")  # Also has 4!

# Correct way to copy
original = [1, 2, 3]
copy_correct = original.copy()  # or list(original) or original[:]
copy_correct.append(4)
print(f"Original: {original}")
print(f"Copy: {copy_correct}")

# LIST LENGTH
numbers = [1, 2, 3, 4, 5]
print(f"\nLength of list: {len(numbers)}")

# CHECKING IF ITEM EXISTS
fruits = ["apple", "banana", "cherry"]
print(f"\n'banana' in fruits: {'banana' in fruits}")
print(f"'orange' in fruits: {'orange' in fruits}")

# LIST COMPREHENSION (preview - we'll cover this in detail later)
# Quick example: create list of squares
squares = [x**2 for x in range(1, 6)]
print(f"\nSquares: {squares}")

# NESTED LISTS (lists within lists)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"\nMatrix: {matrix}")
print(f"Element at row 1, col 2: {matrix[1][2]}")

