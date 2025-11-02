"""
51_collections_advanced.py

This file demonstrates advanced collections from the collections module.
Covers namedtuple, Counter, deque, defaultdict, ChainMap, and more.
"""

from collections import namedtuple, Counter, deque, defaultdict, ChainMap, OrderedDict
from typing import NamedTuple

print("ADVANCED COLLECTIONS IN PYTHON")
print("=" * 50)

# NAMEDTUPLE
# Tuple with named fields

print("1. namedtuple:")

# Create named tuple
Point = namedtuple("Point", ["x", "y"])
p1 = Point(10, 20)

print(f"   Point: {p1}")
print(f"   x: {p1.x}, y: {p1.y}")
print(f"   Index access: {p1[0]}, {p1[1]}")
print(f"   Unpacking: {', '.join(map(str, p1))}")

# Named tuple with methods
class Person(NamedTuple):
    """Person using NamedTuple."""
    name: str
    age: int
    
    def is_adult(self):
        return self.age >= 18

person = Person("Alice", 30)
print(f"   Person: {person.name}, adult: {person.is_adult()}\n")

# COUNTER
# Count hashable objects

print("2. Counter:")

# Count elements
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_count = Counter(words)
print(f"   Word counts: {word_count}")
print(f"   Most common: {word_count.most_common(2)}")

# Counter operations
counter1 = Counter(a=3, b=2, c=1)
counter2 = Counter(a=1, b=2, c=3)

print(f"   Counter1: {counter1}")
print(f"   Counter2: {counter2}")
print(f"   Addition: {counter1 + counter2}")
print(f"   Subtraction: {counter1 - counter2}\n")

# DEQUE
# Double-ended queue

print("3. deque (Double-ended Queue):")

dq = deque([1, 2, 3, 4])
print(f"   Initial: {dq}")

# Add to ends
dq.appendleft(0)
dq.append(5)
print(f"   After append: {dq}")

# Remove from ends
left = dq.popleft()
right = dq.pop()
print(f"   Popped left: {left}, right: {right}")
print(f"   Remaining: {dq}")

# Rotate
dq.rotate(1)
print(f"   Rotated: {dq}\n")

# DEFAULTDICT
# Dictionary with default factory

print("4. defaultdict:")

# Default factory function
def default_factory():
    return "N/A"

dd = defaultdict(default_factory)
dd["name"] = "Alice"
print(f"   Name: {dd['name']}")
print(f"   Missing key: {dd['missing']}")

# Common pattern: defaultdict(list)
dd_list = defaultdict(list)
dd_list["fruits"].append("apple")
dd_list["fruits"].append("banana")
print(f"   Fruits: {dd_list['fruits']}")

# Common pattern: defaultdict(int) for counting
dd_count = defaultdict(int)
for word in ["a", "b", "a", "c", "b"]:
    dd_count[word] += 1
print(f"   Counts: {dict(dd_count)}\n")

# ORDEREDDICT
# Dictionary that remembers insertion order

print("5. OrderedDict:")

# Note: Python 3.7+ dicts are ordered by default
# OrderedDict is still useful for extra features

od = OrderedDict()
od["first"] = 1
od["second"] = 2
od["third"] = 3
print(f"   Ordered: {list(od.keys())}")

# Move to end
od.move_to_end("first")
print(f"   After move_to_end: {list(od.keys())}")

# Pop item
last = od.popitem(last=True)
print(f"   Popped last: {last}\n")

# CHAINMAP
# Chain multiple mappings

print("6. ChainMap:")

# Chain multiple dictionaries
defaults = {"theme": "light", "language": "en"}
user_prefs = {"theme": "dark"}
system_config = {"language": "fr"}

chain = ChainMap(user_prefs, defaults, system_config)
print(f"   ChainMap: {dict(chain)}")
print(f"   Theme (from user_prefs): {chain['theme']}")
print(f"   Language (from defaults): {chain['language']}")

# Update affects first mapping only
chain["theme"] = "auto"
print(f"   After update: {dict(user_prefs)}\n")

# PRACTICAL EXAMPLES

print("7. Practical Examples:")

# Group items by category
items = [("fruit", "apple"), ("fruit", "banana"), ("vegetable", "carrot")]
grouped = defaultdict(list)
for category, item in items:
    grouped[category].append(item)
print(f"   Grouped: {dict(grouped)}")

# Find most frequent items
text = "hello world hello python world"
word_freq = Counter(text.split())
print(f"   Most frequent words: {word_freq.most_common(2)}")

# Efficient queue operations
queue = deque()
queue.append("task1")
queue.append("task2")
print(f"   Queue: {list(queue)}")
print(f"   Process: {queue.popleft()}\n")

# COMPARISON WITH STANDARD TYPES

print("8. When to Use Each:")
print("   namedtuple: Immutable data structures")
print("   Counter: Counting items")
print("   deque: Fast append/pop at both ends")
print("   defaultdict: Dictionary with defaults")
print("   ChainMap: Search multiple mappings")
print("   OrderedDict: Need order features (Python < 3.7) or move_to_end()\n")

print("Advanced collections demonstration complete!")

