"""
61_web_scraping.py

This file demonstrates web scraping in Python.
Covers BeautifulSoup and basic scraping concepts.
Note: Requires 'pip install beautifulsoup4 requests'
"""

print("WEB SCRAPING")
print("=" * 50)

print("1. BeautifulSoup:")
print("   Install: pip install beautifulsoup4 requests")
print()
print("   from bs4 import BeautifulSoup")
print("   import requests")
print()
print("   response = requests.get('https://example.com')")
print("   soup = BeautifulSoup(response.text, 'html.parser')")
print("   print(soup.find('title'))")
print()

print("2. Common Operations:")
print("   - soup.find() - Find first element")
print("   - soup.find_all() - Find all elements")
print("   - soup.select() - CSS selectors")
print("   - Element.text - Get text content")
print()

print("Web scraping demonstration complete!")

