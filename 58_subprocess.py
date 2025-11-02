"""
58_subprocess.py

This file demonstrates subprocess module.
Running external commands and processes.
"""

import subprocess

print("SUBPROCESS MODULE")
print("=" * 50)

print("1. subprocess.run():")

result = subprocess.run(["echo", "Hello"], capture_output=True, text=True)
print(f"   Output: {result.stdout}")

print("\n2. Running Commands:")
print("   subprocess.run() - Run command")
print("   subprocess.Popen() - Advanced control")
print("   subprocess.check_output() - Get output")

print("\nSubprocess demonstration complete!")

