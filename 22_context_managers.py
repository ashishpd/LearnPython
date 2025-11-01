"""
22_context_managers.py

This file demonstrates context managers in Python.
Context managers ensure proper setup and cleanup using the 'with' statement.
The most common example is file handling.
"""

# BASIC CONTEXT MANAGER - FILE HANDLING
# The 'with' statement automatically closes files

with open("example.txt", "w") as file:
    file.write("Hello, World!")
# File is automatically closed here

# This is better than:
# file = open("example.txt", "w")
# file.write("Hello, World!")
# file.close()  # Might forget!

# CUSTOM CONTEXT MANAGER (CLASS-BASED)

class FileManager:
    """Custom context manager for file operations."""
    
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        """Called when entering 'with' block."""
        print(f"Opening {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting 'with' block."""
        print(f"Closing {self.filename}")
        if self.file:
            self.file.close()
        return False  # Don't suppress exceptions

# Usage
with FileManager("test.txt", "w") as f:
    f.write("Test content")

# CONTEXT MANAGER WITH CONTEXTLIB
# Simpler way using @contextmanager decorator

from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    """Context manager using contextlib."""
    file = open(filename, mode)
    try:
        yield file
    finally:
        file.close()

with file_manager("test2.txt", "w") as f:
    f.write("Test content 2")

# TIMING CONTEXT MANAGER

import time
from contextlib import contextmanager

@contextmanager
def timer():
    """Context manager that times code execution."""
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f"Execution took {end - start:.4f} seconds")

with timer():
    time.sleep(0.1)
    print("Doing some work...")

# CHANGING DIRECTORY (using contextlib.chdir)

from contextlib import contextmanager
import os

@contextmanager
def change_directory(path):
    """Temporarily change working directory."""
    old_path = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(old_path)

# Usage:
# with change_directory("/tmp"):
#     # Do something in /tmp
# # Back to original directory

# SUPPRESSING EXCEPTIONS

from contextlib import suppress

with suppress(FileNotFoundError):
    with open("nonexistent.txt") as f:
        content = f.read()
print("Code continues after suppressing error")

# MULTIPLE CONTEXT MANAGERS

with open("file1.txt", "w") as f1, open("file2.txt", "w") as f2:
    f1.write("File 1 content")
    f2.write("File 2 content")

