"""
41_profiling.py

This file demonstrates profiling in Python.
Profiling helps identify performance bottlenecks and optimize code.
Covers cProfile, timeit, and optimization techniques.
"""

import cProfile
import pstats
import timeit
import functools

# TIMEIT MODULE
# Measure execution time of small code snippets

print("PROFILING IN PYTHON")
print("=" * 50)

# Basic timeit usage
def simple_function():
    return sum(range(1000))

# Time a single statement
time_taken = timeit.timeit('sum(range(1000))', number=1000)
print(f"1. timeit - Single statement: {time_taken:.6f} seconds (1000 runs)\n")

# Time a function
time_taken = timeit.timeit(simple_function, number=1000)
print(f"   timeit - Function call: {time_taken:.6f} seconds (1000 runs)\n")

# Compare two approaches
list_comp = timeit.timeit('[x**2 for x in range(100)]', number=10000)
map_comp = timeit.timeit('list(map(lambda x: x**2, range(100)))', number=10000)

print("2. Comparing approaches:")
print(f"   List comprehension: {list_comp:.6f} seconds")
print(f"   Map + lambda: {map_comp:.6f} seconds")
print(f"   Winner: {'List comprehension' if list_comp < map_comp else 'Map'}\n")

# CPROFILE
# Detailed profiling of function calls

def slow_function():
    """Function with performance issues."""
    result = []
    for i in range(1000):
        result.append(i ** 2)
    return result

def fast_function():
    """Optimized version."""
    return [i ** 2 for i in range(1000)]

# Profile a function
print("3. cProfile - Profiling functions:")
profiler = cProfile.Profile()
profiler.enable()

for _ in range(100):
    slow_function()

profiler.disable()

# Create stats object
stats = pstats.Stats(profiler)
print("   Slow function profile (top 5 calls):")
stats.sort_stats('cumulative')
stats.print_stats(5)
print()

# PROFILE DECORATOR
# Easy way to profile functions

def profile_decorator(func):
    """Decorator to profile function execution."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        profiler = cProfile.Profile()
        profiler.enable()
        result = func(*args, **kwargs)
        profiler.disable()
        
        stats = pstats.Stats(profiler)
        stats.sort_stats('cumulative')
        print(f"Profile of {func.__name__}:")
        stats.print_stats(3)
        
        return result
    return wrapper

@profile_decorator
def example_function(n):
    """Example function to profile."""
    total = 0
    for i in range(n):
        total += i ** 2
    return total

print("4. Profile decorator:")
example_function(1000)
print()

# MEMORY PROFILING (concept)
# Note: Requires memory_profiler package

memory_profiling_info = """
5. Memory Profiling:
   Install: pip install memory-profiler
   
   @profile
   def my_function():
       data = [0] * 1000000
       return data
   
   Run: python -m memory_profiler script.py
"""

print(memory_profiling_info)

# LINE PROFILER (concept)
# Profile line by line

line_profiler_info = """
6. Line Profiling:
   Install: pip install line_profiler
   
   @profile
   def my_function():
       # Code to profile
       pass
   
   Run: kernprof -l -v script.py
"""

print(line_profiler_info)

# OPTIMIZATION TECHNIQUES
# Common performance improvements

# 1. Use list comprehensions
def slow_list_creation():
    result = []
    for i in range(1000):
        result.append(i * 2)
    return result

def fast_list_creation():
    return [i * 2 for i in range(1000)]

print("7. Optimization Techniques:")
print("   List comprehension vs loop:")

time_slow = timeit.timeit(slow_list_creation, number=1000)
time_fast = timeit.timeit(fast_list_creation, number=1000)
print(f"   Slow: {time_slow:.6f}s")
print(f"   Fast: {time_fast:.6f}s")
print(f"   Speedup: {time_slow/time_fast:.2f}x\n")

# 2. Use built-in functions
def slow_sum():
    total = 0
    for i in range(1000):
        total += i
    return total

def fast_sum():
    return sum(range(1000))

time_slow = timeit.timeit(slow_sum, number=1000)
time_fast = timeit.timeit(fast_sum, number=1000)
print("   Built-in sum vs manual loop:")
print(f"   Slow: {time_slow:.6f}s")
print(f"   Fast: {time_fast:.6f}s")
print(f"   Speedup: {time_slow/time_fast:.2f}x\n")

# 3. Cache results (memoization)
@functools.lru_cache(maxsize=128)
def fibonacci_cached(n):
    """Fibonacci with caching."""
    if n < 2:
        return n
    return fibonacci_cached(n-1) + fibonacci_cached(n-2)

def fibonacci_uncached(n):
    """Fibonacci without caching."""
    if n < 2:
        return n
    return fibonacci_uncached(n-1) + fibonacci_uncached(n-2)

print("   Caching (memoization):")
time_uncached = timeit.timeit(lambda: fibonacci_uncached(20), number=1)
time_cached = timeit.timeit(lambda: fibonacci_cached(20), number=1)
print(f"   Uncached: {time_uncached:.6f}s")
print(f"   Cached: {time_cached:.6f}s")
if time_uncached > 0:
    print(f"   Speedup: {time_uncached/time_cached:.2f}x\n")

# 4. Avoid global lookups
def slow_global():
    """Function with global lookup."""
    result = []
    for i in range(1000):
        result.append(len(str(i)))  # Global len lookup
    return result

def fast_local():
    """Function with local lookup."""
    local_len = len  # Local reference
    result = []
    for i in range(1000):
        result.append(local_len(str(i)))
    return result

print("   Local vs global lookups:")
time_slow = timeit.timeit(slow_global, number=100)
time_fast = timeit.timeit(fast_local, number=100)
print(f"   Global: {time_slow:.6f}s")
print(f"   Local: {time_fast:.6f}s")
if time_fast > 0:
    print(f"   Speedup: {time_slow/time_fast:.2f}x\n")

# 5. String concatenation
def slow_string_concat():
    """Slow string concatenation."""
    result = ""
    for i in range(100):
        result += str(i)
    return result

def fast_string_concat():
    """Fast string concatenation."""
    return "".join(str(i) for i in range(100))

print("   String concatenation:")
time_slow = timeit.timeit(slow_string_concat, number=1000)
time_fast = timeit.timeit(fast_string_concat, number=1000)
print(f"   += operator: {time_slow:.6f}s")
print(f"   join(): {time_fast:.6f}s")
print(f"   Speedup: {time_slow/time_fast:.2f}x\n")

# PROFILE MAIN PROGRAM
# Profile entire script

def profile_main():
    """Example of profiling main execution."""
    
    def operation1():
        return sum(range(1000))
    
    def operation2():
        return [x**2 for x in range(100)]
    
    # Profile multiple operations
    profiler = cProfile.Profile()
    profiler.enable()
    
    for _ in range(100):
        operation1()
        operation2()
    
    profiler.disable()
    return profiler

print("8. Profiling main program:")
print("   Use: python -m cProfile script.py")
print("   Or: cProfile.run('main()')\n")

# STATS ANALYSIS
# Analyze profile statistics

def analyze_profile(profiler):
    """Analyze profile statistics."""
    stats = pstats.Stats(profiler)
    
    print("9. Profile Statistics:")
    print("   Total calls:", stats.total_calls)
    print("   Primitive calls:", stats.prim_calls)
    print("   Total time:", f"{stats.total_tt:.6f}s")
    print()

# TIMING CONTEXT MANAGER
# Convenient way to time code blocks

from contextlib import contextmanager
import time

@contextmanager
def timer():
    """Context manager for timing code."""
    start = time.perf_counter()
    try:
        yield
    finally:
        end = time.perf_counter()
        print(f"   Execution time: {end - start:.6f} seconds")

print("10. Timing context manager:")
with timer():
    sum(range(100000))

print()

# BEST PRACTICES
print("11. Profiling Best Practices:")
print("   ✓ Profile before optimizing (measure, don't guess)")
print("   ✓ Focus on hotspots (20/80 rule)")
print("   ✓ Use appropriate profiling tools for the job")
print("   ✓ Profile with realistic data sizes")
print("   ✓ Compare before/after when optimizing")
print("   ✓ Consider algorithm complexity, not just implementation")
print()

print("Profiling demonstration complete!")
print("\nTo profile a script:")
print("  python -m cProfile script.py")
print("  python -m cProfile -o profile.stats script.py")
print("  python -c 'import pstats; pstats.Stats(\"profile.stats\").print_stats()'")

