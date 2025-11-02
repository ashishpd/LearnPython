"""
44_database_connections.py

This file demonstrates database connections in Python.
Covers SQLite (built-in), connection pooling, and basic ORM concepts.
Note: SQLite is used for examples as it requires no setup.
"""

import sqlite3
import contextlib
from typing import Optional

print("DATABASE CONNECTIONS IN PYTHON")
print("=" * 50)

# BASIC SQLITE CONNECTION
# SQLite is built into Python

print("1. Basic SQLite Connection:")

# Connect to database (creates if doesn't exist)
conn = sqlite3.connect("example.db")

# Create cursor
cursor = conn.cursor()

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE,
        age INTEGER
    )
""")

# Insert data
cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", 
               ("Alice", "alice@example.com", 30))
cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", 
               ("Bob", "bob@example.com", 25))

# Commit changes
conn.commit()

# Query data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print("   Users:")
for row in rows:
    print(f"     {row}")

# Close connection
conn.close()
print()

# CONTEXT MANAGER FOR CONNECTIONS
# Ensure connections are closed

print("2. Connection with Context Manager:")

with sqlite3.connect("example.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT name, email FROM users")
    rows = cursor.fetchall()
    print("   Users (context manager):")
    for row in rows:
        print(f"     {row[0]}: {row[1]}")

print("   (Connection automatically closed)\n")

# PARAMETERIZED QUERIES
# Prevent SQL injection

print("3. Parameterized Queries:")

def get_user_by_email(email: str) -> Optional[tuple]:
    """Get user by email safely."""
    with sqlite3.connect("example.db") as conn:
        cursor = conn.cursor()
        # Use ? placeholder (SQLite) or %s (others)
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        return cursor.fetchone()

user = get_user_by_email("alice@example.com")
print(f"   User: {user}\n")

# TRANSACTIONS
# Group multiple operations

print("4. Transactions:")

with sqlite3.connect("example.db") as conn:
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
                      ("Charlie", "charlie@example.com", 35))
        cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
                      ("Diana", "diana@example.com", 28))
        
        # Commit transaction
        conn.commit()
        print("   Transaction committed")
    except sqlite3.Error as e:
        # Rollback on error
        conn.rollback()
        print(f"   Transaction rolled back: {e}")

# Verify
with sqlite3.connect("example.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]
    print(f"   Total users: {count}\n")

# CONNECTION POOLING
# Reuse connections efficiently

import threading
from queue import Queue

class ConnectionPool:
    """Simple connection pool."""
    
    def __init__(self, db_path, max_connections=5):
        self.db_path = db_path
        self.max_connections = max_connections
        self.pool = Queue(maxsize=max_connections)
        self.lock = threading.Lock()
        
        # Pre-populate pool
        for _ in range(max_connections):
            conn = sqlite3.connect(db_path, check_same_thread=False)
            self.pool.put(conn)
    
    def get_connection(self):
        """Get connection from pool."""
        return self.pool.get()
    
    def return_connection(self, conn):
        """Return connection to pool."""
        self.pool.put(conn)
    
    def close_all(self):
        """Close all connections."""
        while not self.pool.empty():
            conn = self.pool.get()
            conn.close()

# Usage (concept)
print("5. Connection Pooling:")
print("   Connection pools reuse connections")
print("   Reduces connection overhead")
print("   Important for high-traffic applications\n")

# ROW FACTORY
# Access rows as dictionaries

print("6. Row Factory (Dictionary Access):")

def dict_factory(cursor, row):
    """Convert row to dictionary."""
    return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}

with sqlite3.connect("example.db") as conn:
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users LIMIT 1")
    row = cursor.fetchone()
    print(f"   Row as dict: {row}")
    print(f"   Access by name: {row['name']}\n")

# ERROR HANDLING
# Handle database errors gracefully

print("7. Error Handling:")

try:
    with sqlite3.connect("example.db") as conn:
        cursor = conn.cursor()
        # Try to insert duplicate email
        cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
                      ("Duplicate", "alice@example.com", 30))
        conn.commit()
except sqlite3.IntegrityError as e:
    print(f"   Integrity error: {e}")
except sqlite3.Error as e:
    print(f"   Database error: {e}")

print()

# DATABASE CONTEXT MANAGER CLASS
# Reusable database handler

class Database:
    """Database handler with context manager."""
    
    def __init__(self, db_path):
        self.db_path = db_path
    
    def __enter__(self):
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = dict_factory
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.conn.rollback()
        else:
            self.conn.commit()
        self.conn.close()
        return False
    
    def execute(self, query, params=()):
        """Execute query."""
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        return cursor
    
    def fetch_one(self, query, params=()):
        """Fetch one row."""
        cursor = self.execute(query, params)
        return cursor.fetchone()
    
    def fetch_all(self, query, params=()):
        """Fetch all rows."""
        cursor = self.execute(query, params)
        return cursor.fetchall()

print("8. Database Handler Class:")

with Database("example.db") as db:
    users = db.fetch_all("SELECT name, email FROM users")
    print("   Users:")
    for user in users:
        print(f"     {user['name']}: {user['email']}")

print()

# ORM CONCEPT - SIMPLE EXAMPLE
# Object-Relational Mapping basics

class UserModel:
    """Simple ORM-style model."""
    
    def __init__(self, name, email, age, id=None):
        self.id = id
        self.name = name
        self.email = email
        self.age = age
    
    def save(self):
        """Save to database."""
        with sqlite3.connect("example.db") as conn:
            cursor = conn.cursor()
            if self.id:
                cursor.execute(
                    "UPDATE users SET name=?, email=?, age=? WHERE id=?",
                    (self.name, self.email, self.age, self.id)
                )
            else:
                cursor.execute(
                    "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
                    (self.name, self.email, self.age)
                )
                self.id = cursor.lastrowid
            conn.commit()
    
    @classmethod
    def find_by_id(cls, user_id):
        """Find user by ID."""
        with sqlite3.connect("example.db") as conn:
            conn.row_factory = dict_factory
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
            row = cursor.fetchone()
            if row:
                return cls(row['name'], row['email'], row['age'], row['id'])
        return None

print("9. Simple ORM Example:")

# Create new user
new_user = UserModel("Eve", "eve@example.com", 32)
new_user.save()
print(f"   Created user: {new_user.name} (ID: {new_user.id})")

# Find user
found_user = UserModel.find_by_id(1)
if found_user:
    print(f"   Found user: {found_user.name}\n")

# PREPARED STATEMENTS (Concept)
print("10. Prepared Statements:")
print("    Use parameterized queries for:")
print("    - Security (prevents SQL injection)")
print("    - Performance (query plan cached)")
print("    - Clarity (separate data from structure)\n")

# DATABASE MIGRATIONS (Concept)
print("11. Database Migrations:")
print("    Tools for managing schema changes:")
print("    - Alembic (SQLAlchemy)")
print("    - Django migrations")
print("    - Manual migration scripts")
print()

# OTHER DATABASE LIBRARIES
print("12. Other Database Libraries:")
libraries = {
    "SQLAlchemy": "Full-featured ORM",
    "psycopg2": "PostgreSQL adapter",
    "mysql-connector": "MySQL adapter",
    "pymongo": "MongoDB (NoSQL)",
    "redis-py": "Redis (key-value store)"
}

for lib, desc in libraries.items():
    print(f"    {lib}: {desc}")

print()

# BEST PRACTICES
print("13. Best Practices:")
print("    ✓ Always use parameterized queries")
print("    ✓ Use context managers for connections")
print("    ✓ Handle exceptions properly")
print("    ✓ Close connections explicitly")
print("    ✓ Use connection pooling for production")
print("    ✓ Consider using ORM for complex projects")
print("    ✓ Index frequently queried columns")
print("    ✓ Use transactions for related operations")
print()

# CLEANUP
import os
if os.path.exists("example.db"):
    os.remove("example.db")
    print("   Cleaned up example.db\n")

print("Database connections demonstration complete!")
print("\nFor production applications:")
print("  - Use SQLAlchemy for complex databases")
print("  - Use connection pooling")
print("  - Implement proper error handling")
print("  - Consider database abstraction layers")

