"""
37_package_creation.py

This file demonstrates creating Python packages.
Covers package structure, setup.py, pyproject.toml, and distribution.
"""

import os

# PACKAGE STRUCTURE
# How to organize a Python package

package_structure = """
mypackage/
├── mypackage/              # Package directory
│   ├── __init__.py        # Makes it a package
│   ├── module1.py         # Package modules
│   ├── module2.py
│   └── subpackage/        # Subpackage
│       ├── __init__.py
│       └── module3.py
├── tests/                 # Test directory
│   ├── __init__.py
│   └── test_module1.py
├── setup.py               # Setup script (legacy)
├── pyproject.toml         # Modern setup (preferred)
├── README.md
├── LICENSE
└── requirements.txt
"""

print("1. PACKAGE STRUCTURE")
print(package_structure)

# __INIT__.PY
# Makes a directory a Python package

init_py_content = '''
"""
mypackage - A sample package
"""

__version__ = "0.1.0"
__author__ = "Your Name"

# Import main modules for easier access
from .module1 import function1
from .module2 import Class2

# Define what gets imported with "from package import *"
__all__ = ["function1", "Class2"]
'''

print("2. __INIT__.PY EXAMPLE")
print(init_py_content)

# SETUP.PY (Legacy, but still used)
# Traditional way to define package metadata

setup_py_content = '''
from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A sample Python package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/username/mypackage",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.28.0",
        "numpy>=1.20.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=22.0.0",
        ],
    },
)
'''

print("3. SETUP.PY EXAMPLE")
print(setup_py_content)

# PYPROJECT.TOML (Modern standard)
# Preferred way in Python 3.7+

pyproject_toml_content = '''
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "mypackage"
version = "0.1.0"
description = "A sample Python package"
readme = "README.md"
requires-python = ">=3.7"
license = {text = "MIT"}
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
dependencies = [
    "requests>=2.28.0",
    "numpy>=1.20.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "black>=22.0.0",
]

[project.urls]
Homepage = "https://github.com/username/mypackage"
Documentation = "https://github.com/username/mypackage#readme"
'''

print("4. PYPROJECT.TOML EXAMPLE (Modern)")
print(pyproject_toml_content)

# EXAMPLE PACKAGE MODULE
# How to structure package modules

module_example = '''
"""
mypackage/module1.py
Example module in a package
"""

def function1():
    """Public function."""
    return "Function 1"

def _private_function():
    """Private function (underscore prefix)."""
    return "Private"

class MyClass:
    """Example class."""
    
    def __init__(self, value):
        self.value = value
    
    def get_value(self):
        return self.value
'''

print("5. PACKAGE MODULE EXAMPLE")
print(module_example)

# BUILDING PACKAGES
# Create distribution files

print("6. BUILDING PACKAGES")
print("   Install build tools:")
print("   $ pip install build")
print()
print("   Build package:")
print("   $ python -m build")
print()
print("   This creates:")
print("   - dist/mypackage-0.1.0.tar.gz  (source distribution)")
print("   - dist/mypackage-0.1.0-py3-none-any.whl  (wheel)")
print()

# INSTALLING PACKAGES
print("7. INSTALLING PACKAGES")
print("   Install from local directory:")
print("   $ pip install .")
print()
print("   Install in development mode (editable):")
print("   $ pip install -e .")
print()
print("   Install from built wheel:")
print("   $ pip install dist/mypackage-0.1.0-py3-none-any.whl")
print()

# UPLOADING TO PYPI
print("8. UPLOADING TO PYPI")
print("   Install twine:")
print("   $ pip install twine")
print()
print("   Upload to TestPyPI (testing):")
print("   $ twine upload --repository testpypi dist/*")
print()
print("   Upload to PyPI (production):")
print("   $ twine upload dist/*")
print()

# PACKAGE METADATA
print("9. IMPORTANT METADATA FIELDS")
print("   - name: Package name (must be unique on PyPI)")
print("   - version: Semantic versioning (e.g., 1.2.3)")
print("   - description: Short description")
print("   - author: Author name")
print("   - url: Project homepage")
print("   - classifiers: Package metadata tags")
print("   - requires-python: Minimum Python version")
print()

# ENTRY POINTS
# Create command-line scripts

entry_points_example = '''
[project.scripts]
mycommand = "mypackage.cli:main"

# In setup.py:
entry_points={
    "console_scripts": [
        "mycommand=mypackage.cli:main",
    ],
}
'''

print("10. ENTRY POINTS (CLI Commands)")
print("    Define command-line scripts:")
print(entry_points_example)

# NAMESPACE PACKAGES
print()
print("11. NAMESPACE PACKAGES")
print("    Packages sharing a namespace:")
print("    - company.product1")
print("    - company.product2")
print("    Both under 'company' namespace")
print()

# TESTING PACKAGE STRUCTURE
print("12. TESTING YOUR PACKAGE")
print("    Run tests:")
print("    $ pytest")
print()
print("    Check package structure:")
print("    $ python -m pip install .")
print("    $ python -c 'import mypackage'")
print()

# README AND LICENSE
print("13. DOCUMENTATION FILES")
print("    README.md: Package description and usage")
print("    LICENSE: Legal license (MIT, Apache, etc.)")
print("    CHANGELOG.md: Version history")
print("    CONTRIBUTING.md: How to contribute")
print()

# VERSION MANAGEMENT
print("14. VERSION MANAGEMENT")
print("    Store version in __init__.py:")
print("    __version__ = '0.1.0'")
print()
print("    Or use importlib.metadata:")
print("    from importlib.metadata import version")
print("    version('mypackage')")
print()

# PACKAGE DISCOVERY
print("15. PACKAGE DISCOVERY")
print("    find_packages() automatically finds packages:")
print("    from setuptools import find_packages")
print("    packages=find_packages()")
print()
print("    Manually specify:")
print("    packages=['mypackage', 'mypackage.subpackage']")
print()

# DATA FILES AND RESOURCES
data_files_example = '''
# Include non-Python files
package_data={
    "mypackage": ["data/*.json", "templates/*.html"],
}

# Or in pyproject.toml:
[tool.setuptools.package-data]
mypackage = ["data/*.json", "templates/*.html"]
'''

print("16. INCLUDING DATA FILES")
print(data_files_example)

print("\nPackage creation demonstration complete!")
print("\nQuick start:")
print("  1. Create package structure")
print("  2. Add __init__.py files")
print("  3. Create pyproject.toml or setup.py")
print("  4. pip install -e .  (development install)")
print("  5. python -m build  (create distribution)")
print("  6. twine upload dist/*  (publish to PyPI)")

