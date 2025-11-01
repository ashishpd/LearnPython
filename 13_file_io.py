"""
13_file_io.py

This file demonstrates file input/output (I/O) operations in Python.
You'll learn how to read from and write to files.
"""

# WRITING TO A FILE
# Open file in write mode ('w' - overwrites existing file)

# Method 1: Using open() and close()
file = open("example.txt", "w")
file.write("Hello, World!\n")
file.write("This is a second line.\n")
file.close()  # Important: always close files!

# Method 2: Using with statement (RECOMMENDED - automatically closes file)
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a second line.\n")
# File is automatically closed here

# APPENDING TO A FILE
# Open file in append mode ('a' - adds to end of file)

with open("example.txt", "a") as file:
    file.write("This line is appended.\n")

# READING FROM A FILE

# read() - reads entire file as a single string
with open("example.txt", "r") as file:
    content = file.read()
    print("Full content:")
    print(content)

# readline() - reads one line at a time
with open("example.txt", "r") as file:
    print("\nReading line by line:")
    line1 = file.readline()
    print(f"Line 1: {line1.strip()}")  # strip() removes newline
    line2 = file.readline()
    print(f"Line 2: {line2.strip()}")

# readlines() - reads all lines into a list
with open("example.txt", "r") as file:
    lines = file.readlines()
    print("\nAll lines as list:")
    for line in lines:
        print(f"  {line.strip()}")

# Iterating over file (memory efficient)
with open("example.txt", "r") as file:
    print("\nIterating over file:")
    for line in file:
        print(f"  {line.strip()}")

# FILE MODES
# 'r' - read mode (default)
# 'w' - write mode (overwrites existing file)
# 'a' - append mode (adds to end of file)
# 'x' - exclusive creation (fails if file exists)
# 'b' - binary mode (for images, etc.)
# 't' - text mode (default)
# '+' - read and write

# Examples:
# 'rb' - read binary
# 'wb' - write binary
# 'r+' - read and write (file must exist)
# 'w+' - read and write (creates/overwrites file)

# WRITING MULTIPLE LINES
# writelines() - writes a list of strings

lines_to_write = [
    "Line 1\n",
    "Line 2\n",
    "Line 3\n"
]

with open("multiple_lines.txt", "w") as file:
    file.writelines(lines_to_write)

# READING BINARY FILES
# Use 'b' mode for binary files (images, videos, etc.)

# Example: Copying a binary file
# Uncomment to try:
# with open("source.jpg", "rb") as source:
#     with open("copy.jpg", "wb") as destination:
#         destination.write(source.read())

# CHECKING IF FILE EXISTS
import os

file_path = "example.txt"
if os.path.exists(file_path):
    print(f"\nFile '{file_path}' exists!")
    print(f"File size: {os.path.getsize(file_path)} bytes")
else:
    print(f"\nFile '{file_path}' does not exist.")

# HANDLING FILE ERRORS
# It's good practice to handle potential errors

try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("\nFile not found!")
except PermissionError:
    print("Permission denied!")
except Exception as e:
    print(f"An error occurred: {e}")

# WORKING WITH PATHS
import os

# Get current directory
current_dir = os.getcwd()
print(f"\nCurrent directory: {current_dir}")

# Join paths (works on all operating systems)
file_path = os.path.join("data", "files", "example.txt")
print(f"File path: {file_path}")

# Split path
directory, filename = os.path.split(file_path)
print(f"Directory: {directory}")
print(f"Filename: {filename}")

# PRACTICAL EXAMPLE: Processing a file

# Write sample data
with open("grades.txt", "w") as file:
    file.write("Alice,85\n")
    file.write("Bob,92\n")
    file.write("Charlie,78\n")
    file.write("Diana,95\n")

# Read and process
print("\nProcessing grades:")
with open("grades.txt", "r") as file:
    for line in file:
        name, grade = line.strip().split(",")
        grade = int(grade)
        status = "Pass" if grade >= 80 else "Fail"
        print(f"{name}: {grade} - {status}")

# CONTEXT MANAGERS (with statement)
# The 'with' statement is the recommended way to handle files
# It automatically:
# 1. Opens the file
# 2. Ensures the file is closed even if an error occurs
# 3. Handles exceptions

# This is equivalent to:
# file = open("example.txt", "r")
# try:
#     content = file.read()
# finally:
#     file.close()

# MULTIPLE FILES
# You can open multiple files at once

with open("file1.txt", "w") as f1, open("file2.txt", "w") as f2:
    f1.write("Content for file 1\n")
    f2.write("Content for file 2\n")

# READING LARGE FILES EFFICIENTLY
# For very large files, read in chunks

# This reads the file in 1024-byte chunks
# Uncomment to try:
# with open("large_file.txt", "r") as file:
#     chunk_size = 1024
#     while True:
#         chunk = file.read(chunk_size)
#         if not chunk:
#             break
#         # Process chunk here
#         print(chunk)

