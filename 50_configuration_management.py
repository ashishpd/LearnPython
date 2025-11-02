"""
50_configuration_management.py

This file demonstrates configuration management in Python.
Covers ConfigParser, .env files, environment variables, and configuration patterns.
"""

import os
import json
from configparser import ConfigParser

print("CONFIGURATION MANAGEMENT IN PYTHON")
print("=" * 50)

# ENVIRONMENT VARIABLES
# Simple configuration via environment

print("1. Environment Variables:")

# Get environment variable
home_dir = os.environ.get("HOME", "/default/home")
python_path = os.environ.get("PYTHONPATH", "Not set")

print(f"   HOME: {home_dir}")
print(f"   PYTHONPATH: {python_path}")

# Set environment variable (for current process)
os.environ["MY_APP_CONFIG"] = "value"
print(f"   MY_APP_CONFIG: {os.environ.get('MY_APP_CONFIG')}\n")

# CONFIGPARSER - INI FILES
# Parse INI-style configuration files

print("2. ConfigParser (INI Files):")

config = ConfigParser()
config.read_string("""
[Database]
host = localhost
port = 5432
name = mydb
user = admin
password = secret

[API]
base_url = https://api.example.com
timeout = 30
retry_count = 3

[Logging]
level = INFO
file = app.log
""")

# Access configuration
db_host = config.get("Database", "host")
api_timeout = config.getint("API", "timeout")
log_level = config.get("Logging", "level")

print(f"   Database host: {db_host}")
print(f"   API timeout: {api_timeout}")
print(f"   Log level: {log_level}\n")

# WRITE CONFIG FILE
print("3. Writing Config Files:")

config_write = ConfigParser()
config_write.add_section("Settings")
config_write.set("Settings", "debug", "true")
config_write.set("Settings", "port", "8080")

# Write to file
with open("config.ini", "w") as f:
    config_write.write(f)

print("   Config file written to config.ini\n")

# ENV FILES (.env)
# Environment variables from file

env_file_content = """
# .env file example
DATABASE_URL=postgresql://localhost/mydb
API_KEY=your-api-key-here
DEBUG=true
PORT=8080
"""

# Note: Use python-dotenv library
print("4. .env Files:")
print("   Install: pip install python-dotenv")
print("   Usage:")
print("     from dotenv import load_dotenv")
print("     load_dotenv()  # Load .env file")
print("     api_key = os.getenv('API_KEY')")
print()

# JSON CONFIGURATION
# JSON files for configuration

json_config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "mydb"
    },
    "api": {
        "base_url": "https://api.example.com",
        "timeout": 30
    },
    "logging": {
        "level": "INFO"
    }
}

# Write JSON config
with open("config.json", "w") as f:
    json.dump(json_config, f, indent=2)

# Read JSON config
with open("config.json", "r") as f:
    loaded_config = json.load(f)

print("5. JSON Configuration:")
print(f"   Database host: {loaded_config['database']['host']}\n")

# CONFIGURATION CLASS PATTERN
# Object-oriented configuration

class Config:
    """Configuration class."""
    
    def __init__(self):
        self.database_host = os.getenv("DB_HOST", "localhost")
        self.database_port = int(os.getenv("DB_PORT", "5432"))
        self.api_key = os.getenv("API_KEY", "")
        self.debug = os.getenv("DEBUG", "false").lower() == "true"
    
    @classmethod
    def from_file(cls, filepath):
        """Load config from JSON file."""
        with open(filepath, "r") as f:
            data = json.load(f)
        
        config = cls()
        if "database" in data:
            config.database_host = data["database"].get("host", config.database_host)
            config.database_port = data["database"].get("port", config.database_port)
        
        return config

app_config = Config()
print("6. Configuration Class:")
print(f"   Database: {app_config.database_host}:{app_config.database_port}")
print(f"   Debug mode: {app_config.debug}\n")

# CONFIGURATION WITH DEFAULT VALUES
# Hierarchical configuration loading

def load_config():
    """Load configuration with defaults and overrides."""
    defaults = {
        "host": "localhost",
        "port": 8080,
        "debug": False
    }
    
    # Load from file if exists
    if os.path.exists("config.json"):
        with open("config.json", "r") as f:
            file_config = json.load(f)
            defaults.update(file_config)
    
    # Override with environment variables
    defaults["host"] = os.getenv("HOST", defaults["host"])
    defaults["port"] = int(os.getenv("PORT", defaults["port"]))
    defaults["debug"] = os.getenv("DEBUG", str(defaults["debug"])).lower() == "true"
    
    return defaults

config = load_config()
print("7. Hierarchical Configuration:")
print(f"   Config: {config}\n")

# VALIDATION
# Validate configuration values

def validate_config(config_dict):
    """Validate configuration."""
    errors = []
    
    if "host" not in config_dict:
        errors.append("Missing 'host'")
    
    if "port" in config_dict:
        port = config_dict["port"]
        if not isinstance(port, int) or not (1 <= port <= 65535):
            errors.append(f"Invalid port: {port}")
    
    if errors:
        raise ValueError(f"Configuration errors: {', '.join(errors)}")
    
    return True

print("8. Configuration Validation:")
valid_config = {"host": "localhost", "port": 8080}
try:
    validate_config(valid_config)
    print("   Configuration is valid\n")
except ValueError as e:
    print(f"   {e}\n")

# SECRETS MANAGEMENT
# Handle sensitive configuration

print("9. Secrets Management:")
print("   ✓ Never commit secrets to git")
print("   ✓ Use environment variables")
print("   ✓ Use secret management services")
print("   ✓ Use .env files (gitignored)")
print("   ✓ Use separate config files per environment")
print()

# ENVIRONMENT-SPECIFIC CONFIG
# Different configs for dev/staging/prod

def get_environment_config():
    """Get config based on environment."""
    env = os.getenv("ENVIRONMENT", "development")
    
    configs = {
        "development": {
            "debug": True,
            "log_level": "DEBUG"
        },
        "staging": {
            "debug": False,
            "log_level": "INFO"
        },
        "production": {
            "debug": False,
            "log_level": "WARNING"
        }
    }
    
    return configs.get(env, configs["development"])

env_config = get_environment_config()
print("10. Environment-Specific Config:")
print(f"   Environment: {os.getenv('ENVIRONMENT', 'development')}")
print(f"   Config: {env_config}\n")

# CONFIGURATION PATTERNS
print("11. Configuration Patterns:")

# Singleton pattern for config
class AppConfig:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._load()
        return cls._instance
    
    def _load(self):
        """Load configuration."""
        self.settings = load_config()

# Use singleton
config1 = AppConfig()
config2 = AppConfig()
print(f"   Singleton pattern: {config1 is config2}\n")

# BEST PRACTICES
print("12. Best Practices:")
print("    ✓ Use environment variables for secrets")
print("    ✓ Provide sensible defaults")
print("    ✓ Validate configuration")
print("    ✓ Support multiple config sources")
print("    ✓ Use configuration classes for type safety")
print("    ✓ Separate dev/staging/prod configs")
print("    ✓ Document configuration options")
print("    ✓ Never hardcode secrets")
print()

# CLEANUP
import os
for file in ["config.ini", "config.json"]:
    if os.path.exists(file):
        os.remove(file)

print("Configuration management demonstration complete!")
print("\nConfiguration sources (priority order):")
print("  1. Environment variables (highest)")
print("  2. Configuration files")
print("  3. Default values (lowest)")

