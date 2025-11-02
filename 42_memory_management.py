"""
42_memory_management.py

This file demonstrates memory management in Python.
Covers garbage collection, __slots__, weak references, memory optimization,
and understanding Python's memory model.
"""

import sys
import gc
import weakref
from pympler import asizeof  # Optional: pip install pympler

# PYTHON MEMORY MODEL
# Understanding how Python manages memory

print("MEMORY MANAGEMENT IN PYTHON")
print("=" * 50)

# Check object size
print("1. Object Sizes:")
print(f"   Integer: {sys.getsizeof(42)} bytes")
print(f"   String 'hello': {sys.getsizeof('hello')} bytes")
print(f"   Empty list: {sys.getsizeof([])} bytes")
print(f"   List with 10 items: {sys.getsizeof([0]*10)} bytes")
print(f"   Empty dict: {sys.getsizeof({})} bytes")
print(f"   Empty set: {sys.getsizeof(set())} bytes\n")

# GARBAGE COLLECTION
# Automatic memory management

print("2. Garbage Collection:")

# Check GC stats
gc_stats = gc.get_stats()
print(f"   GC generations: {len(gc_stats)}")
print(f"   GC enabled: {gc.isenabled()}\n")

# Manual GC control
print("   Manual GC control:")
print("   - gc.collect() - Force collection")
print("   - gc.disable() - Disable GC")
print("   - gc.enable() - Enable GC")
print("   - gc.get_count() - Get collection counts")
print(f"   Current counts: {gc.get_count()}\n")

# Force collection
collected = gc.collect()
print(f"   Objects collected: {collected}\n")

# REFERENCE COUNTING
# Python's primary memory management

import ctypes

def get_ref_count(obj):
    """Get reference count of object."""
    return ctypes.c_long.from_address(id(obj)).value

a = [1, 2, 3]
print("3. Reference Counting:")
print(f"   Initial ref count: {get_ref_count(a)}")

b = a  # New reference
print(f"   After assignment: {get_ref_count(a)}")

del b  # Remove reference
print(f"   After deletion: {get_ref_count(a)}\n")

# CIRCULAR REFERENCES
# When objects reference each other

class Node:
    """Node with circular reference."""
    
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __del__(self):
        print(f"   Deleting node {self.value}")

print("4. Circular References:")
node1 = Node(1)
node2 = Node(2)
node1.next = node2
node2.next = node1  # Circular reference

# Delete references
node1 = None
node2 = None

# Force GC to handle circular reference
collected = gc.collect()
print(f"   Collected {collected} objects with circular references\n")

# __SLOTS__
# Reduce memory usage by preventing __dict__

class RegularClass:
    """Regular class with __dict__."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

class SlotsClass:
    """Class using __slots__."""
    __slots__ = ['x', 'y']
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

regular = RegularClass(1, 2)
slots = SlotsClass(1, 2)

print("5. __slots__ Memory Optimization:")
print(f"   Regular class size: {sys.getsizeof(regular)} bytes")
print(f"   Slots class size: {sys.getsizeof(slots)} bytes")

# Check if has __dict__
print(f"   Regular has __dict__: {hasattr(regular, '__dict__')}")
print(f"   Slots has __dict__: {hasattr(slots, '__dict__')}\n")

# WEAK REFERENCES
# References that don't prevent garbage collection

class Data:
    """Class for weak reference example."""
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return f"Data({self.value})"

print("6. Weak References:")

# Strong reference
data = Data(42)
strong_ref = data

# Weak reference
weak_ref = weakref.ref(data)

print(f"   Strong ref: {strong_ref}")
print(f"   Weak ref: {weak_ref()}")
print(f"   Weak ref alive: {weak_ref() is not None}")

# Delete strong reference
del data

# Weak reference should be None now
print(f"   After deleting strong ref:")
print(f"   Weak ref: {weak_ref()}")
print(f"   Weak ref alive: {weak_ref() is not None}\n")

# WEAK VALUE DICTIONARY
# Dictionary with weak references to values

class WeakValueDictExample:
    """Example using WeakValueDictionary."""
    def __init__(self):
        self.cache = weakref.WeakValueDictionary()
    
    def get_or_create(self, key):
        """Get from cache or create new."""
        if key in self.cache:
            return self.cache[key]
        else:
            obj = Data(f"value_{key}")
            self.cache[key] = obj
            return obj

cache_example = WeakValueDictExample()
obj1 = cache_example.get_or_create(1)
obj2 = cache_example.get_or_create(2)

print("7. WeakValueDictionary:")
print(f"   Cache size: {len(cache_example.cache)}")

del obj1  # Remove strong reference
gc.collect()  # Allow GC to clean up

print(f"   After deleting obj1, cache size: {len(cache_example.cache)}\n")

# MEMORY-EFFICIENT DATA STRUCTURES
# Using generators and iterators

def memory_efficient_range(n):
    """Generator - memory efficient."""
    for i in range(n):
        yield i

print("8. Memory-Efficient Structures:")
regular_list = list(range(1000))
generator = memory_efficient_range(1000)

print(f"   List size: {sys.getsizeof(regular_list)} bytes")
print(f"   Generator size: {sys.getsizeof(generator)} bytes\n")

# COPY VS VIEW
# Understanding memory sharing

import copy

original = [1, 2, 3, [4, 5]]

# Shallow copy
shallow = copy.copy(original)
shallow[3].append(6)

print("9. Copy vs Reference:")
print(f"   Original after shallow copy modify: {original}")
print(f"   (Nested list is shared)\n")

# Deep copy
original2 = [1, 2, 3, [4, 5]]
deep = copy.deepcopy(original2)
deep[3].append(6)

print(f"   Original after deep copy modify: {original2}")
print(f"   (No sharing with deep copy)\n")

# MEMORY PROFILING (concept)
# Tools for analyzing memory usage

memory_tools_info = """
10. Memory Profiling Tools:
    
    tracemalloc (built-in):
        import tracemalloc
        tracemalloc.start()
        # ... your code ...
        snapshot = tracemalloc.take_snapshot()
        top_stats = snapshot.statistics('lineno')
    
    memory_profiler (external):
        pip install memory-profiler
        @profile
        def my_function():
            pass
    
    pympler (external):
        pip install pympler
        from pympler import asizeof
        size = asizeof.asizeof(obj)
"""

print(memory_tools_info)

# MEMORY OPTIMIZATION TECHNIQUES

print("11. Memory Optimization Techniques:")
print("   ✓ Use __slots__ for classes with many instances")
print("   ✓ Use generators for large sequences")
print("   ✓ Delete references when done")
print("   ✓ Use weak references for caches")
print("   ✓ Avoid circular references")
print("   ✓ Use appropriate data structures")
print("   ✓ Consider array.array for numeric data")
print()

# ARRAY MODULE
# More memory-efficient than lists for numeric data

import array

print("12. array Module (Memory Efficient):")
list_data = [1, 2, 3, 4, 5] * 1000
array_data = array.array('i', list_data)

print(f"   List size: {sys.getsizeof(list_data)} bytes")
print(f"   Array size: {sys.getsizeof(array_data)} bytes\n")

# STRING INTERNING
# Python reuses string objects

a = "hello"
b = "hello"
c = "hel" + "lo"

print("13. String Interning:")
print(f"   a is b: {a is b}")
print(f"   a is c: {a is c}")
print(f"   (Small strings are interned)\n")

# GARBAGE COLLECTION TUNING
# Adjust GC thresholds

print("14. GC Tuning:")
current_threshold = gc.get_threshold()
print(f"   Current thresholds: {current_threshold}")
print("   gc.set_threshold(threshold0, threshold1, threshold2)")
print("   Use carefully - usually not needed\n")

# MEMORY LEAKS
# Common causes and how to avoid

print("15. Avoiding Memory Leaks:")
print("   ✗ Circular references without __del__")
print("   ✗ Global variables holding references")
print("   ✗ Event handlers not removed")
print("   ✗ Caches that never clear")
print("   ✓ Use weak references for caches")
print("   ✓ Close resources properly")
print("   ✓ Remove event handlers")
print()

# BEST PRACTICES
print("16. Best Practices:")
print("   • Profile memory usage before optimizing")
print("   • Use appropriate data structures")
print("   • Understand reference counting vs GC")
print("   • Use __slots__ for high-instance-count classes")
print("   • Prefer generators for large sequences")
print("   • Clean up resources explicitly")
print()

print("Memory management demonstration complete!")
print("\nMemory analysis tools:")
print("  - sys.getsizeof() - Object size")
print("  - gc module - Garbage collection")
print("  - weakref - Weak references")
print("  - tracemalloc - Memory tracing")
print("  - memory_profiler - Line-by-line profiling")

