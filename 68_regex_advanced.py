"""
68_regex_advanced.py

This file demonstrates advanced regular expressions.
Covers complex patterns, optimization, and advanced regex features.
"""

import re

print("ADVANCED REGULAR EXPRESSIONS")
print("=" * 50)

# NAMED GROUPS
print("1. Named Groups:")

pattern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"
match = re.search(pattern, "2023-12-25")

if match:
    print(f"   Year: {match.group('year')}")
    print(f"   Month: {match.group('month')}")
    print(f"   Day: {match.group('day')}\n")

# COMPILED PATTERNS
print("2. Compiled Patterns:")

compiled = re.compile(r"\d+")
results = compiled.findall("There are 5 apples and 10 oranges")
print(f"   Numbers: {results}\n")

print("Advanced regex demonstration complete!")

