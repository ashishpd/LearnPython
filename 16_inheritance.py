"""
16_inheritance.py

This file demonstrates inheritance in Python.
Inheritance allows a class to inherit attributes and methods from another class,
promoting code reuse and creating a hierarchy of classes.
"""

# BASIC INHERITANCE
# Child class inherits from parent class

class Animal:
    """Base class for all animals."""
    
    def __init__(self, name, age):
        """Initialize an Animal instance."""
        self.name = name
        self.age = age
    
    def speak(self):
        """Make the animal speak."""
        return f"{self.name} makes a sound."
    
    def get_info(self):
        """Get information about the animal."""
        return f"{self.name} is {self.age} years old."

# Dog inherits from Animal
class Dog(Animal):
    """Dog class that inherits from Animal."""
    
    def speak(self):
        """Override the speak method."""
        return f"{self.name} says: Woof!"

# Cat inherits from Animal
class Cat(Animal):
    """Cat class that inherits from Animal."""
    
    def speak(self):
        """Override the speak method."""
        return f"{self.name} says: Meow!"

# Creating instances
dog = Dog("Buddy", 3)
cat = Cat("Whiskers", 2)

print("Dog:", dog.speak())
print("Cat:", cat.speak())
print(f"\nDog info: {dog.get_info()}")
print(f"Cat info: {cat.get_info()}")

# USING super()
# Call parent class methods and constructors

class Vehicle:
    """Base class for vehicles."""
    
    def __init__(self, brand, model, year):
        """Initialize a Vehicle instance."""
        self.brand = brand
        self.model = model
        self.year = year
    
    def start(self):
        """Start the vehicle."""
        return f"{self.brand} {self.model} is starting..."
    
    def get_info(self):
        """Get vehicle information."""
        return f"{self.year} {self.brand} {self.model}"

class Car(Vehicle):
    """Car class that inherits from Vehicle."""
    
    def __init__(self, brand, model, year, num_doors):
        """Initialize a Car instance."""
        # Call parent class constructor
        super().__init__(brand, model, year)
        self.num_doors = num_doors
    
    def start(self):
        """Override start method."""
        # Call parent method and extend it
        return super().start() + " Engine started!"

car = Car("Toyota", "Camry", 2023, 4)
print(f"\n{car.get_info()}")
print(f"{car.start()}")
print(f"Number of doors: {car.num_doors}")

# MULTIPLE INHERITANCE
# A class can inherit from multiple parent classes

class Flyable:
    """Mixin class for objects that can fly."""
    
    def fly(self):
        """Make the object fly."""
        return "Flying through the air!"

class Swimmable:
    """Mixin class for objects that can swim."""
    
    def swim(self):
        """Make the object swim."""
        return "Swimming in the water!"

class Duck(Animal, Flyable, Swimmable):
    """Duck class that can both fly and swim."""
    
    def speak(self):
        """Override the speak method."""
        return f"{self.name} says: Quack!"

duck = Duck("Donald", 5)
print(f"\nDuck: {duck.speak()}")
print(f"Duck: {duck.fly()}")
print(f"Duck: {duck.swim()}")

# METHOD RESOLUTION ORDER (MRO)
# Python determines which method to call in multiple inheritance

print(f"\nDuck MRO: {Duck.__mro__}")

# CHECKING INHERITANCE
# Use isinstance() and issubclass()

print(f"\nisinstance(dog, Dog): {isinstance(dog, Dog)}")
print(f"isinstance(dog, Animal): {isinstance(dog, Animal)}")
print(f"issubclass(Dog, Animal): {issubclass(Dog, Animal)}")

# ABSTRACT BASE CLASSES (ABC)
# Define methods that must be implemented by subclasses

from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class for shapes."""
    
    def __init__(self, name):
        """Initialize a Shape instance."""
        self.name = name
    
    @abstractmethod
    def area(self):
        """Calculate area - must be implemented by subclasses."""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculate perimeter - must be implemented by subclasses."""
        pass
    
    def get_info(self):
        """Get shape information."""
        return f"{self.name}: Area={self.area():.2f}, Perimeter={self.perimeter():.2f}"

class Rectangle(Shape):
    """Rectangle class implementing Shape."""
    
    def __init__(self, width, height):
        """Initialize a Rectangle instance."""
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    
    def area(self):
        """Calculate rectangle area."""
        return self.width * self.height
    
    def perimeter(self):
        """Calculate rectangle perimeter."""
        return 2 * (self.width + self.height)

class Circle(Shape):
    """Circle class implementing Shape."""
    
    def __init__(self, radius):
        """Initialize a Circle instance."""
        super().__init__("Circle")
        self.radius = radius
    
    def area(self):
        """Calculate circle area."""
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """Calculate circle circumference."""
        import math
        return 2 * math.pi * self.radius

rect = Rectangle(5, 3)
circle = Circle(4)

print(f"\n{rect.get_info()}")
print(f"{circle.get_info()}")

# OVERRIDING BUILT-IN METHODS
# Customize behavior of operators and built-in functions

class Book:
    """Book class with custom comparison methods."""
    
    def __init__(self, title, pages):
        """Initialize a Book instance."""
        self.title = title
        self.pages = pages
    
    def __str__(self):
        """String representation."""
        return f"'{self.title}' ({self.pages} pages)"
    
    def __len__(self):
        """Return number of pages."""
        return self.pages
    
    def __eq__(self, other):
        """Check equality (same number of pages)."""
        if isinstance(other, Book):
            return self.pages == other.pages
        return False
    
    def __lt__(self, other):
        """Check if less than (fewer pages)."""
        if isinstance(other, Book):
            return self.pages < other.pages
        return NotImplemented

book1 = Book("Python Guide", 300)
book2 = Book("Java Guide", 250)
book3 = Book("JavaScript Guide", 300)

print(f"\n{book1}")
print(f"Length: {len(book1)}")
print(f"book1 == book3: {book1 == book3}")
print(f"book2 < book1: {book2 < book1}")

