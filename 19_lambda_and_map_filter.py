"""
19_lambda_and_map_filter.py

This file demonstrates lambda functions and the map(), filter(), and reduce() functions.
These are functional programming tools that help write concise, expressive code.
"""

# LAMBDA FUNCTIONS
# Anonymous functions defined with the lambda keyword
# Syntax: lambda arguments: expression

# Traditional function
def square(x):
    return x ** 2

# Lambda equivalent
square_lambda = lambda x: x ** 2

print("Square of 5:", square(5))
print("Square of 5 (lambda):", square_lambda(5))

# Lambda with multiple arguments
add = lambda x, y: x + y
print(f"\nAdd 3 and 4: {add(3, 4)}")

# Lambda with no arguments
greet = lambda: "Hello, World!"
print(f"Greet: {greet()}")

# MAP() FUNCTION
# Applies a function to all items in an iterable
# Syntax: map(function, iterable)

# Traditional way
numbers = [1, 2, 3, 4, 5]
squared_traditional = []
for num in numbers:
    squared_traditional.append(num ** 2)
print(f"\nTraditional squares: {squared_traditional}")

# Using map with regular function
def square_func(x):
    return x ** 2

squared_map = list(map(square_func, numbers))
print(f"Squares with map: {squared_map}")

# Using map with lambda
squared_lambda = list(map(lambda x: x ** 2, numbers))
print(f"Squares with map+lambda: {squared_lambda}")

# Map with multiple iterables
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
summed = list(map(lambda x, y: x + y, numbers1, numbers2))
print(f"\nSum of two lists: {summed}")

# Map with strings
words = ["hello", "world", "python"]
lengths = list(map(len, words))
print(f"Word lengths: {lengths}")

uppercase = list(map(str.upper, words))
print(f"Uppercase words: {uppercase}")

# FILTER() FUNCTION
# Filters items from an iterable based on a condition
# Syntax: filter(function, iterable)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Traditional way
evens_traditional = []
for num in numbers:
    if num % 2 == 0:
        evens_traditional.append(num)
print(f"\nTraditional evens: {evens_traditional}")

# Using filter with regular function
def is_even(x):
    return x % 2 == 0

evens_filter = list(filter(is_even, numbers))
print(f"Evens with filter: {evens_filter}")

# Using filter with lambda
evens_lambda = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Evens with filter+lambda: {evens_lambda}")

# Filter strings
words = ["apple", "banana", "cherry", "date", "elderberry"]
long_words = list(filter(lambda word: len(word) > 5, words))
print(f"\nLong words: {long_words}")

# REDUCE() FUNCTION
# Applies a function cumulatively to items in an iterable
# Syntax: reduce(function, iterable[, initializer])
# Note: Need to import from functools

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Traditional way
sum_traditional = 0
for num in numbers:
    sum_traditional += num
print(f"\nTraditional sum: {sum_traditional}")

# Using reduce
sum_reduce = reduce(lambda x, y: x + y, numbers)
print(f"Sum with reduce: {sum_reduce}")

# Product of numbers
product = reduce(lambda x, y: x * y, numbers)
print(f"Product: {product}")

# Find maximum
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(f"Maximum: {maximum}")

# With initial value
sum_with_init = reduce(lambda x, y: x + y, numbers, 10)
print(f"Sum with initial 10: {sum_with_init}")

# COMBINING MAP, FILTER, AND REDUCE

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Square even numbers and sum them
result = reduce(
    lambda x, y: x + y,
    map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers))
)
print(f"\nSum of squares of even numbers: {result}")

# Break it down:
# 1. Filter: get even numbers [2, 4, 6, 8, 10]
# 2. Map: square them [4, 16, 36, 64, 100]
# 3. Reduce: sum them = 220

# LAMBDA IN SORTING

# Sort by length
words = ["apple", "pear", "banana", "kiwi"]
sorted_by_length = sorted(words, key=lambda x: len(x))
print(f"\nWords sorted by length: {sorted_by_length}")

# Sort by second character
sorted_by_second = sorted(words, key=lambda x: x[1])
print(f"Words sorted by second character: {sorted_by_second}")

# Sort list of tuples
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
sorted_by_age = sorted(people, key=lambda x: x[1])
print(f"\nPeople sorted by age: {sorted_by_age}")

# LAMBDA IN OTHER FUNCTIONS

# With max() and min()
words = ["apple", "banana", "cherry"]
longest = max(words, key=lambda x: len(x))
shortest = min(words, key=lambda x: len(x))
print(f"\nLongest word: {longest}")
print(f"Shortest word: {shortest}")

# WHEN TO USE LAMBDA
# Good for:
# - Simple, one-line functions
# - Functions used only once
# - Callbacks and event handlers
# - With map, filter, reduce, sorted, etc.

# Avoid for:
# - Complex logic (use regular functions)
# - Functions that need documentation
# - Functions reused multiple times
# - When readability suffers

# ALTERNATIVE: LIST COMPREHENSIONS
# Often more readable than map/filter

numbers = [1, 2, 3, 4, 5]

# map equivalent
squared_map = list(map(lambda x: x ** 2, numbers))
squared_comp = [x ** 2 for x in numbers]
print(f"\nMap: {squared_map}")
print(f"Comprehension: {squared_comp}")

# filter equivalent
evens_filter = list(filter(lambda x: x % 2 == 0, numbers))
evens_comp = [x for x in numbers if x % 2 == 0]
print(f"\nFilter: {evens_filter}")
print(f"Comprehension: {evens_comp}")

# Combined
result_map_filter = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
result_comp = [x ** 2 for x in numbers if x % 2 == 0]
print(f"\nMap+Filter: {result_map_filter}")
print(f"Comprehension: {result_comp}")

