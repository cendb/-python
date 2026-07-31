# 03. Control Flow & Error Handling

Learn how to manage application execution order using branch logic, loops, and exception handling.

## Included Files

* `01_if_else.py` — Conditional execution using `if`, `elif`, `else`, and inline ternary expressions (`x if cond else y`).
* `02_match_case.py` — Structural pattern matching introduced in Python 3.10+.
* `03_for_loops.py` — Iterating through sequences, using `range()`, unpacking with `enumerate()`, and combining loops with `zip()`.
* `04_while_loops.py` — Condition-based iteration, controlling flow with `break` and `continue`, and utilizing loop `else` clauses.
* `05_try_except.py` — Exception handling (`try`, `except`, `else`, `finally`) and raising custom exceptions.

## Loop `else` Clause Tip

In Python, loops (`for` and `while`) can have an `else` block. It only executes if the loop finishes without encountering a `break` statement.

```python
for item in items:
    if item == target:
        print("Found!")
        break
else:
    print("Target not found in list.")