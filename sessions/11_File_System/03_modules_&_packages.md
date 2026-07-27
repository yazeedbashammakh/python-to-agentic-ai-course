# Modules & Packages

## Why are We Learning Modules?

So far, every program we've written has been inside **one Python file**.

That works well for small programs.

But imagine building a **Library Management System** or our **Book Store Management System** in a single file.

Finding and updating code would quickly become difficult.

Instead of putting everything into one file, Python allows us to split our program into multiple files and folders.

This keeps our projects:

- Organized
- Easier to read
- Easier to maintain
- Easier to reuse

---

# What is a Module?

A **module** is simply a Python file.

For example:

```text
calculator.py
```

Everything inside `calculator.py` belongs to that module.

---

## Example

### calculator.py

```python
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b
```

### main.py

```python
import calculator

print(calculator.add(10, 5))
print(calculator.subtract(20, 8))
```

Instead of writing the same functions again, we simply **import** them.

> **Write once. Reuse anywhere.**

---

# Different Ways to Import

Python provides several ways to import modules.

## 1. Normal Import

```python
import math

print(math.sqrt(25))
```

Use this when you'll need multiple functions from the module.

---

## 2. Import with an Alias

```python
import math as m

print(m.sqrt(25))
```

Aliases make long module names shorter and easier to type.

---

## 3. Import a Specific Function

```python
from math import sqrt

print(sqrt(25))
```

This is one of the most common ways to import a function.

---

## 4. Import Everything (Not Recommended)

```python
from math import *
```

Although this works, it is discouraged because it imports everything into your program, making the code harder to understand.

---

# Every Python File is a Module

Suppose we have this project:

```text
project/
│
├── calculator.py
└── main.py
```

**calculator.py**

```python
def multiply(a, b):
    return a * b
```

**main.py**

```python
from calculator import multiply

print(multiply(6, 7))
```

The function is written once and can now be used anywhere in the project.

---

# What is a Package?

A **package** is simply a folder that contains related Python modules.

Example:

```text
lms/
│
├── __init__.py
├── students.py
├── marks.py
├── attendance.py
├── fees.py
└── main.py
```

Instead of putting every feature into one file, we group related files together.

---

# Why Use Packages?

Imagine building a Student Management System.

Instead of writing everything inside `main.py`, we separate the project into smaller modules.

- `students.py` → Student operations
- `marks.py` → Marks management
- `attendance.py` → Attendance management
- `fees.py` → Fee management

This makes the project much easier to manage as it grows.

---

# What is `__init__.py`?

`__init__.py` tells Python that a folder should behave like a package.

```text
lms/
│
└── __init__.py
```

In modern versions of Python, this file is optional, but you'll still see it in many real-world projects.

---

# Built-in Modules

Python already comes with many useful modules.

| Module | Used For |
|---------|----------|
| `math` | Mathematical calculations |
| `os` | Working with files and folders |
| `sys` | Accessing Python system information |

Example:

```python
import math

print(math.pi)
```

---

# Third-Party Packages

Not every module is built into Python.

Thousands of developers share their own packages on the **Python Package Index (PyPI)**.

Some popular examples are:

- pandas
- numpy
- requests
- flask

We can install them whenever we need them.

---

# What is pip?

`pip` is Python's default package manager.

It helps us install, update, and remove third-party packages.

### Install a Package

```bash
pip install requests
```

### Uninstall a Package

```bash
pip uninstall requests
```

### View Installed Packages

```bash
pip list
```

### Show Package Information

```bash
pip show requests
```

---

# Local Packages

We can also create our own packages.

For example, our Book Store Management System is organized like this:

```text
book_store/
│
├── models/
├── services/
├── utils/
└── main.py
```

Each folder has a specific responsibility, making the project cleaner and easier to maintain.

---

# Running vs Importing a File

A Python file can be used in two different ways.

### Option 1: Import the File

```python
from calculator import add
```

The file becomes part of another program.

---

### Option 2: Run the File

```bash
python calculator.py
```

Python starts executing that file directly.

---

# The `__name__` Variable

Every Python file automatically gets a special variable called `__name__`.

If you run the file directly:

```python
print(__name__)
```

Output:

```text
__main__
```

If the same file is imported into another program:

```text
calculator
```

---

# Why Do We Write This?

```python
if __name__ == "__main__":
    print("Running directly")
```

This code runs **only** when the file is executed directly.

If the file is imported into another program, Python skips this block.

---

# Virtual Environment

A virtual environment creates an isolated workspace for a project.

This allows different projects to use different package versions without affecting each other.

---

## Create a Virtual Environment

```bash
python -m venv myenv
```

---

## Activate the Environment

### Windows (Command Prompt)

```bash
myenv\Scripts\activate.bat
```

### Windows (PowerShell)

```bash
.\myenv\Scripts\Activate.ps1
```

### Windows (Git Bash)

```bash
source myenv/Scripts/activate
```

### macOS / Linux

```bash
source myenv/bin/activate
```

---

## Deactivate the Environment

```bash
deactivate
```