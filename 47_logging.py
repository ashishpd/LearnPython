"""
47_logging.py

This file demonstrates logging in Python.
Logging is essential for debugging, monitoring, and understanding application behavior.
Covers logging module, levels, handlers, formatters, and best practices.
"""

import logging
import sys

# BASIC LOGGING
# Simple logging setup

print("LOGGING IN PYTHON")
print("=" * 50)

# Basic logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

print("1. Basic Logging:")
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")
print()

# LOGGING LEVELS
# Different severity levels

print("2. Logging Levels (from lowest to highest):")
print("   DEBUG - Detailed information for debugging")
print("   INFO - General informational messages")
print("   WARNING - Warning messages (default level)")
print("   ERROR - Error messages")
print("   CRITICAL - Critical errors")
print()

# CONFIGURE LOGGING
# Customize logging behavior

# Reset logging
logging.root.handlers = []

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)

print("3. Configured Logging:")
logger.info("This is an info message with custom format")
print()

# LOG TO FILE
# Write logs to file

logging.root.handlers = []

file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)

formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

print("4. Multiple Handlers:")
logger.info("This goes to file")
logger.warning("This goes to both file and console")
print("   (Check app.log for file output)\n")

# LOGGER HIERARCHY
# Loggers have hierarchical names

print("5. Logger Hierarchy:")

parent_logger = logging.getLogger("parent")
child_logger = logging.getLogger("parent.child")

parent_logger.setLevel(logging.INFO)
child_logger.setLevel(logging.DEBUG)

print(f"   Parent logger: {parent_logger.name}")
print(f"   Child logger: {child_logger.name}")
print(f"   Is child? {child_logger.parent == parent_logger}")
print()

# CUSTOM LOGGER
# Create logger for specific module

def setup_logger(name, log_file, level=logging.INFO):
    """Create and configure a logger."""
    handler = logging.FileHandler(log_file)
    handler.setFormatter(
        logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    )
    
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    
    return logger

# Create custom logger
custom_logger = setup_logger("custom_module", "custom.log")
custom_logger.info("Custom logger message")
print("6. Custom Logger created\n")

# LOG EXCEPTIONS
# Log exception tracebacks

print("7. Exception Logging:")

def risky_operation():
    """Operation that might fail."""
    raise ValueError("Something went wrong")

try:
    risky_operation()
except Exception as e:
    logger.exception("Exception occurred")  # Logs full traceback
    # logger.error("Exception occurred", exc_info=True)  # Alternative

print()

# ROTATING FILE HANDLER
# Rotate log files when they get large

from logging.handlers import RotatingFileHandler

rotating_handler = RotatingFileHandler(
    'rotating.log',
    maxBytes=1024,  # 1KB for demo
    backupCount=3
)
rotating_handler.setFormatter(formatter)

rotating_logger = logging.getLogger("rotating")
rotating_logger.addHandler(rotating_handler)
rotating_logger.setLevel(logging.INFO)

rotating_logger.info("This will rotate when file gets large")
print("8. Rotating File Handler created\n")

# TIMED ROTATING HANDLER
# Rotate logs based on time

from logging.handlers import TimedRotatingFileHandler

timed_handler = TimedRotatingFileHandler(
    'timed.log',
    when='midnight',
    interval=1,
    backupCount=7
)
timed_handler.setFormatter(formatter)

timed_logger = logging.getLogger("timed")
timed_logger.addHandler(timed_handler)

print("9. Timed Rotating Handler (rotates daily)\n")

# STRUCTURED LOGGING
# Log structured data

import json

class StructuredFormatter(logging.Formatter):
    """Formatter for structured logging."""
    
    def format(self, record):
        log_data = {
            'timestamp': self.formatTime(record),
            'level': record.levelname,
            'logger': record.name,
            'message': record.getMessage(),
        }
        
        # Add extra fields
        if hasattr(record, 'user_id'):
            log_data['user_id'] = record.user_id
        
        return json.dumps(log_data)

structured_handler = logging.StreamHandler()
structured_handler.setFormatter(StructuredFormatter())

structured_logger = logging.getLogger("structured")
structured_logger.addHandler(structured_handler)
structured_logger.setLevel(logging.INFO)

print("10. Structured Logging:")
structured_logger.info("User action", extra={"user_id": "12345"})
print()

# FILTERS
# Filter log messages

class LevelFilter(logging.Filter):
    """Filter by exact level match."""
    
    def __init__(self, level):
        super().__init__()
        self.level = level
    
    def filter(self, record):
        return record.levelno == self.level

# Apply filter
error_filter = LevelFilter(logging.ERROR)
error_handler = logging.StreamHandler()
error_handler.addFilter(error_filter)
error_handler.setFormatter(formatter)

filtered_logger = logging.getLogger("filtered")
filtered_logger.addHandler(error_handler)

print("11. Filters:")
filtered_logger.info("This won't appear")
filtered_logger.warning("This won't appear")
filtered_logger.error("This will appear (filtered)")
print()

# LOGGING CONFIGURATION
# Configure from dictionary or file

config = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '%(asctime)s - %(levelname)s - %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'default',
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['console'],
    },
}

logging.config.dictConfig(config)
print("12. Dict Configuration applied\n")

# BEST PRACTICES
print("13. Logging Best Practices:")
print("   ✓ Use appropriate log levels")
print("   ✓ Include context in messages")
print("   ✓ Use structured logging for production")
print("   ✓ Rotate log files")
print("   ✓ Don't log sensitive information")
print("   ✓ Use logger.exception() for exceptions")
print("   ✓ Set appropriate levels per module")
print("   ✓ Use meaningful logger names")
print()

# EXAMPLE LOGGER SETUP
print("14. Example Production Setup:")

def setup_production_logging():
    """Setup logging for production."""
    # Clear existing handlers
    logging.root.handlers = []
    
    # File handler
    file_handler = RotatingFileHandler(
        'app.log',
        maxBytes=10*1024*1024,  # 10MB
        backupCount=5
    )
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(
        logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
    )
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    console_handler.setFormatter(
        logging.Formatter('%(levelname)s: %(message)s')
    )
    
    # Root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)
    
    return root_logger

prod_logger = setup_production_logging()
prod_logger.info("Production logger configured")
print("   Production logging configured\n")

# CLEANUP
import os
for log_file in ["app.log", "custom.log", "rotating.log", "timed.log"]:
    if os.path.exists(log_file):
        os.remove(log_file)

print("Logging demonstration complete!")
print("\nQuick reference:")
print("  - logging.basicConfig() - Simple setup")
print("  - Logger objects - Per-module loggers")
print("  - Handlers - Where logs go (file, console, etc.)")
print("  - Formatters - How logs look")
print("  - Filters - What gets logged")

