"""
38_metaclasses.py

This file demonstrates metaclasses in Python.
Metaclasses are classes whose instances are classes themselves.
They control class creation and are powerful but advanced features.
Use sparingly - most problems don't require metaclasses.
"""

# WHAT IS A METACLASS?
# A metaclass is a class that creates classes

print("METACLASSES IN PYTHON")
print("=" * 50)

# UNDERSTANDING TYPE
# type() is the default metaclass

# type() can create classes dynamically
def __init__(self, name):
    self.name = name

def say_hello(self):
    return f"Hello, I'm {self.name}"

# Create class using type(name, bases, dict)
Person = type('Person', (object,), {
    '__init__': __init__,
    'say_hello': say_hello
})

person = Person("Alice")
print(f"Dynamic class: {person.say_hello()}")

# Check metaclass
print(f"Person metaclass: {type(Person)}")
print(f"Person instance type: {type(person)}\n")

# BASIC METACLASS
# Custom metaclass that modifies class creation

class MyMeta(type):
    """Custom metaclass."""
    
    def __new__(cls, name, bases, attrs):
        """Called when creating a new class."""
        print(f"Creating class: {name}")
        
        # Modify attributes before class creation
        if 'add_prefix' in attrs:
            # Add prefix to all methods
            new_attrs = {}
            for key, value in attrs.items():
                if key.startswith('method_'):
                    new_attrs[f'prefixed_{key}'] = value
                else:
                    new_attrs[key] = value
            attrs = new_attrs
        
        # Create the class
        return super().__new__(cls, name, bases, attrs)
    
    def __init__(cls, name, bases, attrs):
        """Called after class is created."""
        super().__init__(name, bases, attrs)
        cls._meta_created = True

# Use metaclass
class MyClass(metaclass=MyMeta):
    """Class using custom metaclass."""
    
    def method_test(self):
        return "test"

print(f"MyClass created: {hasattr(MyClass, '_meta_created')}\n")

# METACLASS FOR SINGLETON
# Ensure only one instance exists

class SingletonMeta(type):
    """Metaclass that creates singleton classes."""
    
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        """Called when class is instantiated."""
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    """Singleton class using metaclass."""
    
    def __init__(self, value):
        self.value = value

# Test singleton
s1 = Singleton("first")
s2 = Singleton("second")
print(f"Singleton test: s1 is s2 = {s1 is s2}")
print(f"Both have same value: {s1.value == s2.value}\n")

# METACLASS FOR REGISTRATION
# Automatically register classes

class RegistryMeta(type):
    """Metaclass that registers classes."""
    
    registry = {}
    
    def __new__(cls, name, bases, attrs):
        # Create class
        new_class = super().__new__(cls, name, bases, attrs)
        
        # Register if it has a register key
        if hasattr(new_class, 'registry_key'):
            key = getattr(new_class, 'registry_key')
            cls.registry[key] = new_class
        
        return new_class

class PluginA(metaclass=RegistryMeta):
    registry_key = "plugin_a"
    pass

class PluginB(metaclass=RegistryMeta):
    registry_key = "plugin_b"
    pass

print("Registry:")
for key, cls in RegistryMeta.registry.items():
    print(f"  {key}: {cls.__name__}")
print()

# METACLASS FOR VALIDATION
# Validate class attributes at creation time

class ValidatedMeta(type):
    """Metaclass that validates class attributes."""
    
    def __new__(cls, name, bases, attrs):
        # Check for required attributes
        required_attrs = ['required_method', 'required_field']
        
        for attr in required_attrs:
            if attr not in attrs:
                raise TypeError(f"{name} must define {attr}")
        
        return super().__new__(cls, name, bases, attrs)

# This will raise error
try:
    class InvalidClass(metaclass=ValidatedMeta):
        pass
except TypeError as e:
    print(f"Validation error: {e}")

# This will work
class ValidClass(metaclass=ValidatedMeta):
    def required_method(self):
        pass
    
    required_field = "value"

print(f"ValidClass created successfully\n")

# METACLASS FOR METHOD DECORATION
# Automatically wrap methods

def logging_decorator(func):
    """Decorator that logs method calls."""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

class LoggingMeta(type):
    """Metaclass that adds logging to methods."""
    
    def __new__(cls, name, bases, attrs):
        # Wrap all methods with logging
        for attr_name, attr_value in attrs.items():
            if callable(attr_value) and not attr_name.startswith('__'):
                attrs[attr_name] = logging_decorator(attr_value)
        
        return super().__new__(cls, name, bases, attrs)

class LoggedClass(metaclass=LoggingMeta):
    """Class with automatic logging."""
    
    def method1(self):
        return "Method 1"
    
    def method2(self):
        return "Method 2"

obj = LoggedClass()
obj.method1()
obj.method2()
print()

# METACLASS INHERITANCE
# Metaclasses are inherited

class BaseMeta(type):
    def __new__(cls, name, bases, attrs):
        attrs['_meta_tag'] = 'base'
        return super().__new__(cls, name, bases, attrs)

class DerivedMeta(BaseMeta):
    def __new__(cls, name, bases, attrs):
        attrs['_meta_tag'] = 'derived'
        return super().__new__(cls, name, bases, attrs)

class BaseClass(metaclass=BaseMeta):
    pass

class DerivedClass(metaclass=DerivedMeta):
    pass

print(f"BaseClass meta tag: {BaseClass._meta_tag}")
print(f"DerivedClass meta tag: {DerivedClass._meta_tag}\n")

# METACLASS vs CLASS DECORATORS
# Class decorators are often simpler

def class_decorator(cls):
    """Alternative to metaclass for simple modifications."""
    cls._decorated = True
    return cls

@class_decorator
class DecoratedClass:
    pass

print(f"Class decorator approach: {hasattr(DecoratedClass, '_decorated')}\n")

# __NEW__ VS __INIT__ IN METACLASSES
# __new__ creates, __init__ initializes

class DetailedMeta(type):
    def __new__(cls, name, bases, attrs):
        """Create the class object."""
        print(f"__new__ called for {name}")
        return super().__new__(cls, name, bases, attrs)
    
    def __init__(cls, name, bases, attrs):
        """Initialize the class (after creation)."""
        print(f"__init__ called for {name}")
        super().__init__(name, bases, attrs)

class Example(metaclass=DetailedMeta):
    pass

print()

# PRACTICAL EXAMPLE: ORM-STYLE METACLASS
# Simulate database table mapping

class ModelMeta(type):
    """Metaclass for model classes."""
    
    def __new__(cls, name, bases, attrs):
        # Collect field definitions
        fields = {}
        for key, value in attrs.items():
            if isinstance(value, Field):
                fields[key] = value
        
        # Store fields in class
        attrs['_fields'] = fields
        attrs['_table_name'] = attrs.get('table_name', name.lower())
        
        return super().__new__(cls, name, bases, attrs)

class Field:
    """Field descriptor."""
    def __init__(self, field_type):
        self.field_type = field_type

class Model(metaclass=ModelMeta):
    """Base model class."""
    pass

class User(Model):
    table_name = 'users'
    name = Field(str)
    age = Field(int)

print("ORM-style example:")
print(f"  Table name: {User._table_name}")
print(f"  Fields: {list(User._fields.keys())}\n")

# WHEN TO USE METACLASSES
print("WHEN TO USE METACLASSES:")
print("  ✓ Framework development (Django ORM, SQLAlchemy)")
print("  ✓ API generation")
print("  ✓ Automatic code generation")
print("  ✗ Usually overkill for regular applications")
print("  ✗ Prefer decorators or __init_subclass__ for most cases")
print()

print("Metaclasses demonstration complete!")

