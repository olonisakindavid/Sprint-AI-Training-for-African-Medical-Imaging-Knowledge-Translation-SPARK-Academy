# Factorial of a Number (Recursion)
# Filename: factorial.py
# Write a recursive function `factorial(n)` to compute the factorial of a given number n.

def factorial(n):
    # Handle negative inputs
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    
    # Recursive case: n! = n * (n-1)!
    return n * factorial(n - 1)