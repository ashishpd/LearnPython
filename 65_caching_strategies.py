"""
65_caching_strategies.py

This file demonstrates caching strategies in Python.
Covers functools.lru_cache, memoization patterns, and caching techniques.
"""

from functools import lru_cache

print("CACHING STRATEGIES")
print("=" * 50)

# LRU_CACHE
print("1. LRU Cache:")

@lru_cache(maxsize=128)
def expensive_function(n):
    return sum(i**2 for i in range(n))

result1 = expensive_function(1000)
result2 = expensive_function(1000)  # Cached

print(f"   Cache info: {expensive_function.cache_info()}\n")

# MANUAL CACHE
print("2. Manual Caching:")

cache = {}

def cached_function(key):
    if key not in cache:
        cache[key] = key ** 2
    return cache[key]

print(f"   {cached_function(5)}")
print(f"   Cache size: {len(cache)}\n")

print("Caching strategies demonstration complete!")

