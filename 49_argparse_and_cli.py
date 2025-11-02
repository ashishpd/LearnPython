"""
49_argparse_and_cli.py

This file demonstrates command-line interface (CLI) creation in Python.
Covers argparse (built-in) and click (popular third-party library).
"""

import argparse
import sys

print("COMMAND-LINE INTERFACES IN PYTHON")
print("=" * 50)

# ARGPARSE - BASIC USAGE
# Python's built-in argument parser

print("1. Basic argparse:")

parser = argparse.ArgumentParser(description="Example CLI application")
parser.add_argument("name", help="Name of the user")
parser.add_argument("--age", type=int, help="Age of the user")

# Parse arguments
# args = parser.parse_args(["Alice", "--age", "30"])
# print(f"   Name: {args.name}, Age: {args.age}\n")

print("   Usage: python script.py NAME [--age AGE]")
print()

# POSITIONAL AND OPTIONAL ARGUMENTS
print("2. Positional vs Optional Arguments:")

parser = argparse.ArgumentParser()
parser.add_argument("input_file", help="Input file path")
parser.add_argument("--output", "-o", help="Output file path")
parser.add_argument("--verbose", "-v", action="store_true", help="Verbose mode")

# args = parser.parse_args(["file.txt", "--output", "out.txt", "--verbose"])
print("   Positional: input_file (required)")
print("   Optional: --output/-o, --verbose/-v")
print()

# ARGUMENT TYPES
print("3. Argument Types:")

parser = argparse.ArgumentParser()
parser.add_argument("--count", type=int, help="Integer argument")
parser.add_argument("--price", type=float, help="Float argument")
parser.add_argument("--name", type=str, help="String argument")

print("   Types: int, float, str (default)\n")

# CHOICES
print("4. Choices:")

parser = argparse.ArgumentParser()
parser.add_argument(
    "--mode",
    choices=["read", "write", "append"],
    help="File mode"
)

print("   Restricts values to specified choices\n")

# BOOLEAN FLAGS
print("5. Boolean Flags:")

parser = argparse.ArgumentParser()
parser.add_argument("--verbose", action="store_true", help="Enable verbose")
parser.add_argument("--quiet", action="store_false", dest="verbose", help="Disable verbose")
parser.add_argument("--flag", action="store_true", default=False)

print("   store_true: Flag set to True when present")
print("   store_false: Flag set to False when present\n")

# COUNTING FLAGS
print("6. Counting Flags:")

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", action="count", default=0, help="Verbosity level")

print("   -v = 1, -vv = 2, -vvv = 3\n")

# NARGS (NUMBER OF ARGUMENTS)
print("7. Number of Arguments (nargs):")

parser = argparse.ArgumentParser()
parser.add_argument("files", nargs="+", help="One or more files")
parser.add_argument("--tags", nargs="*", help="Zero or more tags")
parser.add_argument("--pair", nargs=2, help="Exactly 2 values")

print("   nargs='+' - One or more")
print("   nargs='*' - Zero or more")
print("   nargs=2 - Exactly 2\n")

# DEFAULT VALUES
print("8. Default Values:")

parser = argparse.ArgumentParser()
parser.add_argument("--host", default="localhost", help="Host address")
parser.add_argument("--port", type=int, default=8080, help="Port number")

print("   Default values used when argument not provided\n")

# SUBCOMMANDS
print("9. Subcommands:")

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command", help="Available commands")

# Create subcommand
parser_list = subparsers.add_parser("list", help="List items")
parser_list.add_argument("--all", action="store_true")

parser_add = subparsers.add_parser("add", help="Add item")
parser_add.add_argument("name", help="Item name")

print("   python script.py COMMAND [args]")
print("   Commands: list, add\n")

# COMPLETE EXAMPLE
print("10. Complete argparse Example:")

def create_example_cli():
    """Complete CLI example."""
    parser = argparse.ArgumentParser(
        prog="example",
        description="Example CLI application",
        epilog="For more info, see README.md"
    )
    
    parser.add_argument("input", help="Input file")
    parser.add_argument("-o", "--output", help="Output file")
    parser.add_argument("-v", "--verbose", action="count", default=0)
    parser.add_argument("--format", choices=["json", "xml"], default="json")
    
    return parser

example_parser = create_example_cli()
print("   Example parser created")
print("   Try: python script.py input.txt -o output.txt -vv --format json\n")

# CLICK LIBRARY (Third-party)
# More elegant CLI library

click_info = """
11. Click Library (Third-party):
    Install: pip install click
    
    import click
    
    @click.command()
    @click.argument('name')
    @click.option('--age', type=int, default=0)
    @click.option('--verbose', is_flag=True)
    def main(name, age, verbose):
        if verbose:
            click.echo(f"Hello {name}, age {age}")
        else:
            click.echo(f"Hello {name}")
    
    if __name__ == '__main__':
        main()
    
    Benefits:
    - Decorator-based (cleaner)
    - Automatic help generation
    - Type conversion
    - Nested commands
    - Color support
"""

print(click_info)

# BEST PRACTICES
print("12. CLI Best Practices:")
print("    ✓ Provide clear descriptions")
print("    ✓ Use meaningful argument names")
print("    ✓ Set appropriate defaults")
print("    ✓ Validate input")
print("    ✓ Provide helpful error messages")
print("    ✓ Support --help flag")
print("    ✓ Use subcommands for complex CLIs")
print()

# ERROR HANDLING
print("13. Error Handling:")

def safe_parse_args(parser):
    """Parse args with error handling."""
    try:
        return parser.parse_args()
    except SystemExit:
        # argparse calls sys.exit() on error
        print("   Error parsing arguments")
        sys.exit(1)

print("   Handle parsing errors gracefully\n")

# ARGUMENT GROUPS
print("14. Argument Groups:")

parser = argparse.ArgumentParser()
input_group = parser.add_argument_group("input options")
output_group = parser.add_argument_group("output options")

input_group.add_argument("--input-file", help="Input file")
output_group.add_argument("--output-file", help="Output file")

print("   Groups organize related arguments\n")

print("CLI demonstration complete!")
print("\nComparison:")
print("  argparse - Built-in, standard, verbose")
print("  click - Third-party, elegant, feature-rich")
print("\nFor simple CLIs: argparse")
print("For complex CLIs: consider click")

