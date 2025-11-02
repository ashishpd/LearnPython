"""
53_pathlib_advanced.py

This file demonstrates pathlib module (Python 3.4+).
Modern, object-oriented path handling.
"""

from pathlib import Path
import os

print("PATHLIB IN PYTHON")
print("=" * 50)

# BASIC PATH OPERATIONS
# Create and manipulate paths

print("1. Basic Path Operations:")

# Create Path objects
current_dir = Path(".")
home_dir = Path.home()
root_path = Path("/")

print(f"   Current dir: {current_dir.absolute()}")
print(f"   Home dir: {home_dir}")
print(f"   Path exists: {current_dir.exists()}\n")

# PATH COMPONENTS
# Access path parts

print("2. Path Components:")

file_path = Path("/home/user/documents/file.txt")
print(f"   Path: {file_path}")
print(f"   Parent: {file_path.parent}")
print(f"   Name: {file_path.name}")
print(f"   Stem: {file_path.stem}")
print(f"   Suffix: {file_path.suffix}")
print(f"   Parts: {file_path.parts}\n")

# PATH OPERATIONS
# Join paths, check properties

print("3. Path Operations:")

base = Path("/home/user")
file1 = base / "documents" / "file.txt"
file2 = base.joinpath("downloads", "file.pdf")

print(f"   Joined: {file1}")
print(f"   Is file: {file1.is_file()}")
print(f"   Is dir: {file1.parent.is_dir()}\n")

# FILE OPERATIONS
# Read, write, check files

print("4. File Operations:")

# Create test file
test_file = Path("test_file.txt")
test_file.write_text("Hello, Pathlib!")
content = test_file.read_text()
print(f"   Read content: {content}")

# Check file properties
print(f"   Size: {test_file.stat().st_size} bytes")
print(f"   Exists: {test_file.exists()}\n")

# DIRECTORY OPERATIONS
# List, create directories

print("5. Directory Operations:")

# Create directory
test_dir = Path("test_dir")
test_dir.mkdir(exist_ok=True)
print(f"   Created: {test_dir.exists()}")

# List directory
if test_dir.exists():
    files = list(test_dir.iterdir())
    print(f"   Files in dir: {len(files)}")

# Cleanup
test_dir.rmdir()
print()

# GLOB PATTERNS
# Find files matching patterns

print("6. Glob Patterns:")

# Find Python files in current directory
py_files = list(Path(".").glob("*.py"))
print(f"   Python files found: {len(py_files)}")

# Recursive glob
# all_py = list(Path(".").glob("**/*.py"))
# print(f"   Recursive Python files: {len(all_py)}\n")

# PATH UTILITIES
# Common path operations

print("7. Path Utilities:")

path = Path("example.txt")
print(f"   Absolute: {path.absolute()}")
print(f"   Resolved: {path.resolve() if path.exists() else 'N/A'}")
print(f"   With suffix: {path.with_suffix('.bak')}")
print(f"   With name: {path.with_name('new_file.txt')}\n")

# COMPARISON WITH OS.PATH
print("8. pathlib vs os.path:")
print("   pathlib - Object-oriented, modern")
print("   os.path - Function-based, older")
print("   Prefer pathlib for new code\n")

# Cleanup
if test_file.exists():
    test_file.unlink()

print("Pathlib demonstration complete!")

