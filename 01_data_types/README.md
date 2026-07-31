# 01. Built-in Data Types

This module focuses on Python's fundamental primitive types, immutability, and basic operations.

## Included Files

* `01_numeric.py` — Integers (`int`), Floating-point (`float`), and Complex (`complex`) numbers.
* `02_strings.py` — String manipulation, methods (`.split()`, `.join()`, `.strip()`), slicing `[start:stop:step]`, and f-strings.
* `03_booleans.py` — Logical values (`True`/`False`), comparison operators, and evaluating Truthy/Falsy states.
* `04_binary.py` — Low-level data structures: `bytes`, `bytearray`, and zero-copy `memoryview`.

## Quick Reference: Primitive Types

| Type | Example | Mutable? | Key Feature |
| :--- | :--- | :--- | :--- |
| **`int`** | `42` | No | Arbitrary precision whole numbers |
| **`float`** | `3.14159` | No | Double-precision floating point |
| **`complex`** | `2 + 3j` | No | Real and imaginary units |
| **`str`** | `"Hello"` | No | Immutable sequence of Unicode characters |
| **`bool`** | `True` | No | Subtype of integer (`1` or `0`) |
| **`bytes`** | `b'data'` | No | Immutable sequence of bytes |
| **`bytearray`**| `bytearray(5)`| Yes | Mutable sequence of bytes |