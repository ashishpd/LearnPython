"""
10_tuples_and_sets.py

This file demonstrates tuples and sets in Python.
Tuples are ordered, immutable collections.
Sets are unordered collections of unique elements.
"""

# ========================================
# TUPLES
# ========================================

# CREATING TUPLES
# Tuples use parentheses () instead of square brackets

# Empty tuple
empty_tuple = ()
print("Empty tuple:", empty_tuple)

# Tuple with items
coordinates = (3, 5)
print("Coordinates:", coordinates)

# Tuple with multiple types
person_info = ("Alice", 30, "Engineer")
print("Person info:", person_info)

# Note: Single item tuple needs a comma!
single_item = (42,)  # This is a tuple
not_a_tuple = (42)   # This is just the number 42
print(f"Single item tuple: {single_item}, type: {type(single_item)}")

# Tuples without parentheses (comma makes it a tuple)
numbers = 1, 2, 3
print(f"Tuple without parentheses: {numbers}")

# ACCESSING TUPLE ELEMENTS
# Similar to lists - use indexing

point = (10, 20)
print(f"\nX coordinate: {point[0]}")
print(f"Y coordinate: {point[1]}")

# Tuple unpacking
x, y = point
print(f"Unpacked: x={x}, y={y}")

# Multiple values unpacking
person = ("Bob", 25, "Developer")
name, age, job = person
print(f"Unpacked: {name}, {age}, {job}")

# IMMUTABILITY
# Tuples cannot be modified after creation

point = (3, 4)
# point[0] = 5  # This would cause an error!
# point.append(5)  # This would cause an error!

# You can create a new tuple
point = (5, 4)  # This creates a new tuple
print(f"\nNew point: {point}")

# TUPLE OPERATIONS

# Concatenation (combining tuples)
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print(f"\nCombined tuples: {combined}")

# Repetition
repeated = (1, 2) * 3
print(f"Repeated tuple: {repeated}")

# Membership testing
numbers = (1, 2, 3, 4, 5)
print(f"\n3 in numbers: {3 in numbers}")
print(f"6 in numbers: {6 in numbers}")

# TUPLE METHODS
# Tuples have fewer methods than lists (because they're immutable)

numbers = (1, 2, 3, 2, 4, 2)

# count() - counts occurrences
print(f"\nCount of 2: {numbers.count(2)}")

# index() - finds first index
print(f"Index of 3: {numbers.index(3)}")

# WHEN TO USE TUPLES
# - When you want to ensure data cannot be changed
# - When you need a fixed collection of items
# - For returning multiple values from functions
# - As dictionary keys (lists can't be keys, but tuples can!)

def get_stats(numbers):
    """Returns min, max, and average as a tuple."""
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

stats = get_stats([1, 5, 3, 9, 2])
print(f"\nStats (min, max, avg): {stats}")

# Tuple as dictionary key
locations = {
    (0, 0): "Origin",
    (1, 2): "Point A",
    (3, 4): "Point B"
}
print(f"\nLocation at (1, 2): {locations[(1, 2)]}")

# ========================================
# SETS
# ========================================

# CREATING SETS
# Sets use curly braces {} (like dicts, but no colons)

# Empty set (must use set(), not {} - that's a dict!)
empty_set = set()
print(f"\nEmpty set: {empty_set}")

# Set with items
fruits = {"apple", "banana", "cherry"}
print(f"Fruits set: {fruits}")

# Set from a list (removes duplicates automatically!)
numbers_list = [1, 2, 2, 3, 3, 3, 4]
numbers_set = set(numbers_list)
print(f"List: {numbers_list}")
print(f"Set (unique only): {numbers_set}")

# UNIQUENESS
# Sets automatically contain only unique elements

numbers = {1, 2, 2, 3, 3, 4}
print(f"\nSet automatically removes duplicates: {numbers}")

# ADDING AND REMOVING ITEMS

# add() - adds single item
fruits.add("date")
print(f"\nAfter add('date'): {fruits}")

# update() - adds multiple items
fruits.update(["elderberry", "fig"])
print(f"After update: {fruits}")

# remove() - removes item (raises error if not found)
fruits.remove("banana")
print(f"After remove: {fruits}")

# discard() - removes item (no error if not found)
fruits.discard("banana")  # Safe even if not in set
print(f"After discard: {fruits}")

# pop() - removes and returns arbitrary element
removed = fruits.pop()
print(f"Popped: {removed}")
print(f"After pop: {fruits}")

# SET OPERATIONS

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union (all elements in either set)
union = set1 | set2  # or set1.union(set2)
print(f"\nSet1: {set1}")
print(f"Set2: {set2}")
print(f"Union: {union}")

# Intersection (elements in both sets)
intersection = set1 & set2  # or set1.intersection(set2)
print(f"Intersection: {intersection}")

# Difference (elements in set1 but not in set2)
difference = set1 - set2  # or set1.difference(set2)
print(f"Difference (set1 - set2): {difference}")

# Symmetric Difference (elements in either set, but not both)
sym_diff = set1 ^ set2  # or set1.symmetric_difference(set2)
print(f"Symmetric difference: {sym_diff}")

# SUBSET AND SUPERSET
set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}

print(f"\nset_a: {set_a}")
print(f"set_b: {set_b}")
print(f"set_a is subset of set_b: {set_a.issubset(set_b)}")
print(f"set_b is superset of set_b: {set_b.issuperset(set_a)}")

# MEMBERSHIP TESTING
numbers = {1, 2, 3, 4, 5}
print(f"\n3 in numbers: {3 in numbers}")
print(f"6 in numbers: {6 in numbers}")

# ITERATING OVER SETS
fruits = {"apple", "banana", "cherry"}
print("\nIterating over set:")
for fruit in fruits:
    print(f"  {fruit}")

# SET COMPREHENSION
squares = {x**2 for x in range(1, 6)}
print(f"\nSet comprehension (squares): {squares}")

