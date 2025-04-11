import math

def calculate_factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    # If n is 0, return 1
    if n == 0:
        return 1
    
    # Use an iterative approach to calculate the factorial
    result = 1
    for i in range(1, n + 1):
        result *= i

# Example usage
n = int(input("Enter a number: "))
try:
    calculate_factorial(n)
except ValueError as e:
    print(e)
