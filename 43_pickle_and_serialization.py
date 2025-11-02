"""
43_pickle_and_serialization.py

This file demonstrates serialization in Python.
Covers pickle, JSON, and other serialization formats.
Serialization converts objects to byte streams for storage or transmission.
"""

import pickle
import json
import dill  # Extended pickle - may need: pip install dill

# PICKLE - Python Object Serialization
# Serialize Python objects to byte streams

print("SERIALIZATION IN PYTHON")
print("=" * 50)

# Basic pickle usage
data = {
    "name": "Alice",
    "age": 30,
    "hobbies": ["reading", "coding"]
}

# Serialize (pickle) to bytes
print("1. Basic Pickle:")
pickled_data = pickle.dumps(data)
print(f"   Original: {data}")
print(f"   Pickled size: {len(pickled_data)} bytes")

# Deserialize (unpickle) from bytes
unpickled_data = pickle.loads(pickled_data)
print(f"   Unpickled: {unpickled_data}\n")

# Pickle to file
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

# Unpickle from file
with open("data.pkl", "rb") as f:
    loaded_data = pickle.load(f)

print(f"   Loaded from file: {loaded_data}")
print("   (data.pkl file created)\n")

# CUSTOM OBJECTS
# Pickle user-defined classes

class Person:
    """Custom class for pickling."""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

person = Person("Bob", 25)

print("2. Pickling Custom Objects:")
pickled_person = pickle.dumps(person)
unpickled_person = pickle.loads(pickled_person)
print(f"   Original: {person}")
print(f"   Unpickled: {unpickled_person}")
print(f"   Are equal: {person.name == unpickled_person.name}\n")

# PICKLE PROTOCOLS
# Different pickle protocol versions

print("3. Pickle Protocols:")
protocols = [0, 1, 2, 3, 4, 5]

for protocol in protocols:
    try:
        data_bytes = pickle.dumps(data, protocol=protocol)
        print(f"   Protocol {protocol}: {len(data_bytes)} bytes")
    except ValueError:
        print(f"   Protocol {protocol}: Not available")

print("   (Higher protocols are more efficient)\n")

# PICKLE CUSTOM SERIALIZATION
# Control how objects are pickled

class CustomPickle:
    """Class with custom pickle behavior."""
    
    def __init__(self, value):
        self.value = value
        self._temp = "not saved"
    
    def __getstate__(self):
        """Custom state for pickling."""
        state = self.__dict__.copy()
        # Don't save _temp
        del state['_temp']
        return state
    
    def __setstate__(self, state):
        """Restore state when unpickling."""
        self.__dict__.update(state)
        self._temp = "restored"

obj = CustomPickle("test")
print("4. Custom Pickle Methods:")
print(f"   Original _temp: {obj._temp}")

pickled = pickle.dumps(obj)
restored = pickle.loads(pickled)

print(f"   Restored _temp: {restored._temp}\n")

# JSON SERIALIZATION
# Human-readable, language-agnostic

print("5. JSON Serialization:")
json_data = {
    "name": "Alice",
    "age": 30,
    "active": True,
    "scores": [95, 87, 92]
}

json_string = json.dumps(json_data, indent=2)
print("   JSON string:")
print(json_string)

# Parse JSON
parsed = json.loads(json_string)
print(f"\n   Parsed: {parsed}\n")

# JSON TO/FROM FILE
with open("data.json", "w") as f:
    json.dump(json_data, f, indent=2)

with open("data.json", "r") as f:
    loaded_json = json.load(f)

print(f"   Loaded from JSON file: {loaded_json}\n")

# JSON WITH CUSTOM OBJECTS
# Use custom encoders/decoders

class PersonEncoder(json.JSONEncoder):
    """Custom JSON encoder for Person."""
    
    def default(self, obj):
        if isinstance(obj, Person):
            return {"__person__": True, "name": obj.name, "age": obj.age}
        return super().default(obj)

def person_decoder(dct):
    """Custom JSON decoder for Person."""
    if "__person__" in dct:
        return Person(dct["name"], dct["age"])
    return dct

person = Person("Charlie", 35)
person_json = json.dumps(person, cls=PersonEncoder)
print("6. JSON with Custom Objects:")
print(f"   Person JSON: {person_json}")

# Note: Custom decoder needs object_hook when loading
# person_restored = json.loads(person_json, object_hook=person_decoder)
print()

# COMPARISON: PICKLE vs JSON
print("7. Pickle vs JSON:")

comparison_data = {
    "pickle": {
        "pros": ["Handles any Python object", "Preserves object types", "Can serialize functions"],
        "cons": ["Python-specific", "Security risks", "Not human-readable"]
    },
    "json": {
        "pros": ["Human-readable", "Language-agnostic", "Secure", "Widely supported"],
        "cons": ["Limited to basic types", "No function serialization"]
    }
}

for fmt, details in comparison_data.items():
    print(f"   {fmt.upper()}:")
    print(f"     Pros: {', '.join(details['pros'])}")
    print(f"     Cons: {', '.join(details['cons'])}")

print()

# DILL - Extended Pickle
# Serialize more types (functions, lambdas, etc.)

def example_function(x):
    """Function to serialize."""
    return x * 2

try:
    print("8. Dill (Extended Pickle):")
    # Serialize function with dill
    dill_data = dill.dumps(example_function)
    restored_func = dill.loads(dill_data)
    
    print(f"   Function serialized: {len(dill_data)} bytes")
    print(f"   Restored function result: {restored_func(5)}")
    print()
except ImportError:
    print("8. Dill: Install with 'pip install dill' for function serialization\n")

# SERIALIZATION FORMATS COMPARISON

print("9. Serialization Formats:")

formats = {
    "pickle": "Python objects → binary",
    "json": "Python dict/list → text",
    "yaml": "Python objects → text (human-readable)",
    "msgpack": "Python objects → binary (compact)",
    "protobuf": "Structured data → binary (efficient)",
    "xml": "Python objects → XML text"
}

for fmt, desc in formats.items():
    print(f"   {fmt}: {desc}")

print()

# SECURITY WARNING
print("10. Security Warning:")
print("    ⚠️  NEVER unpickle data from untrusted sources!")
print("    ⚠️  Pickle can execute arbitrary code!")
print("    ✓  Use JSON for untrusted data")
print("    ✓  Use pickle only for trusted sources")
print()

# SERIALIZATION PATTERNS

class Serializable:
    """Base class for serialization."""
    
    def to_dict(self):
        """Convert to dictionary."""
        return self.__dict__
    
    @classmethod
    def from_dict(cls, data):
        """Create from dictionary."""
        return cls(**data)

class User(Serializable):
    """User class with serialization."""
    
    def __init__(self, name, email):
        self.name = name
        self.email = email

user = User("Alice", "alice@example.com")
print("11. Serialization Pattern:")
user_dict = user.to_dict()
print(f"   To dict: {user_dict}")

user_restored = User.from_dict(user_dict)
print(f"   Restored: {user_restored.to_dict()}\n")

# PICKLE WITH COMPRESSION
# Compress pickled data

import gzip

print("12. Compressed Pickle:")
# Pickle and compress
pickled = pickle.dumps(data)
compressed = gzip.compress(pickled)

print(f"   Original size: {len(pickled)} bytes")
print(f"   Compressed size: {len(compressed)} bytes")
print(f"   Compression ratio: {len(compressed)/len(pickled):.2%}\n")

# STREAMING SERIALIZATION
# Serialize multiple objects

print("13. Streaming Serialization:")

objects = [Person("Alice", 30), Person("Bob", 25), Person("Charlie", 35)]

# Serialize multiple objects
with open("persons.pkl", "wb") as f:
    for obj in objects:
        pickle.dump(obj, f)

# Deserialize multiple objects
loaded_objects = []
with open("persons.pkl", "rb") as f:
    while True:
        try:
            obj = pickle.load(f)
            loaded_objects.append(obj)
        except EOFError:
            break

print(f"   Serialized {len(objects)} objects")
print(f"   Loaded {len(loaded_objects)} objects\n")

# BEST PRACTICES
print("14. Best Practices:")
print("   ✓ Use JSON for data exchange")
print("   ✓ Use pickle for Python-only applications")
print("   ✓ Never unpickle untrusted data")
print("   ✓ Use protocols 4+ for better performance")
print("   ✓ Handle serialization errors gracefully")
print("   ✓ Version your serialization format")
print()

# CLEANUP
import os
for file in ["data.pkl", "data.json", "persons.pkl"]:
    if os.path.exists(file):
        os.remove(file)
        print(f"   Cleaned up {file}")

print("\nSerialization demonstration complete!")
print("\nKey points:")
print("  - pickle: Python-specific, handles any object")
print("  - json: Universal, secure, human-readable")
print("  - Choose based on use case and security needs")

