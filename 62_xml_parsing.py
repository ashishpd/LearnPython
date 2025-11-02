"""
62_xml_parsing.py

This file demonstrates XML parsing in Python.
Covers xml.etree.ElementTree.
"""

import xml.etree.ElementTree as ET

print("XML PARSING")
print("=" * 50)

# PARSE XML
print("1. Parse XML:")

xml_string = """<?xml version="1.0"?>
<root>
    <person name="Alice" age="30"/>
    <person name="Bob" age="25"/>
</root>"""

root = ET.fromstring(xml_string)
print(f"   Root tag: {root.tag}")

for person in root.findall('person'):
    print(f"   {person.get('name')}: {person.get('age')}")

print()

print("XML parsing demonstration complete!")

