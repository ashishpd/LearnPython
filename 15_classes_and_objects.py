"""
15_classes_and_objects.py

This file demonstrates classes and objects in Python.
Classes are blueprints for creating objects (instances).
Object-oriented programming helps organize and structure code.
"""

# DEFINING A CLASS
# A class is a blueprint for creating objects

class Dog:
    """A simple Dog class."""
    
    # Class attribute (shared by all instances)
    species = "Canis familiaris"
    
    # __init__ method (constructor) - called when object is created
    def __init__(self, name, age):
        """Initialize a Dog instance."""
        # Instance attributes (unique to each instance)
        self.name = name
        self.age = age
    
    # Instance method
    def bark(self):
        """Make the dog bark."""
        return f"{self.name} says: Woof!"
    
    def get_info(self):
        """Return information about the dog."""
        return f"{self.name} is {self.age} years old."

# CREATING OBJECTS (INSTANCES)
# Create instances of the Dog class

dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print("Dog 1:", dog1.get_info())
print("Dog 2:", dog2.get_info())
print(f"\nDog 1 bark: {dog1.bark()}")
print(f"Dog 2 bark: {dog2.bark()}")

# ACCESSING ATTRIBUTES
print(f"\n{dog1.name} is a {dog1.species}")
print(f"{dog2.name} is a {dog2.species}")

# MODIFYING ATTRIBUTES
dog1.age = 4
print(f"\nUpdated age: {dog1.get_info()}")

# CLASS VS INSTANCE ATTRIBUTES

class Circle:
    """A Circle class demonstrating class and instance attributes."""
    
    # Class attribute
    pi = 3.14159
    
    def __init__(self, radius):
        """Initialize a Circle instance."""
        # Instance attribute
        self.radius = radius
    
    def area(self):
        """Calculate and return the area of the circle."""
        return Circle.pi * self.radius ** 2
        # Could also use self.pi

circle1 = Circle(5)
circle2 = Circle(10)

print(f"\nCircle 1 area: {circle1.area():.2f}")
print(f"Circle 2 area: {circle2.area():.2f}")
print(f"Pi value: {Circle.pi}")

# METHODS

class BankAccount:
    """A BankAccount class demonstrating different method types."""
    
    def __init__(self, account_number, balance=0):
        """Initialize a BankAccount instance."""
        self.account_number = account_number
        self.balance = balance
    
    # Instance method - operates on instance
    def deposit(self, amount):
        """Deposit money into account."""
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        return "Deposit amount must be positive"
    
    def withdraw(self, amount):
        """Withdraw money from account."""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        return "Invalid withdrawal amount"
    
    def get_balance(self):
        """Get current account balance."""
        return self.balance

account = BankAccount("12345", 100)
print(f"\n{account.deposit(50)}")
print(f"{account.withdraw(30)}")
print(f"Current balance: ${account.get_balance()}")

# STRING REPRESENTATION
# __str__ and __repr__ methods

class Person:
    """A Person class with string representation."""
    
    def __init__(self, name, age):
        """Initialize a Person instance."""
        self.name = name
        self.age = age
    
    def __str__(self):
        """String representation for users (informal)."""
        return f"Person(name={self.name}, age={self.age})"
    
    def __repr__(self):
        """String representation for developers (formal)."""
        return f"Person('{self.name}', {self.age})"

person = Person("Alice", 30)
print(f"\n__str__: {str(person)}")
print(f"__repr__: {repr(person)}")
print(f"Direct print: {person}")  # Calls __str__

# PRIVATE ATTRIBUTES (CONVENTION)
# Prefix with underscore to indicate "private" (Python doesn't enforce privacy)

class Student:
    """A Student class demonstrating private attributes."""
    
    def __init__(self, name, student_id):
        """Initialize a Student instance."""
        self.name = name  # Public attribute
        self._grade = None  # Protected attribute (convention)
        self.__id = student_id  # Private attribute (name mangling)
    
    def set_grade(self, grade):
        """Set the student's grade."""
        if 0 <= grade <= 100:
            self._grade = grade
        else:
            print("Grade must be between 0 and 100")
    
    def get_grade(self):
        """Get the student's grade."""
        return self._grade

student = Student("Bob", "S12345")
student.set_grade(85)
print(f"\nStudent: {student.name}")
print(f"Grade: {student.get_grade()}")

# PROPERTIES (GETTERS AND SETTERS)
# Use @property decorator for controlled attribute access

class Temperature:
    """A Temperature class using properties."""
    
    def __init__(self, celsius):
        """Initialize a Temperature instance."""
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Get temperature in Celsius."""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Set temperature in Celsius."""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Get temperature in Fahrenheit."""
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set temperature from Fahrenheit."""
        self.celsius = (value - 32) * 5/9

temp = Temperature(25)
print(f"\nTemperature: {temp.celsius}°C = {temp.fahrenheit}°F")
temp.fahrenheit = 86
print(f"After setting to 86°F: {temp.celsius}°C")

