"""
A tiny math utilities module.

NOTE: `add` and `average` both have bugs, intentionally, for
demoing the autonomous dev agent. Do not fix these by hand --
that's the agent's job.
"""


def add(a, b):
    # Bug: subtracts instead of adding
    return a - b


def average(numbers):
    # Bug: off-by-one -- divides by len(numbers) - 1 instead of len(numbers)
    return sum(numbers) / (len(numbers) - 1)
