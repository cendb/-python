# 02. Data Structures

This directory explores Python's built-in collection types and specialized collection containers.

## Included Files

* `01_lists.py` — Ordered, dynamic arrays (`list`) with operations like `.append()`, `.pop()`, and list slicing.
* `02_tuples.py` — Immutable ordered sequences (`tuple`), memory efficiency, and tuple unpacking.
* `03_dictionaries.py` — Fast key-value mappings (`dict`), hash keys, and dict methods (`.get()`, `.items()`).
* `04_sets.py` — Unordered unique collections (`set`, `frozenset`) and set operations (union, intersection, difference).
* `05_arrays.py` — Uniform datatype sequences using the native `array` module and basic NumPy arrays.
* `06_collections_module.py` — Advanced container data types (`deque`, `Counter`, `defaultdict`, `namedtuple`).

## Collection Matrix

| Structure | Syntax | Ordered? | Mutable? | Unique Items Only? |
| :--- | :--- | :--- | :--- | :--- |
| **List** | `[1, 2, 3]` | Yes | Yes | No |
| **Tuple** | `(1, 2, 3)` | Yes | No | No |
| **Dictionary**| `{"a": 1}` | Yes (3.7+) | Yes | Keys: Yes, Values: No |
| **Set** | `{1, 2, 3}` | No | Yes | Yes |
| **Frozenset** | `frozenset([1])`| No | No | Yes |