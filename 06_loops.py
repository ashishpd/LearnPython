"""
06_loops.py

This file demonstrates loops in Python - for loops and while loops.
Loops allow you to execute code repeatedly, which is essential for
processing multiple items or repeating actions.
"""

# FOR LOOP
# The for loop iterates over a sequence (like a range, list, string, etc.)

# Loop through a range of numbers
print("Counting from 1 to 5:")  # Output: Counting from 1 to 5:
for i in range(1, 6):  # range(start, stop) - stop is exclusive
    print(i)  # Output: 1, 2, 3, 4, 5 (one per line)

# range() function
# range(stop) - starts at 0, goes up to (but not including) stop
print("\nCounting from 0 to 4:")  # Output: Counting from 0 to 4:
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4 (one per line)

# range(start, stop) - starts at start, goes up to (but not including) stop
print("\nCounting from 2 to 6:")  # Output: Counting from 2 to 6:
for i in range(2, 7):
    print(i)  # Output: 2, 3, 4, 5, 6 (one per line)

# range(start, stop, step) - can specify step size
print("\nCounting by 2s from 0 to 8:")  # Output: Counting by 2s from 0 to 8:
for i in range(0, 10, 2):
    print(i)  # Output: 0, 2, 4, 6, 8 (one per line)

# Loop through a string
print("\nLooping through characters in 'Hello':")  # Output: Looping through characters in 'Hello':
for char in "Hello":
    print(char)  # Output: H, e, l, l, o (one per line)

# Loop through a list (we'll learn more about lists next)
print("\nLooping through a list:")  # Output: Looping through a list:
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")  # Output: I like apple, I like banana, I like cherry (one per line)

# WHILE LOOP
# The while loop repeats as long as a condition is True

print("\n" + "="*50)  # Output: ==================================================
print("While loop example - counting down:")  # Output: While loop example - counting down:
count = 5
while count > 0:
    print(count)  # Output: 5, 4, 3, 2, 1 (one per line)
    count = count - 1  # Important: update the counter!
print("Blast off!")  # Output: Blast off!

# BE CAREFUL: Infinite loops!
# If the condition never becomes False, the loop runs forever
# Example (commented out so it doesn't run):
# while True:
#     print("This would run forever!")

# Loop with user input
print("\n" + "="*50)  # Output: ==================================================
# Uncomment to try:
# password = ""
# while password != "secret":
#     password = input("Enter password: ")
# print("Access granted!")

# LOOP CONTROL: break and continue

# break - exits the loop immediately
print("\n" + "="*50)  # Output: ==================================================
print("Using break to exit early:")  # Output: Using break to exit early:
for i in range(1, 10):
    if i == 5:
        break  # Exit the loop when i equals 5
    print(i)  # Output: 1, 2, 3, 4 (one per line)
print("Loop ended")  # Output: Loop ended

# continue - skips the rest of the current iteration and continues
print("\n" + "="*50)  # Output: ==================================================
print("Using continue to skip even numbers:")  # Output: Using continue to skip even numbers:
for i in range(1, 11):
    if i % 2 == 0:  # If i is even
        continue  # Skip the rest and go to next iteration
    print(i)  # Output: 1, 3, 5, 7, 9 (one per line)  # Only prints odd numbers

# NESTED LOOPS
# Loops inside other loops

print("\n" + "="*50)  # Output: ==================================================
print("Multiplication table (nested loops):")  # Output: Multiplication table (nested loops):
for i in range(1, 4):
    for j in range(1, 4):
        result = i * j
        print(f"{i} x {j} = {result}")  # Output: 1 x 1 = 1, 1 x 2 = 2, 1 x 3 = 3, 2 x 1 = 2, etc. (one per line)

# LOOP WITH ELSE
# The else block executes when the loop completes normally
# (not when exited by break)

print("\n" + "="*50)  # Output: ==================================================
print("For-else example:")  # Output: For-else example:
for i in range(3):
    print(f"Loop iteration {i}")  # Output: Loop iteration 0, Loop iteration 1, Loop iteration 2 (one per line)
else:
    print("Loop completed normally!")  # Output: Loop completed normally!

# Compare with break:
print("\nFor-else with break:")  # Output: For-else with break:
for i in range(3):
    if i == 1:
        break
    print(f"Loop iteration {i}")  # Output: Loop iteration 0
else:
    print("This won't print because loop was broken")  # This won't print

# PRACTICAL EXAMPLES

# Sum numbers from 1 to 10
print("\n" + "="*50)  # Output: ==================================================
total = 0
for num in range(1, 11):
    total = total + num
print(f"Sum of 1 to 10: {total}")  # Output: Sum of 1 to 10: 55

# Find even numbers
print("\nFinding even numbers from 1 to 20:")  # Output: Finding even numbers from 1 to 20:
even_numbers = []
for num in range(1, 21):
    if num % 2 == 0:
        even_numbers.append(num)
print(f"Even numbers: {even_numbers}")  # Output: Even numbers: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

