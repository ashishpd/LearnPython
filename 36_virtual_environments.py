"""
36_virtual_environments.py

This file demonstrates virtual environments in Python.
Virtual environments isolate project dependencies and prevent conflicts.
Essential for managing Python packages across different projects.
"""

import subprocess
import sys
import os

# WHAT ARE VIRTUAL ENVIRONMENTS?
# Isolated Python environments with their own packages

print("Virtual Environments in Python")
print("=" * 50)
print("\n1. VIRTUAL ENVIRONMENTS OVERVIEW")
print("   - Isolate project dependencies")
print("   - Prevent package conflicts")
print("   - Allow different Python versions")
print("   - Essential for production deployments\n")

# CREATING VIRTUAL ENVIRONMENTS
# Multiple ways to create venvs

print("2. CREATING VIRTUAL ENVIRONMENTS")
print("   Using venv (Python 3.3+):")
print("   $ python -m venv myenv")
print("   $ python3 -m venv myenv")
print()
print("   Using virtualenv (older method):")
print("   $ pip install virtualenv")
print("   $ virtualenv myenv")
print()

# ACTIVATING VIRTUAL ENVIRONMENTS
# Different commands for different OS

print("3. ACTIVATING VIRTUAL ENVIRONMENTS")
print("   On Linux/Mac:")
print("   $ source myenv/bin/activate")
print()
print("   On Windows:")
print("   $ myenv\\Scripts\\activate")
print()
print("   After activation, prompt shows:")
print("   (myenv) $ python --version")
print()

# DEACTIVATING VIRTUAL ENVIRONMENTS
print("4. DEACTIVATING")
print("   $ deactivate")
print()

# CHECKING VIRTUAL ENVIRONMENT
# Verify if you're in a virtual environment

def check_venv():
    """Check if running in virtual environment."""
    in_venv = hasattr(sys, 'real_prefix') or (
        hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix
    )
    
    if in_venv:
        print(f"✓ Running in virtual environment")
        print(f"  Virtual env path: {sys.prefix}")
        print(f"  Base Python path: {sys.base_prefix}")
    else:
        print("✗ Not in virtual environment")
        print(f"  Python path: {sys.prefix}")
    print()

check_venv()

# VIRTUAL ENVIRONMENT STRUCTURE
# What's inside a venv

print("5. VIRTUAL ENVIRONMENT STRUCTURE")
print("   myenv/")
print("   ├── bin/          # Scripts (Linux/Mac)")
print("   │   ├── activate")
print("   │   ├── python")
print("   │   └── pip")
print("   ├── lib/          # Installed packages")
print("   │   └── python3.x/")
print("   ├── include/      # Header files")
print("   └── pyvenv.cfg    # Configuration")
print()

# WORKING WITH REQUIREMENTS.TXT
# Managing dependencies

requirements_content = """
# requirements.txt example
requests==2.28.1
flask>=2.0.0
numpy<1.24.0
pytest~=7.0.0
"""

print("6. REQUIREMENTS.TXT")
print("   Create requirements.txt:")
print("   $ pip freeze > requirements.txt")
print()
print("   Install from requirements.txt:")
print("   $ pip install -r requirements.txt")
print()
print("   Example requirements.txt:")
print(requirements_content)

# PIP FREEZE
# Generate requirements file

print("7. GENERATING REQUIREMENTS")
print("   Export current packages:")
print("   $ pip freeze > requirements.txt")
print()
print("   List installed packages:")
print("   $ pip list")
print()
print("   Show package details:")
print("   $ pip show package_name")
print()

# PYPROJECT.TOML (Modern approach)
# Alternative to setup.py + requirements.txt

pyproject_toml_example = """
[project]
name = "myproject"
version = "0.1.0"
dependencies = [
    "requests>=2.28.0",
    "flask>=2.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "black>=22.0.0",
]
"""

print("8. PYPROJECT.TOML (Modern Standard)")
print("   Modern Python packaging uses pyproject.toml:")
print(pyproject_toml_example)

# WORKING WITH MULTIPLE PYTHON VERSIONS
print()
print("9. MULTIPLE PYTHON VERSIONS")
print("   Create venv with specific Python version:")
print("   $ python3.9 -m venv venv39")
print("   $ python3.11 -m venv venv311")
print()

# VIRTUALENVWRAPPER (Optional tool)
print("10. VIRTUALENVWRAPPER (Optional)")
print("    Convenient tool for managing venvs:")
print("    $ pip install virtualenvwrapper")
print("    $ mkvirtualenv myenv")
print("    $ workon myenv")
print("    $ deactivate")
print()

# POETRY (Modern dependency management)
print("11. POETRY (Modern Tool)")
print("    Alternative package manager:")
print("    $ pip install poetry")
print("    $ poetry new myproject")
print("    $ poetry install")
print("    $ poetry add requests")
print("    $ poetry shell  # Activate venv")
print()

# PIPENV (Another alternative)
print("12. PIPENV (Alternative Tool)")
print("    Combines pip and virtualenv:")
print("    $ pip install pipenv")
print("    $ pipenv install")
print("    $ pipenv shell")
print("    $ pipenv install requests")
print()

# BEST PRACTICES
print("13. BEST PRACTICES")
print("    ✓ Always use venvs for projects")
print("    ✓ Never install packages globally")
print("    ✓ Commit requirements.txt to git")
print("    ✓ Use different venvs per project")
print("    ✓ Keep venv out of git (.gitignore)")
print()

# GITIGNORE EXAMPLE
gitignore_content = """
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python

# Virtual environments
venv/
env/
ENV/
.venv
"""
print("14. .GITIGNORE EXAMPLE")
print("    Always exclude venv from git:")
print(gitignore_content)

# CHECKING PACKAGES
print()
print("15. MANAGING PACKAGES IN VENV")
print("    List installed packages:")
print("    $ pip list")
print()
print("    Search for packages:")
print("    $ pip search package_name")
print()
print("    Install package:")
print("    $ pip install package_name")
print()
print("    Install specific version:")
print("    $ pip install package_name==2.1.0")
print()
print("    Upgrade package:")
print("    $ pip install --upgrade package_name")
print()
print("    Uninstall package:")
print("    $ pip uninstall package_name")
print()

# VENV VS CONDA
print("16. VENV VS CONDA")
print("    venv: Built-in, lightweight, Python-only")
print("    conda: Full package manager, cross-language, heavier")
print("    Choose venv for Python-only projects")
print()

print("Virtual environments demonstration complete!")
print("\nTo create and use a venv:")
print("  python -m venv myenv")
print("  source myenv/bin/activate  # Linux/Mac")
print("  myenv\\Scripts\\activate      # Windows")
print("  pip install package_name")
print("  deactivate")

