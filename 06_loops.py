"""
06_loops.py

This file demonstrates loops in Python - for loops and while loops.
Loops allow you to execute code repeatedly, which is essential for
processing multiple items or repeating actions.
"""

# FOR LOOP
# The for loop iterates over a sequence (like a range, list, string, etc.)

# Loop through a range of numbers
print("Counting from 1 to 5:")
for i in range(1, 6):  # range(start, stop) - stop is exclusive
    print(i)

# range() function
# range(stop) - starts at 0, goes up to (but not including) stop
print("\nCounting from 0 to 4:")
for i in range(5):
    print(i)

# range(start, stop) - starts at start, goes up to (but not including) stop
print("\nCounting from 2 to 6:")
for i in range(2, 7):
    print(i)

# range(start, stop, step) - can specify step size
print("\nCounting by 2s from 0 to 8:")
for i in range(0, 10, 2):
    print(i)

# Loop through a string
print("\nLooping through characters in 'Hello':")
for char in "Hello":
    print(char)

# Loop through a list (we'll learn more about lists next)
print("\nLooping through a list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

# WHILE LOOP
# The while loop repeats as long as a condition is True

print("\n" + "="*50)
print("While loop example - counting down:")
count = 5
while count > 0:
    print(count)
    count = count - 1  # Important: update the counter!
print("Blast off!")

# BE CAREFUL: Infinite loops!
# If the condition never becomes False, the loop runs forever
# Example (commented out so it doesn't run):
# while True:
#     print("This would run forever!")

# Loop with user input
print("\n" + "="*50)
# Uncomment to try:
# password = ""
# while password != "secret":
#     password = input("Enter password: ")
# print("Access granted!")

# LOOP CONTROL: break and continue

# break - exits the loop immediately
print("\n" + "="*50)
print("Using break to exit early:")
for i in range(1, 10):
    if i == 5:
        break  # Exit the loop when i equals 5
    print(i)
print("Loop ended")

# continue - skips the rest of the current iteration and continues
print("\n" + "="*50)
print("Using continue to skip even numbers:")
for i in range(1, 11):
    if i % 2 == 0:  # If i is even
        continue  # Skip the rest and go to next iteration
    print(i)  # Only prints odd numbers

# NESTED LOOPS
# Loops inside other loops

print("\n" + "="*50)
print("Multiplication table (nested loops):")
for i in range(1, 4):
    for j in range(1, 4):
        result = i * j
        print(f"{i} x {j} = {result}")

# LOOP WITH ELSE
# The else block executes when the loop completes normally
# (not when exited by break)

print("\n" + "="*50)
print("For-else example:")
for i in range(3):
    print(f"Loop iteration {i}")
else:
    print("Loop completed normally!")

# Compare with break:
print("\nFor-else with break:")
for i in range(3):
    if i == 1:
        break
    print(f"Loop iteration {i}")
else:
    print("This won't print because loop was broken")

# PRACTICAL EXAMPLES

# Sum numbers from 1 to 10
print("\n" + "="*50)
total = 0
for num in range(1, 11):
    total = total + num
print(f"Sum of 1 to 10: {total}")

# Find even numbers
print("\nFinding even numbers from 1 to 20:")
even_numbers = []
for num in range(1, 21):
    if num % 2 == 0:
        even_numbers.append(num)
print(f"Even numbers: {even_numbers}")

