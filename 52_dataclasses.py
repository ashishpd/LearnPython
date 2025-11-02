"""
52_dataclasses.py

This file demonstrates dataclasses in Python 3.7+.
Dataclasses automatically generate special methods for classes,
reducing boilerplate code.
"""

from dataclasses import dataclass, field, asdict, astuple
from typing import List, Optional

print("DATACLASSES IN PYTHON")
print("=" * 50)

# BASIC DATACLASS
# Simple class with auto-generated methods

print("1. Basic Dataclass:")

@dataclass
class Point:
    """Point with x and y coordinates."""
    x: float
    y: float

p1 = Point(10.0, 20.0)
p2 = Point(10.0, 20.0)

print(f"   Point: {p1}")
print(f"   Equality: {p1 == p2}")
print(f"   Hash: {hash(p1) if hasattr(p1, '__hash__') else 'Not hashable'}\n")

# DATACLASS WITH METHODS
# Add custom methods

print("2. Dataclass with Methods:")

@dataclass
class Person:
    """Person dataclass."""
    name: str
    age: int
    
    def greet(self):
        return f"Hello, I'm {self.name}, {self.age} years old"
    
    def is_adult(self):
        return self.age >= 18

person = Person("Alice", 30)
print(f"   {person.greet()}")
print(f"   Adult: {person.is_adult()}\n")

# DEFAULT VALUES
# Fields with default values

print("3. Default Values:")

@dataclass
class Config:
    """Configuration with defaults."""
    host: str = "localhost"
    port: int = 8080
    debug: bool = False

config1 = Config()
config2 = Config("example.com", 9000, True)

print(f"   Default config: {config1}")
print(f"   Custom config: {config2}\n")

# FIELD FUNCTION
# Advanced field configuration

print("4. Field Function:")

@dataclass
class Product:
    """Product with computed fields."""
    name: str
    price: float
    tags: List[str] = field(default_factory=list)
    _discount: float = field(default=0.1, repr=False)
    
    @property
    def discounted_price(self):
        return self.price * (1 - self._discount)

product = Product("Laptop", 1000.0, ["electronics", "computers"])
print(f"   Product: {product}")
print(f"   Discounted price: {product.discounted_price}\n")

# FROZEN DATACLASS
# Immutable dataclass

print("5. Frozen Dataclass (Immutable):")

@dataclass(frozen=True)
class ImmutablePoint:
    """Immutable point."""
    x: float
    y: float

point = ImmutablePoint(5.0, 10.0)
print(f"   Point: {point}")
print(f"   Hashable: {hash(point)}")

# point.x = 20  # Would raise FrozenInstanceError
print("   (Immutable - cannot modify)\n")

# ORDERING
# Enable comparison operators

print("6. Ordering:")

@dataclass(order=True)
class Student:
    """Student with ordering."""
    name: str = field(compare=False)  # Don't use in comparison
    age: int = field(compare=True)
    grade: float = field(compare=True)

students = [
    Student("Alice", 20, 85.5),
    Student("Bob", 19, 90.0),
    Student("Charlie", 20, 80.0)
]

sorted_students = sorted(students, key=lambda s: (s.age, s.grade))
print(f"   Sorted by age, then grade:")
for s in sorted_students:
    print(f"     {s.name}: age={s.age}, grade={s.grade}")
print()

# POST_INIT
# Custom initialization logic

print("7. __post_init__:")

@dataclass
class Rectangle:
    """Rectangle with validation."""
    width: float
    height: float
    area: float = field(init=False)  # Computed field
    
    def __post_init__(self):
        if self.width <= 0 or self.height <= 0:
            raise ValueError("Dimensions must be positive")
        self.area = self.width * self.height

rect = Rectangle(5.0, 3.0)
print(f"   Rectangle: width={rect.width}, height={rect.height}, area={rect.area}\n")

# INHERITANCE
# Dataclass inheritance

print("8. Inheritance:")

@dataclass
class Animal:
    """Base animal."""
    name: str

@dataclass
class Dog(Animal):
    """Dog inheriting from Animal."""
    breed: str
    age: int = 0

dog = Dog("Buddy", "Golden Retriever", 5)
print(f"   Dog: {dog}\n")

# ASDICT AND ASTUPLE
# Convert to dictionary or tuple

print("9. asdict and astuple:")

@dataclass
class Point3D:
    """3D point."""
    x: float
    y: float
    z: float

point = Point3D(1.0, 2.0, 3.0)
point_dict = asdict(point)
point_tuple = astuple(point)

print(f"   Point: {point}")
print(f"   As dict: {point_dict}")
print(f"   As tuple: {point_tuple}\n")

# REPLACE
# Create modified copy

from dataclasses import replace

print("10. replace (Create Modified Copy):")

@dataclass
class Settings:
    """Settings dataclass."""
    theme: str = "light"
    language: str = "en"
    notifications: bool = True

settings = Settings()
new_settings = replace(settings, theme="dark", notifications=False)

print(f"   Original: {settings}")
print(f"   Modified: {new_settings}\n")

# DATACLASS VS REGULAR CLASS
# Comparison

print("11. Dataclass Benefits:")
print("    ✓ Less boilerplate")
print("    ✓ Auto-generated __init__, __repr__, __eq__")
print("    ✓ Type hints integrated")
print("    ✓ Easy to convert to dict/tuple")
print("    ✓ Field validation with __post_init__")
print()

print("Dataclasses demonstration complete!")
print("\nUse dataclasses when:")
print("  - Classes are mainly data containers")
print("  - You want auto-generated special methods")
print("  - Type hints are important")
print("  - Immutability is desired (frozen=True)")

