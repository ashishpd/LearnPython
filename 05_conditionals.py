"""
05_conditionals.py

This file demonstrates conditional statements (if/elif/else) in Python.
Conditionals allow your program to make decisions and execute different
code based on different conditions.
"""

# IF STATEMENT
# The if statement executes code only if a condition is True

age = 18
if age >= 18:
    print("You are an adult!")  # Output: You are an adult!
    print("You can vote.")  # Output: You can vote.

# Note: In Python, indentation is crucial!
# Code inside the if block must be indented (typically 4 spaces)
# Everything at the same indentation level is part of the same block

# IF-ELSE STATEMENT
# Execute one block if condition is True, another if False

print("\n" + "="*50)  # Output: ==================================================
temperature = 75
if temperature > 70:
    print("It's warm outside!")  # Output: It's warm outside!
else:
    print("It's cool outside!")

# COMPARISON OPERATORS
# ==  equals
# !=  not equals
# <   less than
# >   greater than
# <=  less than or equal to
# >=  greater than or equal to

print("\n" + "="*50)  # Output: ==================================================
x = 10
y = 5

if x == y:
    print("x equals y")
elif x > y:
    print("x is greater than y")  # Output: x is greater than y
else:
    print("x is less than y")

# IF-ELIF-ELSE (multiple conditions)
# Check multiple conditions in order

print("\n" + "="*50)  # Output: ==================================================
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")  # Output: Score: 85, Grade: B

# LOGICAL OPERATORS
# and - both conditions must be True
# or  - at least one condition must be True
# not - reverses the condition

print("\n" + "="*50)  # Output: ==================================================
age = 25
has_license = True

# Using 'and'
if age >= 18 and has_license:
    print("You can drive!")  # Output: You can drive!

# Using 'or'
is_weekend = True
is_holiday = False
if is_weekend or is_holiday:
    print("No work today!")  # Output: No work today!

# Using 'not'
is_raining = False
if not is_raining:
    print("Perfect weather for a walk!")  # Output: Perfect weather for a walk!

# NESTED CONDITIONALS
# You can put if statements inside other if statements

print("\n" + "="*50)  # Output: ==================================================
weather = "sunny"
temperature = 75

if weather == "sunny":
    if temperature > 70:
        print("Great beach weather!")  # Output: Great beach weather!
    else:
        print("Nice day, but might be a bit cool for the beach")
else:
    print("Not a sunny day")

# COMPARING STRINGS
# You can compare strings (alphabetically)

print("\n" + "="*50)  # Output: ==================================================
name1 = "Alice"
name2 = "Bob"

if name1 < name2:  # Alphabetically earlier
    print(f"{name1} comes before {name2}")  # Output: Alice comes before Bob

# CHECKING IF VALUES ARE IN A COLLECTION (preview)
# We'll learn more about this with lists, but here's a quick example

print("\n" + "="*50)  # Output: ==================================================
day = "Saturday"

if day in ["Saturday", "Sunday"]:
    print("It's the weekend!")  # Output: It's the weekend!
else:
    print("It's a weekday")

