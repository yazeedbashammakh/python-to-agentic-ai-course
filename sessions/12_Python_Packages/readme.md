# Session 12: Modules, Packages, pip and Virtual Environments

# Why Do We Need Modules?

Imagine building a Student Management System.

Initially, everything is written in a single file:

```text
main.py

Student Registration
Student Login
Attendance
Marks
Fees
Reports
```

As the application grows, the file becomes difficult to manage.

Instead, we divide our application into multiple files, where each file has a specific responsibility.

This makes the code:

* Easier to read
* Easier to maintain
* Easier to reuse
* Easier to test
* Easier for teams to collaborate

---

# What is a Module?

A **module** is simply a Python file (`.py`) containing Python code.

Example:

```text
marks.py
```

```python
def calculate_percentage(total, maximum):
    return (total / maximum) * 100
```

Now it can be used in another file.

```python
import marks

percentage = marks.calculate_percentage(450, 500)
```

Every Python file is a module.

---

# Types of Imports

## Normal Import

```python
import math

print(math.sqrt(25))
```

---

## Import with Alias

Useful when the module name is long.

```python
import math as m

print(m.sqrt(25))
```

---

## Import Specific Functions (Recommended)

Imports only the required function.

```python
from math import sqrt

print(sqrt(25))
```

---

## Import Everything (Discouraged)

```python
from math import *
```

This is discouraged because:

* It pollutes the namespace.
* It becomes difficult to know where functions come from.
* It may overwrite existing names.
* It reduces code readability.

---

# Built-in Modules

Python already includes many useful modules.

Some common examples are:

| Module        | Purpose                        |
| ------------- | ------------------------------ |
| `math`        | Mathematical operations        |
| `os`          | Operating system interactions  |
| `sys`         | Python interpreter information |
| `json`        | Read and write JSON            |
| `random`      | Generate random values         |
| `datetime`    | Work with dates and times      |
| `collections` | Specialized data structures    |

These modules are available immediately—no installation is required.

Example:

```python
import math

print(math.pi)
```

---

# Third-Party Packages

Python also has thousands of community-created packages.

Examples:

* requests
* numpy
* pandas
* fastapi
* google-genai
* google-adk

These packages are **not** included with Python and must be installed separately.

---

# PyPI (Python Package Index)

The official repository for Python packages is called **PyPI (Python Package Index)**.

It contains hundreds of thousands of open-source packages created by the Python community.

Website:

https://pypi.org

Whenever you run:

```bash
pip install requests
```

`pip` downloads the package from PyPI.

---

# What is pip?

**pip** is Python's default package manager.

It is used to:

* Install packages
* Upgrade packages
* Remove packages
* View installed packages
* Display package information

---

# Common pip Commands

## Install a package

```bash
pip install requests
```

---

## Install a specific version

```bash
pip install requests==2.32.0
```

---

## Upgrade a package

```bash
pip install --upgrade requests
```

---

## Uninstall a package

```bash
pip uninstall requests
```

---

## List installed packages

```bash
pip list
```

---

## Show package details

```bash
pip show requests
```

---

## Export installed packages

```bash
pip freeze
```

Commonly used to create a `requirements.txt` file.

```bash
pip freeze > requirements.txt
```

---

## Install all packages from requirements.txt

```bash
pip install -r requirements.txt
```

---

# Local Modules

You can also create your own modules.

Example:

```text
calculator.py
```

```python
def add(a, b):
    return a + b
```

Use it in another file.

```python
import calculator

print(calculator.add(5, 3))
```

---

# Local Packages

A package is a folder that contains related modules.

Example:

```text
lms/
│
├── __init__.py
├── students.py
├── marks.py
├── attendance.py
└── fees.py

main.py
```

This keeps projects organized and easier to manage.

---

# What is `__init__.py`?

Traditionally, the `__init__.py` file tells Python that a directory should be treated as a package.

In modern Python (3.3+), packages can often work without this file because of namespace packages.

However, it is still commonly included because it:

* Clearly identifies a package.
* Can run initialization code.
* Can expose selected modules and functions.

For most Python projects, including an empty `__init__.py` file is still considered good practice.

---

# Project Structure Example

```text
student_management/

│
├── main.py
│
├── lms/
│   ├── __init__.py
│   ├── students.py
│   ├── attendance.py
│   ├── marks.py
│   └── fees.py
│
└── requirements.txt
```

---

# Understanding `__name__`

Every Python file contains a special variable called `__name__`.

There are two ways a Python file can be used.

## Case 1 — Executed Directly

```bash
python marks.py
```

Here,

```python
__name__ == "__main__"
```

---

## Case 2 — Imported by Another File

```python
import marks
```

Here,

```python
__name__ == "marks"
```

---

# Why Use `if __name__ == "__main__"`?

It allows you to execute code only when the file is run directly.

Example:

```python
def calculate_percentage(total, maximum):
    return (total / maximum) * 100

if __name__ == "__main__":
    print(calculate_percentage(450, 500))
```

Now:

* Running `marks.py` executes the test code.
* Importing `marks.py` only imports the function without executing the test code.

This is a common best practice for reusable modules.

---

# Virtual Environments

Every Python project may require different package versions.

Instead of installing everything globally, we create an isolated environment for each project.

Benefits:

* Prevents dependency conflicts.
* Keeps projects independent.
* Makes collaboration easier.
* Ensures reproducible environments.

---

# Global Environment

Packages installed globally are available to every Python project.

This can lead to version conflicts between projects.

---

# Virtual Environment

Each project gets its own isolated Python installation and package directory.

Example:

```text
student_management/

├── myenv/
├── main.py
└── requirements.txt
```

---

# Create a Virtual Environment

```bash
python -m venv myenv
```

---

# Activate the Virtual Environment

## macOS / Linux

```bash
source myenv/bin/activate
```

---

## Windows (Command Prompt)

```bash
myenv\Scripts\activate.bat
```

---

## Windows (PowerShell)

```powershell
.\myenv\Scripts\Activate.ps1
```

---

## Windows (Git Bash)

```bash
source myenv/Scripts/activate
```

---

# Deactivate the Environment

```bash
deactivate
```

