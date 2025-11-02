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
print("Empty list:", empty_list)  # Output: Empty list: []

# List of numbers
numbers = [1, 2, 3, 4, 5]
print("Numbers:", numbers)  # Output: Numbers: [1, 2, 3, 4, 5]

# List of strings
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)  # Output: Fruits: ['apple', 'banana', 'cherry']

# Mixed types (Python allows this!)
mixed = [1, "hello", 3.14, True]
print("Mixed types:", mixed)  # Output: Mixed types: [1, 'hello', 3.14, True]

# LIST INDEXING
# Access items by their position (index starts at 0)

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(f"\nFirst fruit: {fruits[0]}")    # Output: First fruit: apple  # First item (index 0)
print(f"Second fruit: {fruits[1]}")     # Output: Second fruit: banana  # Second item (index 1)
print(f"Last fruit: {fruits[4]}")      # Output: Last fruit: elderberry  # Last item (index 4)
print(f"Last fruit: {fruits[-1]}")     # Output: Last fruit: elderberry  # Negative index: -1 is last item
print(f"Second to last: {fruits[-2]}") # Output: Second to last: date  # -2 is second to last

# LIST SLICING
# Get a portion of the list using slicing [start:stop:step]

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"\nOriginal: {numbers}")  # Output: Original: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"First 3: {numbers[0:3]}")      # Output: First 3: [0, 1, 2]  # Items 0, 1, 2
print(f"Items 2-5: {numbers[2:5]}")    # Output: Items 2-5: [2, 3, 4]  # Items 2, 3, 4
print(f"Last 3: {numbers[-3:]}")       # Output: Last 3: [7, 8, 9]  # Last 3 items
print(f"All but last: {numbers[:-1]}") # Output: All but last: [0, 1, 2, 3, 4, 5, 6, 7, 8]  # All except last
print(f"Every 2nd item: {numbers[::2]}") # Output: Every 2nd item: [0, 2, 4, 6, 8]  # Step by 2
print(f"Reverse: {numbers[::-1]}")     # Output: Reverse: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  # Reverse the list

# MODIFYING LISTS

# Change an item
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"
print(f"\nModified list: {fruits}")  # Output: Modified list: ['apple', 'blueberry', 'cherry']

# Add items

# append() - adds to the end
fruits.append("date")
print(f"After append: {fruits}")  # Output: After append: ['apple', 'blueberry', 'cherry', 'date']

# insert() - inserts at a specific position
fruits.insert(1, "apricot")  # Insert at index 1
print(f"After insert: {fruits}")  # Output: After insert: ['apple', 'apricot', 'blueberry', 'cherry', 'date']

# extend() - adds multiple items from another list
more_fruits = ["elderberry", "fig"]
fruits.extend(more_fruits)
print(f"After extend: {fruits}")  # Output: After extend: ['apple', 'apricot', 'blueberry', 'cherry', 'date', 'elderberry', 'fig']

# Remove items

# remove() - removes first occurrence of value
fruits.remove("cherry")
print(f"\nAfter remove: {fruits}")  # Output: After remove: ['apple', 'apricot', 'blueberry', 'date', 'elderberry', 'fig']

# pop() - removes and returns item at index (default: last item)
last_fruit = fruits.pop()
print(f"Popped item: {last_fruit}")  # Output: Popped item: fig
print(f"After pop(): {fruits}")  # Output: After pop(): ['apple', 'apricot', 'blueberry', 'date', 'elderberry']

popped = fruits.pop(0)  # Remove first item
print(f"Popped first: {popped}")  # Output: Popped first: apple
print(f"After pop(0): {fruits}")  # Output: After pop(0): ['apricot', 'blueberry', 'date', 'elderberry']

# del - removes item by index
del fruits[0]
print(f"After del fruits[0]: {fruits}")  # Output: After del fruits[0]: ['blueberry', 'date', 'elderberry']

# clear() - removes all items
fruits.clear()
print(f"After clear: {fruits}")  # Output: After clear: []

# LIST METHODS

fruits = ["apple", "banana", "cherry", "apple"]

# count() - counts occurrences
print(f"\nCount of 'apple': {fruits.count('apple')}")  # Output: Count of 'apple': 2

# index() - finds first index of value
print(f"Index of 'banana': {fruits.index('banana')}")  # Output: Index of 'banana': 1

# sort() - sorts the list in place
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()
print(f"Sorted numbers: {numbers}")  # Output: Sorted numbers: [1, 1, 2, 3, 4, 5, 6, 9]
numbers.sort(reverse=True)  # Sort in descending order
print(f"Reverse sorted: {numbers}")  # Output: Reverse sorted: [9, 6, 5, 4, 3, 2, 1, 1]

# sorted() - returns new sorted list (doesn't modify original)
fruits = ["cherry", "apple", "banana"]
sorted_fruits = sorted(fruits)
print(f"Original: {fruits}")  # Output: Original: ['cherry', 'apple', 'banana']
print(f"Sorted copy: {sorted_fruits}")  # Output: Sorted copy: ['apple', 'banana', 'cherry']

# reverse() - reverses the list in place
fruits.reverse()
print(f"Reversed: {fruits}")  # Output: Reversed: ['banana', 'apple', 'cherry']

# COPYING LISTS

# Shallow copy (both reference same list - changes affect both!)
original = [1, 2, 3]
copy_wrong = original
copy_wrong.append(4)
print(f"\nOriginal: {original}")  # Output: Original: [1, 2, 3, 4]  # Also has 4!

# Correct way to copy
original = [1, 2, 3]
copy_correct = original.copy()  # or list(original) or original[:]
copy_correct.append(4)
print(f"Original: {original}")  # Output: Original: [1, 2, 3]
print(f"Copy: {copy_correct}")  # Output: Copy: [1, 2, 3, 4]

# LIST LENGTH
numbers = [1, 2, 3, 4, 5]
print(f"\nLength of list: {len(numbers)}")  # Output: Length of list: 5

# CHECKING IF ITEM EXISTS
fruits = ["apple", "banana", "cherry"]
print(f"\n'banana' in fruits: {'banana' in fruits}")  # Output: 'banana' in fruits: True
print(f"'orange' in fruits: {'orange' in fruits}")  # Output: 'orange' in fruits: False

# LIST COMPREHENSION (preview - we'll cover this in detail later)
# Quick example: create list of squares
squares = [x**2 for x in range(1, 6)]
print(f"\nSquares: {squares}")  # Output: Squares: [1, 4, 9, 16, 25]

# NESTED LISTS (lists within lists)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"\nMatrix: {matrix}")  # Output: Matrix: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Element at row 1, col 2: {matrix[1][2]}")  # Output: Element at row 1, col 2: 6

