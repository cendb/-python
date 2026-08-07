# 05. Modules & Packages

Understand Python's modular organization system, import mechanisms, and standard library tools.

## Included Files

* `01_standard_lib.py` — Exploring built-in utility modules (`math`, `random`, `datetime`, `os`, `sys`, `pathlib`).
* `02_custom_imports/` — Structuring multi-file Python applications.
  * `main.py` — Main entry point executing imported logic.
  * `helpers.py` — Helper utility module containing exportable functions.

## Key Architectural Concepts

* **Module**: Any standard `.py` file containing executable code or function definitions.
* **Package**: A folder containing one or more modules.
* **`if __name__ == "__main__":`**: Guard statement that ensures a script only runs when executed directly, not when imported as a module.