"""
26_regular_expressions.py

This file demonstrates regular expressions (regex) in Python using the 're' module.
Regular expressions are patterns for matching text.
"""

import re

# BASIC PATTERN MATCHING
# re.search() - find first match

text = "The price is $19.99"

# Find pattern in text
match = re.search(r'\$\d+\.\d+', text)
if match:
    print(f"Found: {match.group()}")

# MATCHING AT START/END
# re.match() - match at beginning of string
# re.fullmatch() - match entire string

text = "Hello, World!"
if re.match(r'Hello', text):
    print("Starts with 'Hello'")

# FINDING ALL MATCHES
# re.findall() - find all matches

text = "Prices are $10.50, $25.99, and $5.00"
prices = re.findall(r'\$\d+\.\d+', text)
print(f"\nAll prices: {prices}")

# COMMON PATTERNS

# Digits
text = "Phone: 123-456-7890"
phone = re.search(r'\d{3}-\d{3}-\d{4}', text)
print(f"\nPhone: {phone.group() if phone else 'Not found'}")

# Email pattern (simplified)
email = "user@example.com"
if re.match(r'[\w\.-]+@[\w\.-]+\.\w+', email):
    print(f"Valid email: {email}")

# GROUPS AND CAPTURING
# Use parentheses to capture groups

text = "Date: 2023-12-25"
match = re.search(r'(\d{4})-(\d{2})-(\d{2})', text)
if match:
    print(f"\nFull match: {match.group()}")
    print(f"Year: {match.group(1)}")
    print(f"Month: {match.group(2)}")
    print(f"Day: {match.group(3)}")
    print(f"All groups: {match.groups()}")

# SUBSTITUTION
# re.sub() - replace matches

text = "Hello World"
new_text = re.sub(r'World', 'Python', text)
print(f"\nReplaced: {new_text}")

# Compile pattern for reuse
pattern = re.compile(r'\d+')
text = "I have 3 cats and 2 dogs"
numbers = pattern.findall(text)
print(f"\nNumbers: {numbers}")

