"""
57_os_and_sys_modules.py

This file demonstrates os and sys modules.
System interaction and environment management.
"""

import os
import sys

print("OS AND SYS MODULES")
print("=" * 50)

# OS MODULE
print("1. os Module:")

print(f"   Current directory: {os.getcwd()}")
print(f"   Home directory: {os.path.expanduser('~')}")
print(f"   Path separator: {os.sep}")
print(f"   Environment PATH: {os.environ.get('PATH', 'N/A')[:50]}...\n")

# SYS MODULE
print("2. sys Module:")

print(f"   Python version: {sys.version.split()[0]}")
print(f"   Platform: {sys.platform}")
print(f"   Executable: {sys.executable}")
print(f"   Module search path: {len(sys.path)} directories\n")

print("OS and sys demonstration complete!")

