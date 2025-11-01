"""
09_dictionaries.py

This file demonstrates dictionaries in Python.
Dictionaries store key-value pairs. They are unordered (in Python < 3.7),
mutable, and allow fast lookups by key.
"""

# CREATING DICTIONARIES
# Dictionaries use curly braces {} with key:value pairs

# Empty dictionary
empty_dict = {}
print("Empty dict:", empty_dict)

# Dictionary with key-value pairs
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print("Person dictionary:", person)

# Alternative way to create
person2 = dict(name="Bob", age=25, city="Boston")
print("Person2 dictionary:", person2)

# ACCESSING VALUES
# Access values using square brackets with the key

print(f"\nName: {person['name']}")
print(f"Age: {person['age']}")

# Using .get() method (safer - returns None if key doesn't exist)
print(f"Name: {person.get('name')}")
print(f"Email: {person.get('email')}")  # Returns None
print(f"Email: {person.get('email', 'Not provided')}")  # Returns default value

# MODIFYING DICTIONARIES

# Add new key-value pair
person["email"] = "alice@example.com"
print(f"\nAfter adding email: {person}")

# Update existing value
person["age"] = 31
print(f"After updating age: {person}")

# Update multiple values at once
person.update({"city": "Los Angeles", "phone": "555-1234"})
print(f"After update(): {person}")

# REMOVING ITEMS

# del statement
del person["phone"]
print(f"\nAfter del: {person}")

# pop() - removes and returns value
email = person.pop("email")
print(f"Popped email: {email}")
print(f"After pop: {person}")

# popitem() - removes and returns last item (key, value) tuple
last_item = person.popitem()
print(f"Popped item: {last_item}")
print(f"After popitem: {person}")

# clear() - removes all items
person.clear()
print(f"After clear: {person}")

# DICTIONARY METHODS

person = {"name": "Charlie", "age": 28, "city": "Chicago"}

# keys() - returns all keys
print(f"\nKeys: {list(person.keys())}")

# values() - returns all values
print(f"Values: {list(person.values())}")

# items() - returns all key-value pairs as tuples
print(f"Items: {list(person.items())}")

# Iterating over dictionaries
print("\nIterating over keys:")
for key in person:
    print(f"{key}: {person[key]}")

print("\nIterating over items:")
for key, value in person.items():
    print(f"{key}: {value}")

# CHECKING IF KEY EXISTS
print(f"\n'name' in person: {'name' in person}")
print(f"'email' in person: {'email' in person}")

# DICTIONARY COMPREHENSION
# Create dictionary from iterable

# Squares dictionary
squares = {x: x**2 for x in range(1, 6)}
print(f"\nSquares dict: {squares}")

# Filter dictionary
numbers = {"a": 1, "b": 2, "c": 3, "d": 4}
even_only = {k: v for k, v in numbers.items() if v % 2 == 0}
print(f"Even numbers only: {even_only}")

# NESTED DICTIONARIES
# Dictionaries can contain other dictionaries

students = {
    "student1": {
        "name": "Alice",
        "grades": [85, 90, 88]
    },
    "student2": {
        "name": "Bob",
        "grades": [78, 82, 80]
    }
}

print(f"\nNested dictionary: {students}")
print(f"Student1 name: {students['student1']['name']}")
print(f"Student1 grades: {students['student1']['grades']}")

# COPYING DICTIONARIES
# Same issue as lists - need to use .copy() or dict()

original = {"a": 1, "b": 2}
copy_wrong = original  # Both reference same dict!
copy_wrong["c"] = 3
print(f"\nOriginal: {original}")  # Also has 'c'!

original = {"a": 1, "b": 2}
copy_correct = original.copy()
copy_correct["c"] = 3
print(f"Original: {original}")
print(f"Copy: {copy_correct}")

# COMBINING DICTIONARIES
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Using update()
dict1.update(dict2)
print(f"\nCombined with update(): {dict1}")

# Using ** unpacking (Python 3.5+)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
combined = {**dict1, **dict2}
print(f"Combined with **: {combined}")

