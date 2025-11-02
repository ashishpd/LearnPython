"""
39_descriptors.py

This file demonstrates descriptors in Python.
Descriptors are objects that define how attribute access works.
They enable properties, static methods, class methods, and more.
"""

# WHAT ARE DESCRIPTORS?
# Objects that define __get__, __set__, or __delete__

print("DESCRIPTORS IN PYTHON")
print("=" * 50)

# BASIC DESCRIPTOR
# Implement descriptor protocol

class SimpleDescriptor:
    """Basic descriptor."""
    
    def __get__(self, obj, objtype=None):
        """Called when attribute is accessed."""
        print(f"__get__ called with obj={obj}, objtype={objtype}")
        return "descriptor value"
    
    def __set__(self, obj, value):
        """Called when attribute is set."""
        print(f"__set__ called with obj={obj}, value={value}")
    
    def __delete__(self, obj):
        """Called when attribute is deleted."""
        print(f"__delete__ called with obj={obj}")

class MyClass:
    attr = SimpleDescriptor()

obj = MyClass()
print("Accessing attribute:")
value = obj.attr
print(f"Value: {value}\n")

print("Setting attribute:")
obj.attr = "new value\n"

print("Deleting attribute:")
del obj.attr
print()

# DATA DESCRIPTOR (has __set__)
# Takes precedence over instance dictionary

class ValidatedDescriptor:
    """Descriptor with validation."""
    
    def __init__(self, name):
        self.name = name
        self.storage_name = f"_{name}"
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.storage_name, None)
    
    def __set__(self, obj, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError(f"{self.name} must be a non-negative integer")
        setattr(obj, self.storage_name, value)

class Product:
    price = ValidatedDescriptor("price")
    quantity = ValidatedDescriptor("quantity")
    
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

product = Product(10, 5)
print(f"Product price: {product.price}, quantity: {product.quantity}")

try:
    product.price = -5
except ValueError as e:
    print(f"Validation error: {e}\n")

# NON-DATA DESCRIPTOR (no __set__)
# Instance dictionary takes precedence

class ReadOnlyDescriptor:
    """Non-data descriptor (read-only)."""
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return "read-only value"

class Example:
    attr = ReadOnlyDescriptor()

obj = Example()
print(f"Read-only value: {obj.attr}")

# Instance attribute overrides non-data descriptor
obj.attr = "instance value"
print(f"After setting: {obj.attr}\n")

# PROPERTY DESCRIPTOR
# Built-in descriptor for getter/setter/deleter

class Temperature:
    """Temperature with property descriptor."""
    
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Get temperature in Celsius."""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Set temperature in Celsius."""
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Get temperature in Fahrenheit."""
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set temperature in Fahrenheit."""
        self.celsius = (value - 32) * 5/9

temp = Temperature(25)
print(f"Temperature in Celsius: {temp.celsius}°C")
print(f"Temperature in Fahrenheit: {temp.fahrenheit}°F")

temp.fahrenheit = 100
print(f"After setting 100°F: {temp.celsius}°C\n")

# CACHED PROPERTY
# Descriptor that caches computed values

class CachedProperty:
    """Cached property descriptor."""
    
    def __init__(self, func):
        self.func = func
        self.name = func.__name__
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        
        # Check cache
        cache_name = f"_{self.name}_cached"
        if not hasattr(obj, cache_name):
            value = self.func(obj)
            setattr(obj, cache_name, value)
        
        return getattr(obj, cache_name)

class DataProcessor:
    """Example using cached property."""
    
    def __init__(self, data):
        self.data = data
    
    @CachedProperty
    def expensive_computation(self):
        """Expensive computation cached after first call."""
        print("Computing...")
        return sum(x ** 2 for x in self.data)

processor = DataProcessor([1, 2, 3, 4, 5])
print(f"First call: {processor.expensive_computation}")
print(f"Second call (cached): {processor.expensive_computation}\n")

# DESCRIPTOR FOR TYPE VALIDATION
# Validate types automatically

class TypedDescriptor:
    """Descriptor that enforces types."""
    
    def __init__(self, expected_type):
        self.expected_type = expected_type
        self.name = None
    
    def __set_name__(self, owner, name):
        """Called when descriptor is assigned to class."""
        self.name = name
        self.storage_name = f"_{name}"
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.storage_name, None)
    
    def __set__(self, obj, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(
                f"{self.name} must be of type {self.expected_type.__name__}"
            )
        setattr(obj, self.storage_name, value)

class Person:
    name = TypedDescriptor(str)
    age = TypedDescriptor(int)
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 30)
print(f"Person: {person.name}, {person.age}")

try:
    person.age = "thirty"
except TypeError as e:
    print(f"Type error: {e}\n")

# LAZY DESCRIPTOR
# Compute value on first access

class LazyProperty:
    """Lazy property that computes on first access."""
    
    def __init__(self, func):
        self.func = func
        self.name = func.__name__
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        
        value = self.func(obj)
        # Replace descriptor with value
        setattr(obj, self.name, value)
        return value

class Resource:
    """Example using lazy property."""
    
    def __init__(self, config_file):
        self.config_file = config_file
    
    @LazyProperty
    def config(self):
        """Load config only when accessed."""
        print(f"Loading config from {self.config_file}")
        return {"key": "value", "setting": True}

resource = Resource("config.json")
print("Resource created")
print(f"Accessing config: {resource.config}")
print(f"Accessing again: {resource.config}\n")

# DESCRIPTOR FOR OBSERVABLE PROPERTIES
# Notify when values change

class ObservableDescriptor:
    """Descriptor that notifies on changes."""
    
    def __init__(self, name):
        self.name = name
        self.storage_name = f"_{name}"
        self.observers = []
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.storage_name, None)
    
    def __set__(self, obj, value):
        old_value = getattr(obj, self.storage_name, None)
        setattr(obj, self.storage_name, value)
        
        # Notify observers
        if old_value != value:
            for observer in self.observers:
                observer(obj, self.name, old_value, value)
    
    def add_observer(self, callback):
        """Add observer callback."""
        self.observers.append(callback)

def notify(obj, attr_name, old_value, new_value):
    """Observer callback."""
    print(f"{attr_name} changed from {old_value} to {new_value}")

class ObservableModel:
    price = ObservableDescriptor("price")
    
    def __init__(self):
        # Add observer
        type(self).price.add_observer(notify)

model = ObservableModel()
model.price = 10
model.price = 20
print()

# __SET_NAME__ METHOD
# Called when descriptor is assigned to class

class NamedDescriptor:
    """Descriptor that knows its name."""
    
    def __set_name__(self, owner, name):
        """Called when descriptor is assigned."""
        self.owner = owner.__name__
        self.name = name
        self.storage_name = f"_{name}"
        print(f"Descriptor {name} assigned to {owner.__name__}")
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.storage_name, None)
    
    def __set__(self, obj, value):
        setattr(obj, self.storage_name, value)

class NamedClass:
    attr1 = NamedDescriptor()
    attr2 = NamedDescriptor()

obj = NamedClass()
obj.attr1 = "value1"
print(f"attr1 value: {obj.attr1}\n")

# DESCRIPTOR INHERITANCE
# Descriptors work with inheritance

class BaseDescriptor:
    def __get__(self, obj, objtype=None):
        return "base value"

class DerivedDescriptor(BaseDescriptor):
    def __get__(self, obj, objtype=None):
        return "derived value"

class Base:
    attr = BaseDescriptor()

class Derived(Base):
    attr = DerivedDescriptor()

base = Base()
derived = Derived()

print(f"Base attr: {base.attr}")
print(f"Derived attr: {derived.attr}\n")

# WHEN TO USE DESCRIPTORS
print("WHEN TO USE DESCRIPTORS:")
print("  ✓ Property getters/setters/deleters")
print("  ✓ Type validation")
print("  ✓ Caching computed values")
print("  ✓ Lazy initialization")
print("  ✓ Framework development (Django, SQLAlchemy)")
print("  ✗ Simple attributes don't need descriptors")
print()

print("Descriptors demonstration complete!")

