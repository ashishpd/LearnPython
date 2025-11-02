"""
63_security_basics.py

This file demonstrates security basics in Python.
Covers hashlib, secrets module, and security best practices.
"""

import hashlib
import secrets

print("SECURITY BASICS")
print("=" * 50)

# HASHING
print("1. Hashing:")

data = "password123"
md5_hash = hashlib.md5(data.encode()).hexdigest()
sha256_hash = hashlib.sha256(data.encode()).hexdigest()

print(f"   MD5: {md5_hash[:20]}...")
print(f"   SHA256: {sha256_hash[:20]}...\n")

# SECRETS MODULE
print("2. Secrets Module:")

token = secrets.token_hex(16)
print(f"   Secure token: {token[:20]}...\n")

# SECURITY BEST PRACTICES
print("3. Security Best Practices:")
print("   ✓ Use secrets module for random")
print("   ✓ Hash passwords (never store plaintext)")
print("   ✓ Validate and sanitize input")
print("   ✓ Use parameterized queries")
print("   ✓ Keep dependencies updated")
print()

print("Security basics demonstration complete!")

