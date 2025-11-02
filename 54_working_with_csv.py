"""
54_working_with_csv.py

This file demonstrates working with CSV files in Python.
Covers csv module and pandas basics.
"""

import csv
from pathlib import Path

print("WORKING WITH CSV IN PYTHON")
print("=" * 50)

# READING CSV
# Read CSV files

print("1. Reading CSV:")

# Sample CSV data
csv_data = """name,age,city
Alice,30,New York
Bob,25,San Francisco
Charlie,35,Chicago"""

# Write sample CSV
sample_file = Path("sample.csv")
sample_file.write_text(csv_data)

# Read CSV
with open(sample_file, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(f"   {row}")

print()

# DICTREADER
# Read CSV as dictionaries

print("2. DictReader:")

with open(sample_file, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"   {row['name']}: {row['age']} years old, from {row['city']}")

print()

# WRITING CSV
# Write data to CSV

print("3. Writing CSV:")

output_file = Path("output.csv")
data = [
    ["Name", "Score", "Grade"],
    ["Alice", 95, "A"],
    ["Bob", 87, "B"],
    ["Charlie", 92, "A"]
]

with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)

print(f"   Written to {output_file}\n")

# DICTWRITER
# Write dictionaries to CSV

print("4. DictWriter:")

fieldnames = ["name", "age", "city"]
people = [
    {"name": "Diana", "age": "28", "city": "Boston"},
    {"name": "Eve", "age": "32", "city": "Seattle"}
]

with open(output_file, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(people)

print(f"   Written with DictWriter\n")

# CSV OPTIONS
# Customize CSV format

print("5. CSV Options:")

# Custom delimiter
with open("delim.csv", 'w', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(["Item", "Price", "Quantity"])
    writer.writerow(["Apple", "1.50", "10"])

print("   Created semicolon-delimited CSV\n")

# PANDAS (Third-party)
# Powerful data manipulation

pandas_info = """
6. Pandas for CSV (Third-party):
    Install: pip install pandas
    
    import pandas as pd
    
    # Read CSV
    df = pd.read_csv('file.csv')
    
    # Write CSV
    df.to_csv('output.csv', index=False)
    
    # Data operations
    df.head()        # First 5 rows
    df.describe()    # Statistics
    df.groupby()     # Group operations
    df.filter()      # Filter rows
"""

print(pandas_info)

# CLEANUP
for file in [sample_file, output_file, Path("delim.csv")]:
    if file.exists():
        file.unlink()

print("CSV demonstration complete!")

