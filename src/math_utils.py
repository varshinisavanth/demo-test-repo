
"""
A tiny math utilities module.
"""

def add(a, b):
    # Fixed bug: now adds instead of subtracting
    return a + b

def average(numbers):
    # Fixed bug: now divides by the correct length
    return sum(numbers) / len(numbers)