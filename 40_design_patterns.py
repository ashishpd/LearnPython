"""
40_design_patterns.py

This file demonstrates common design patterns in Python.
Design patterns are reusable solutions to common programming problems.
Python's dynamic nature makes some patterns simpler than in other languages.
"""

# SINGLETON PATTERN
# Ensure only one instance exists

class Singleton:
    """Singleton pattern implementation."""
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Test singleton
s1 = Singleton()
s2 = Singleton()
print("Singleton Pattern:")
print(f"  s1 is s2: {s1 is s2}")
print()

# FACTORY PATTERN
# Create objects without specifying exact class

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class AnimalFactory:
    """Factory for creating animals."""
    
    @staticmethod
    def create_animal(animal_type):
        """Create animal based on type."""
        animals = {
            "dog": Dog,
            "cat": Cat,
        }
        
        animal_class = animals.get(animal_type.lower())
        if animal_class:
            return animal_class()
        raise ValueError(f"Unknown animal type: {animal_type}")

# Use factory
dog = AnimalFactory.create_animal("dog")
cat = AnimalFactory.create_animal("cat")

print("Factory Pattern:")
print(f"  Dog: {dog.speak()}")
print(f"  Cat: {cat.speak()}\n")

# OBSERVER PATTERN
# Notify multiple objects of state changes

class Subject:
    """Subject that observers watch."""
    
    def __init__(self):
        self._observers = []
        self._state = None
    
    def attach(self, observer):
        """Attach observer."""
        self._observers.append(observer)
    
    def detach(self, observer):
        """Detach observer."""
        self._observers.remove(observer)
    
    def notify(self):
        """Notify all observers."""
        for observer in self._observers:
            observer.update(self._state)
    
    def set_state(self, state):
        """Set state and notify observers."""
        self._state = state
        self.notify()

class Observer:
    """Observer interface."""
    
    def update(self, state):
        """Called when subject changes."""
        pass

class ConcreteObserver(Observer):
    """Concrete observer."""
    
    def __init__(self, name):
        self.name = name
    
    def update(self, state):
        print(f"  {self.name} received update: {state}")

# Test observer pattern
subject = Subject()
observer1 = ConcreteObserver("Observer 1")
observer2 = ConcreteObserver("Observer 2")

subject.attach(observer1)
subject.attach(observer2)

print("Observer Pattern:")
subject.set_state("New State")
print()

# STRATEGY PATTERN
# Encapsulate algorithms and make them interchangeable

class PaymentStrategy:
    """Strategy interface."""
    
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Paid ${amount} using Credit Card"

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Paid ${amount} using PayPal"

class BitcoinPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Paid ${amount} using Bitcoin"

class ShoppingCart:
    """Shopping cart using strategy pattern."""
    
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy
        self.items = []
    
    def add_item(self, item, price):
        self.items.append((item, price))
    
    def checkout(self):
        total = sum(price for _, price in self.items)
        return self.payment_strategy.pay(total)

# Test strategy pattern
cart = ShoppingCart(CreditCardPayment())
cart.add_item("Book", 20)
cart.add_item("Pen", 5)

print("Strategy Pattern:")
print(f"  {cart.checkout()}\n")

# DECORATOR PATTERN
# Add behavior to objects dynamically

class Component:
    """Component interface."""
    
    def operation(self):
        return "Component"

class ConcreteComponent(Component):
    def operation(self):
        return "ConcreteComponent"

class Decorator(Component):
    """Base decorator."""
    
    def __init__(self, component):
        self.component = component
    
    def operation(self):
        return self.component.operation()

class ConcreteDecoratorA(Decorator):
    def operation(self):
        return f"DecoratorA({self.component.operation()})"

class ConcreteDecoratorB(Decorator):
    def operation(self):
        return f"DecoratorB({self.component.operation()})"

# Test decorator pattern
component = ConcreteComponent()
decorated = ConcreteDecoratorA(ConcreteDecoratorB(component))

print("Decorator Pattern:")
print(f"  {decorated.operation()}\n")

# ADAPTER PATTERN
# Make incompatible interfaces work together

class OldSystem:
    """Old system with different interface."""
    
    def old_method(self):
        return "Old System Output"

class NewSystem:
    """New system interface."""
    
    def new_method(self):
        pass

class Adapter(NewSystem):
    """Adapter that makes OldSystem work with NewSystem."""
    
    def __init__(self, old_system):
        self.old_system = old_system
    
    def new_method(self):
        return self.old_system.old_method()

# Test adapter
old = OldSystem()
adapter = Adapter(old)

print("Adapter Pattern:")
print(f"  {adapter.new_method()}\n")

# FACADE PATTERN
# Provide simplified interface to complex subsystem

class SubsystemA:
    def operation_a(self):
        return "Subsystem A"

class SubsystemB:
    def operation_b(self):
        return "Subsystem B"

class SubsystemC:
    def operation_c(self):
        return "Subsystem C"

class Facade:
    """Facade that simplifies subsystem access."""
    
    def __init__(self):
        self.subsystem_a = SubsystemA()
        self.subsystem_b = SubsystemB()
        self.subsystem_c = SubsystemC()
    
    def operation(self):
        """Simplified operation."""
        return f"{self.subsystem_a.operation_a()}, {self.subsystem_b.operation_b()}, {self.subsystem_c.operation_c()}"

# Test facade
facade = Facade()
print("Facade Pattern:")
print(f"  {facade.operation()}\n")

# TEMPLATE METHOD PATTERN
# Define algorithm skeleton, let subclasses fill details

class AbstractClass:
    """Abstract class with template method."""
    
    def template_method(self):
        """Template method defining algorithm."""
        self.step1()
        self.step2()
        self.step3()
    
    def step1(self):
        print("  Default step 1")
    
    def step2(self):
        raise NotImplementedError
    
    def step3(self):
        print("  Default step 3")

class ConcreteClass(AbstractClass):
    def step2(self):
        print("  Custom step 2")

print("Template Method Pattern:")
concrete = ConcreteClass()
concrete.template_method()
print()

# COMMAND PATTERN
# Encapsulate requests as objects

class Command:
    """Command interface."""
    
    def execute(self):
        pass

class Light:
    """Receiver."""
    
    def turn_on(self):
        return "Light is ON"
    
    def turn_off(self):
        return "Light is OFF"

class TurnOnCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        return self.light.turn_on()

class TurnOffCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        return self.light.turn_off()

class RemoteControl:
    """Invoker."""
    
    def __init__(self):
        self.command = None
    
    def set_command(self, command):
        self.command = command
    
    def press_button(self):
        if self.command:
            return self.command.execute()
        return "No command set"

# Test command pattern
light = Light()
remote = RemoteControl()

remote.set_command(TurnOnCommand(light))
print("Command Pattern:")
print(f"  {remote.press_button()}")

remote.set_command(TurnOffCommand(light))
print(f"  {remote.press_button()}\n")

# STATE PATTERN
# Allow object to alter behavior when state changes

class State:
    """State interface."""
    
    def handle(self, context):
        pass

class ConcreteStateA(State):
    def handle(self, context):
        print("  State A handling")
        context.state = ConcreteStateB()

class ConcreteStateB(State):
    def handle(self, context):
        print("  State B handling")
        context.state = ConcreteStateA()

class Context:
    """Context that changes state."""
    
    def __init__(self):
        self.state = ConcreteStateA()
    
    def request(self):
        self.state.handle(self)

# Test state pattern
context = Context()
print("State Pattern:")
context.request()
context.request()
context.request()
print()

# BUILDER PATTERN
# Construct complex objects step by step

class Computer:
    """Product to build."""
    
    def __init__(self):
        self.cpu = None
        self.memory = None
        self.storage = None
    
    def __str__(self):
        return f"Computer: CPU={self.cpu}, Memory={self.memory}, Storage={self.storage}"

class ComputerBuilder:
    """Builder for Computer."""
    
    def __init__(self):
        self.computer = Computer()
    
    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self
    
    def set_memory(self, memory):
        self.computer.memory = memory
        return self
    
    def set_storage(self, storage):
        self.computer.storage = storage
        return self
    
    def build(self):
        return self.computer

# Test builder pattern
builder = ComputerBuilder()
computer = (builder
            .set_cpu("Intel i7")
            .set_memory("16GB")
            .set_storage("512GB SSD")
            .build())

print("Builder Pattern:")
print(f"  {computer}\n")

# PROXY PATTERN
# Provide placeholder for another object

class Subject:
    """Subject interface."""
    
    def request(self):
        pass

class RealSubject(Subject):
    """Real subject."""
    
    def request(self):
        return "RealSubject: Handling request"

class Proxy(Subject):
    """Proxy that controls access."""
    
    def __init__(self):
        self._real_subject = None
    
    def request(self):
        if self._real_subject is None:
            self._real_subject = RealSubject()
        return self._real_subject.request()

# Test proxy
proxy = Proxy()
print("Proxy Pattern:")
print(f"  {proxy.request()}\n")

print("Design patterns demonstration complete!")

