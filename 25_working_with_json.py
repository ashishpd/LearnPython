"""
25_working_with_json.py

This file demonstrates working with JSON in Python.
JSON (JavaScript Object Notation) is a common data interchange format.
"""

import json

# ENCODING (PYTHON TO JSON)
# json.dumps() - convert Python object to JSON string

data = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "coding", "hiking"],
    "married": False
}

json_string = json.dumps(data)
print("JSON string:")
print(json_string)

# Pretty printing with indentation
pretty_json = json.dumps(data, indent=2)
print("\nPretty JSON:")
print(pretty_json)

# Sort keys
sorted_json = json.dumps(data, indent=2, sort_keys=True)
print("\nSorted keys:")
print(sorted_json)

# DECODING (JSON TO PYTHON)
# json.loads() - convert JSON string to Python object

json_data = '{"name": "Bob", "age": 25, "city": "Boston"}'
python_obj = json.loads(json_data)
print(f"\nPython object: {python_obj}")
print(f"Type: {type(python_obj)}")
print(f"Name: {python_obj['name']}")

# READING JSON FROM FILE
# json.load() - read from file and parse

# Write JSON to file
with open("data.json", "w") as file:
    json.dump(data, file, indent=2)

# Read JSON from file
with open("data.json", "r") as file:
    loaded_data = json.load(file)

print(f"\nLoaded data: {loaded_data}")

# HANDLING NESTED DATA

nested_data = {
    "users": [
        {"name": "Alice", "scores": [85, 90, 88]},
        {"name": "Bob", "scores": [78, 82, 80]}
    ]
}

json_string = json.dumps(nested_data, indent=2)
print("\nNested JSON:")
print(json_string)

# CUSTOM ENCODING (complex objects)
# Use default parameter for custom serialization

from datetime import datetime

class Person:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date

def custom_encoder(obj):
    """Custom JSON encoder for Person objects."""
    if isinstance(obj, Person):
        return {
            "name": obj.name,
            "birth_date": obj.birth_date.isoformat()
        }
    raise TypeError(f"Object {obj} is not JSON serializable")

person = Person("Alice", datetime(1990, 5, 15))
person_json = json.dumps(person, default=custom_encoder)
print(f"\nCustom encoded: {person_json}")

# ERROR HANDLING

try:
    invalid_json = "{'name': 'Alice'}"  # Single quotes are invalid JSON
    data = json.loads(invalid_json)
except json.JSONDecodeError as e:
    print(f"\nJSON Error: {e}")

