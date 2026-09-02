import random

from fastmcp import FastMCP

mcp = FastMCP(name="Demo Server")

@mcp.tool
def roll_dice(roll_dice: int = 1) -> list[int]:
    """Rolls a dice with the specified number of sides."""
    return [random.randint(1, 6) for _ in range(roll_dice)]

@mcp.tool
def add_numbers(a: int, b: int) -> int:
    """Adds two numbers together."""
    return a + b

@mcp.tool
def multiply_numbers(a: int, b: int) -> int:
    """Multiplies two numbers together."""
    return a * b

@mcp.tool
def subtract_numbers(a: int, b: int) ->int:
    """Subtracts the second number from the first."""
    return a - b 

@mcp.tool
def divide_numbers(a: int, b: int) -> float:
    """Divides the first number by the second."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

@mcp.tool
def percentage(a: float, b: float) -> float:
    """Calculates the percentage of a number."""
    if b == 0:
        raise ValueError("Cannot calculate percentage with a denominator of zero.")
    return (a / b) * 100    

@mcp.tool
def square_number(a: int) -> int:
    """Returns the square of a number."""
    return a * a

@mcp.tool
def cube_number(a: int) -> int:
    """Returns the cube of a number."""
    return a * a * a 

@mcp.tool
def power_number(a: int, b: int) -> int:
    """Returns the first number raised to the power of the second number."""
    return a ** b

@mcp.tool
def factorial_number(a: int) -> int:
    """Returns the factorial of a number."""
    if a < 0:
        raise ValueError("Cannot compute factorial of a negative number.")
    if a == 0 or a == 1:
        return 1
    result = 1
    for i in range(2, a + 1):
        result *= i
    return result

@mcp.tool
def even_or_odd(a: int) -> str:
    """Checks if a number is even or odd."""
    return "Even" if a % 2 == 0 else "Odd"

@mcp.tool
def is_prime_number(n: int) -> bool:
    """Checks if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    mcp.run()