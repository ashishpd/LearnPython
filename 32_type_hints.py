"""
32_type_hints.py

This file demonstrates type hints in Python.
Type hints help document code and enable static type checking.
They don't affect runtime behavior but improve code quality and IDE support.
"""

# BASIC TYPE HINTS
# Annotate variables and function parameters

from typing import List, Dict, Optional, Union, Tuple, Any, Callable

# Variable type hints
name: str = "Python"
age: int = 30
price: float = 19.99
is_active: bool = True

# Function type hints
def greet(name: str) -> str:
    """Function with type hints."""
    return f"Hello, {name}!"

result: str = greet("Alice")
print(f"Result: {result}\n")

# COMPLEX TYPE HINTS - Lists
# Specify the type of elements in a list

def process_numbers(numbers: List[int]) -> List[int]:
    """Process a list of integers."""
    return [n * 2 for n in numbers]

numbers: List[int] = [1, 2, 3, 4, 5]
doubled = process_numbers(numbers)
print(f"Doubled: {doubled}\n")

# COMPLEX TYPE HINTS - Dictionaries
# Specify key and value types

def process_scores(scores: Dict[str, int]) -> Dict[str, str]:
    """Process scores dictionary."""
    return {name: f"Grade: {score}" for name, score in scores.items()}

student_scores: Dict[str, int] = {"Alice": 95, "Bob": 87, "Charlie": 92}
grades = process_scores(student_scores)
print(f"Grades: {grades}\n")

# OPTIONAL TYPES
# Use Optional for values that can be None

def find_user(user_id: int) -> Optional[str]:
    """Find user, may return None."""
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)

user = find_user(1)
print(f"User 1: {user}")
user2 = find_user(99)
print(f"User 99: {user2}\n")

# UNION TYPES
# Accept multiple types

def process_id(user_id: Union[int, str]) -> str:
    """Process ID that can be int or string."""
    return f"ID: {user_id}"

print(f"Int ID: {process_id(123)}")
print(f"String ID: {process_id('abc')}\n")

# TUPLES
# Specify types for each tuple element

def get_coordinates() -> Tuple[float, float]:
    """Return x, y coordinates."""
    return (10.5, 20.3)

x, y = get_coordinates()
print(f"Coordinates: ({x}, {y})\n")

# CALLABLE
# Type hint for functions

def apply_operation(numbers: List[int], operation: Callable[[int], int]) -> List[int]:
    """Apply a function to each number."""
    return [operation(n) for n in numbers]

square = lambda x: x ** 2
squared = apply_operation([1, 2, 3, 4], square)
print(f"Squared: {squared}\n")

# ANY TYPE
# When type is unknown or dynamic

def process_data(data: Any) -> Any:
    """Process data of any type."""
    return data

# GENERIC TYPES
# Create reusable type hints

from typing import TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):
    """Generic stack class."""
    
    def __init__(self):
        self.items: List[T] = []
    
    def push(self, item: T) -> None:
        """Push item onto stack."""
        self.items.append(item)
    
    def pop(self) -> T:
        """Pop item from stack."""
        return self.items.pop()

# Use with specific types
int_stack: Stack[int] = Stack()
int_stack.push(1)
int_stack.push(2)
print(f"Popped: {int_stack.pop()}\n")

# TYPE ALIASES
# Create custom type names for clarity

UserId = int
UserName = str
UserDict = Dict[UserId, UserName]

def get_user(user_id: UserId) -> Optional[UserName]:
    """Get user by ID."""
    users: UserDict = {1: "Alice", 2: "Bob"}
    return users.get(user_id)

print(f"User 1: {get_user(1)}\n")

# LITERAL TYPES
# Restrict to specific values

from typing import Literal

def process_status(status: Literal["active", "inactive", "pending"]) -> str:
    """Process status with specific values."""
    return f"Status: {status}"

print(f"Status: {process_status('active')}\n")

# TYPE VARIABLES
# For generic functions

from typing import TypeVar

T = TypeVar('T')

def first_item(items: List[T]) -> Optional[T]:
    """Get first item from list."""
    return items[0] if items else None

print(f"First string: {first_item(['a', 'b', 'c'])}")
print(f"First int: {first_item([1, 2, 3])}\n")

# CLASS TYPE HINTS
# Type hints for class methods and attributes

class Person:
    """Person class with type hints."""
    
    def __init__(self, name: str, age: int) -> None:
        """Initialize person."""
        self.name: str = name
        self.age: int = age
        self.friends: List[str] = []
    
    def add_friend(self, friend: str) -> None:
        """Add a friend."""
        self.friends.append(friend)
    
    def get_info(self) -> str:
        """Get person info."""
        return f"{self.name}, age {self.age}"

person = Person("Alice", 30)
person.add_friend("Bob")
print(f"Person: {person.get_info()}\n")

# OVERLOADING
# Different signatures for same function

from typing import overload

@overload
def process(value: int) -> str:
    """Process integer."""
    ...

@overload
def process(value: str) -> int:
    """Process string."""
    ...

def process(value: Union[int, str]) -> Union[str, int]:
    """Process value based on type."""
    if isinstance(value, int):
        return str(value)
    return len(value)

print(f"Process int: {process(123)}")
print(f"Process str: {process('hello')}\n")

# FIXED-SIZE LISTS (TYPING EXTENSIONS)
# For Python 3.9+ use built-in types

# Python 3.9+ syntax (preferred)
def modern_types_example():
    """Modern type hints (Python 3.9+)."""
    # Instead of List[int], use list[int]
    numbers: list[int] = [1, 2, 3]
    
    # Instead of Dict[str, int], use dict[str, int]
    scores: dict[str, int] = {"Alice": 95}
    
    # Instead of Optional[str], use str | None
    name: str | None = None
    
    return numbers, scores, name

# TYPE CHECKING AT RUNTIME
# Use TYPE_CHECKING to avoid import overhead

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # This import only happens during type checking
    from typing import Final

# Constants with type hints
MAX_SIZE: int = 100
API_URL: str = "https://api.example.com"

print(f"Constants: MAX_SIZE={MAX_SIZE}, API_URL={API_URL}\n")

# FINAL
# Mark values that shouldn't be reassigned

from typing import Final

MAX_CONNECTIONS: Final[int] = 10
# MAX_CONNECTIONS = 20  # Type checker will warn

print(f"Final constant: {MAX_CONNECTIONS}\n")

print("Type hints demonstration complete!")

