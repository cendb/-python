# 04. Functions & Functional Concepts

This directory covers reusable code blocks, parameter passing, scope, and functional programming features.

## Included Files

* `01_basics.py` — Declaring functions with `def`, return values, default parameters, type hinting, and docstrings.
* `02_args_kwargs.py` — Flexible function arguments with positional `*args` (tuples) and keyword `**kwargs` (dicts).
* `03_lambda.py` — One-line anonymous functions (`lambda`) paired with higher-order functions like `map()`, `filter()`, and `sorted()`.
* `04_comprehensions.py` — Concise inline syntax for generating lists, dictionaries, and sets.

## Essential Syntax Cheatsheet

```python
# Function with flexible parameters
def process_data(*args, **kwargs):
    pass

# Lambda expression
double = lambda x: x * 2

# List comprehension
evens = [x for x in range(20) if x % 2 == 0]

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}