"""
17_modules_and_imports.py

This file demonstrates modules and imports in Python.
Modules are files containing Python code that can be imported and reused.
They help organize code and promote reusability.
"""

# IMPORTING ENTIRE MODULES
# Import a module and use it with dot notation

import math
print(f"Pi: {math.pi}")
print(f"Square root of 16: {math.sqrt(16)}")

# IMPORTING SPECIFIC FUNCTIONS/CLASSES
# Import only what you need

from datetime import datetime, timedelta
now = datetime.now()
print(f"\nCurrent time: {now}")
tomorrow = now + timedelta(days=1)
print(f"Tomorrow: {tomorrow}")

# IMPORTING WITH ALIAS
# Give modules or functions a shorter name

import random as rnd
number = rnd.randint(1, 10)
print(f"\nRandom number: {number}")

from collections import Counter as Cnt
my_list = [1, 2, 2, 3, 3, 3]
count = Cnt(my_list)
print(f"Count: {count}")

# IMPORTING EVERYTHING (NOT RECOMMENDED)
# from math import *
# Can cause naming conflicts and makes code less clear

# COMMON STANDARD LIBRARY MODULES

# os - operating system interface
import os
print(f"\nCurrent directory: {os.getcwd()}")
print(f"Platform: {os.name}")

# sys - system-specific parameters
import sys
print(f"\nPython version: {sys.version}")
print(f"Platform: {sys.platform}")

# random - random number generation
import random
print(f"\nRandom integer (1-10): {random.randint(1, 10)}")
print(f"Random choice: {random.choice(['apple', 'banana', 'cherry'])}")
print(f"Random sample: {random.sample(range(1, 11), 3)}")

# collections - specialized container types
from collections import Counter, defaultdict, deque

# Counter - count occurrences
counter = Counter(['a', 'b', 'a', 'c', 'b', 'a'])
print(f"\nCounter: {counter}")
print(f"Most common: {counter.most_common(2)}")

# defaultdict - dict with default values
dd = defaultdict(int)
dd['a'] += 1  # No need to check if key exists
print(f"Defaultdict: {dd}")

# json - JSON encoder and decoder
import json
data = {"name": "Alice", "age": 30, "city": "New York"}
json_string = json.dumps(data)
print(f"\nJSON string: {json_string}")
parsed = json.loads(json_string)
print(f"Parsed back: {parsed}")

# datetime - date and time handling
from datetime import datetime, date, time

today = date.today()
print(f"\nToday: {today}")
print(f"Year: {today.year}, Month: {today.month}, Day: {today.day}")

now = datetime.now()
print(f"Current datetime: {now}")
print(f"Formatted: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Creating your own module
# Create a file called my_module.py with:
# def greet(name):
#     return f"Hello, {name}!"
#
# Then import it:
# import my_module
# print(my_module.greet("Alice"))

# CHECKING IF MODULE IS IMPORTED
if 'math' in sys.modules:
    print("\nMath module is imported")

# DIR() FUNCTION
# List all attributes of a module

print(f"\nMath module attributes (first 10): {dir(math)[:10]}")

# GETMODULEINFO
# Get information about a module

import math
print(f"\nMath module path: {math.__file__}")
print(f"Math module name: {math.__name__}")

# RELATIVE IMPORTS
# Import from package structure
# from .module import function  # Same package
# from ..parent import function  # Parent package

# PACKAGES
# Packages are directories containing __init__.py files
# They allow organizing multiple modules

# Example structure:
# mypackage/
#   __init__.py
#   module1.py
#   module2.py
#   subpackage/
#       __init__.py
#       module3.py

# Import from package:
# from mypackage import module1
# from mypackage.subpackage import module3

# VIRTUAL ENVIRONMENTS AND INSTALLING MODULES
# Use pip to install external modules:
# pip install package_name

# Example external modules:
# - requests (HTTP library)
# - numpy (numerical computing)
# - pandas (data analysis)
# - flask/django (web frameworks)

# BEST PRACTICES

# 1. Import at the top of the file
# 2. Group imports: standard library, third-party, local
# 3. Be specific: import only what you need
# 4. Use aliases for long names
# 5. Avoid import * (from module import *)

# Example of organized imports:
# # Standard library
# import os
# import sys
# from datetime import datetime
#
# # Third-party
# import requests
# import numpy as np
#
# # Local
# from my_module import my_function

