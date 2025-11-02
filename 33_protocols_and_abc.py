"""
33_protocols_and_abc.py

This file demonstrates Protocols (structural typing) and Abstract Base Classes (ABC).
Protocols define "duck typing" interfaces, while ABCs define inheritance-based interfaces.
Both enable polymorphism and code that works with multiple types.
"""

from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable

# ABSTRACT BASE CLASSES (ABC)
# Define interfaces through inheritance

class Animal(ABC):
    """Abstract base class for animals."""
    
    @abstractmethod
    def speak(self) -> str:
        """Animal must be able to speak."""
        pass
    
    @abstractmethod
    def move(self) -> str:
        """Animal must be able to move."""
        pass
    
    def describe(self) -> str:
        """Non-abstract method available to all animals."""
        return f"{self.speak()} and {self.move()}"

# Concrete implementation
class Dog(Animal):
    """Dog implements Animal interface."""
    
    def speak(self) -> str:
        return "Woof!"
    
    def move(self) -> str:
        return "runs"

class Cat(Animal):
    """Cat implements Animal interface."""
    
    def speak(self) -> str:
        return "Meow!"
    
    def move(self) -> str:
        return "walks"

dog = Dog()
cat = Cat()

print("Abstract Base Classes:")
print(f"Dog: {dog.describe()}")
print(f"Cat: {cat.describe()}\n")

# ABC WITH PROPERTIES
# Abstract properties

class Shape(ABC):
    """Abstract base class for shapes."""
    
    @property
    @abstractmethod
    def area(self) -> float:
        """Area must be implemented."""
        pass
    
    @property
    @abstractmethod
    def perimeter(self) -> float:
        """Perimeter must be implemented."""
        pass

class Rectangle(Shape):
    """Rectangle implementation."""
    
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height
    
    @property
    def area(self) -> float:
        return self._width * self._height
    
    @property
    def perimeter(self) -> float:
        return 2 * (self._width + self._height)

rect = Rectangle(5, 3)
print(f"Rectangle area: {rect.area}, perimeter: {rect.perimeter}\n")

# PROTOCOLS (STRUCTURAL TYPING)
# Define interfaces by structure, not inheritance

class Drawable(Protocol):
    """Protocol for objects that can be drawn."""
    
    def draw(self) -> str:
        """Object must have a draw method."""
        ...

def render(item: Drawable) -> str:
    """Render any drawable item."""
    return item.draw()

# Class doesn't need to inherit from Drawable
class Circle:
    """Circle implements Drawable protocol by structure."""
    
    def __init__(self, radius: float):
        self.radius = radius
    
    def draw(self) -> str:
        return f"Drawing circle with radius {self.radius}"

class Square:
    """Square implements Drawable protocol."""
    
    def __init__(self, side: float):
        self.side = side
    
    def draw(self) -> str:
        return f"Drawing square with side {self.side}"

circle = Circle(5)
square = Square(4)

print("Protocols (Structural Typing):")
print(f"Circle: {render(circle)}")
print(f"Square: {render(square)}\n")

# RUNTIME_CHECKABLE PROTOCOLS
# Check protocol conformance at runtime

@runtime_checkable
class Serializable(Protocol):
    """Protocol for serializable objects."""
    
    def to_dict(self) -> dict:
        """Convert to dictionary."""
        ...

def check_serializable(obj):
    """Check if object is serializable."""
    if isinstance(obj, Serializable):
        return obj.to_dict()
    return None

class Person:
    """Person implements Serializable protocol."""
    
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def to_dict(self) -> dict:
        return {"name": self.name, "age": self.age}

person = Person("Alice", 30)
result = check_serializable(person)
print(f"Serializable check: {result}\n")

# COMPARABLE PROTOCOL
# Protocol for objects with comparison operators

class Comparable(Protocol):
    """Protocol for comparable objects."""
    
    def __eq__(self, other) -> bool:
        ...
    
    def __lt__(self, other) -> bool:
        ...

def find_min(items: list[Comparable]) -> Comparable:
    """Find minimum item."""
    return min(items)

class Product:
    """Product that's comparable."""
    
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
    
    def __eq__(self, other):
        return isinstance(other, Product) and self.price == other.price
    
    def __lt__(self, other):
        return isinstance(other, Product) and self.price < other.price
    
    def __str__(self):
        return f"{self.name}: ${self.price}"

products = [
    Product("Laptop", 999),
    Product("Mouse", 25),
    Product("Keyboard", 75)
]

cheapest = find_min(products)
print(f"Cheapest product: {cheapest}\n")

# ITERABLE PROTOCOL
# Protocol for objects that can be iterated

class Countdown:
    """Countdown that's iterable."""
    
    def __init__(self, start: int):
        self.start = start
    
    def __iter__(self):
        """Make it iterable."""
        return CountdownIterator(self.start)

class CountdownIterator:
    """Iterator for Countdown."""
    
    def __init__(self, start: int):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

print("Iterable protocol:")
for num in Countdown(5):
    print(f"  {num}")
print()

# CONTEXT MANAGER PROTOCOL
# Protocol for objects that work with 'with' statement

class ManagedResource:
    """Resource managed by context manager protocol."""
    
    def __enter__(self):
        print("Entering context")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")
        return False

print("Context manager protocol:")
with ManagedResource() as resource:
    print("  Inside context")
print()

# ABC vs PROTOCOL COMPARISON
# When to use each

# ABC: Use when you want inheritance-based polymorphism
class Vehicle(ABC):
    """Vehicle ABC."""
    
    @abstractmethod
    def start(self) -> str:
        pass

class Car(Vehicle):
    def start(self) -> str:
        return "Car engine started"

# Protocol: Use when you want structural typing
class Startable(Protocol):
    """Startable protocol."""
    
    def start(self) -> str:
        ...

def start_vehicle(vehicle: Startable) -> str:
    """Start any startable vehicle."""
    return vehicle.start()

# Both work!
print("ABC vs Protocol:")
car = Car()
print(f"ABC: {car.start()}")
print(f"Protocol: {start_vehicle(car)}\n")

# MULTIPLE PROTOCOLS
# Objects can satisfy multiple protocols

class Readable(Protocol):
    def read(self) -> str:
        ...

class Writable(Protocol):
    def write(self, data: str) -> None:
        ...

class File:
    """File satisfies both Readable and Writable."""
    
    def __init__(self, content: str = ""):
        self.content = content
    
    def read(self) -> str:
        return self.content
    
    def write(self, data: str) -> None:
        self.content = data

def read_file(file: Readable) -> str:
    """Read from readable file."""
    return file.read()

def write_file(file: Writable, data: str) -> None:
    """Write to writable file."""
    file.write(data)

file = File()
write_file(file, "Hello, World!")
content = read_file(file)
print(f"Multiple protocols: {content}\n")

print("Protocols and ABC demonstration complete!")

