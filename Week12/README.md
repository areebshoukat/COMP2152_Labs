# Week 12 Lab: Inheritance, Polymorphism & Special Methods

## What Are We Building?

Last week you built classes. This week you'll learn to make classes **inherit** from each other — so a child class can reuse everything from a parent class and add its own behavior on top. You'll also learn **special methods** (dunder methods) that let your objects work with built-in Python features like `print()`, `len()`, `==`, and `sorted()`.

Open the starter files and look for the **`# TODO`** markers.

---

## Q1: Scanner Inheritance — Parent and Child Classes

**File:** `lab12_q1_starter.py`

In Week 11 you built a `SimpleScanner`. But what if you need different types of scanners — one for checking open ports, another for checking HTTP websites? Instead of writing two completely separate classes, you can create a **parent class** with shared code, then **child classes** that add their own specific behavior.

The starter has the parent class structure and main section. **Your work is completing the parent class and building two child classes.**

**`class Scanner:`** — the parent class (shared by all scanners):

```
__init__(self, target)
    Store self.target and create self.results = []

display_results(self)
    Print "Results for {self.target}:"
    If self.results is empty, print "(no results)"
    Otherwise, print each result
```

**`class PortScanner(Scanner):`** — child class for port scanning:

```
__init__(self, target, ports)
    Call the parent constructor using super().__init__(target)
    Store self.ports (a list of port numbers to scan)

scan(self)
    Loop through self.ports
    For each port, use socket.connect_ex to check if it's open
    If open, append f"Port {port}: OPEN" to self.results
    If closed, append f"Port {port}: closed" to self.results
```

**`class HTTPScanner(Scanner):`** — child class for HTTP checking:

```
__init__(self, target, paths)
    Call the parent constructor using super().__init__(target)
    Store self.paths (a list of URL paths to check, like "/", "/admin", "/.git/config")

scan(self)
    Loop through self.paths
    For each path, use urllib to request http://{self.target}{path}
    If status 200, append f"{path} → {status} (accessible)" to self.results
    If error, append f"{path} → NOT FOUND" to self.results
```

### Reference

```python
# Inheritance — child class gets everything from parent
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "..."

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)         # call parent's __init__
        self.breed = breed
    def speak(self):                   # override parent's method
        return "Woof!"

d = Dog("Rex", "Lab")
print(d.name)      # "Rex" — inherited from Animal
print(d.speak())   # "Woof!" — overridden in Dog
```

### Test It

Run `python lab12_q1_starter.py`. You should see:

```
============================================================
  Q1: SCANNER INHERITANCE
============================================================

--- Port Scanner ---
  Scanning 127.0.0.1 ports...
  Port 22: OPEN
  Port 80: closed
  Port 443: closed
  Results for 127.0.0.1:
    Port 22: OPEN
    Port 80: closed
    Port 443: closed

--- HTTP Scanner ---
  Scanning 127.0.0.1 paths...
  / → 200 (accessible)
  /admin → NOT FOUND
  /.git/config → NOT FOUND
  Results for 127.0.0.1:
    / → 200 (accessible)
    /admin → NOT FOUND
    /.git/config → NOT FOUND

============================================================
```

---

## Q2: Dunder Methods — Making Objects Smarter

**File:** `lab12_q2_starter.py`

Remember the `Finding` class from Week 11? It had `__str__` so you could print it. This week you'll add more **special methods** so your objects can be compared, sorted, counted, and combined — just like built-in Python types.

The starter has the class structure and main section. **Your work is adding 4 dunder methods.**

**`class Finding:`** — enhanced with special methods:

```
__init__(self, subdomain, title, severity)
    Store all three. Also store a severity_rank dictionary:
    {"LOW": 1, "MEDIUM": 2, "HIGH": 3}

__str__(self)
    Return "[{severity}] {subdomain} — {title}"

__eq__(self, other)
    Return True if self.subdomain == other.subdomain and self.title == other.title

__lt__(self, other)
    Compare using severity_rank: self is "less than" other if its severity rank is lower
    This lets sorted() arrange findings from LOW to HIGH
```

**`class Report:`** — enhanced with special methods:

```
__init__(self, team_name)
    Store team_name, create self.findings = []

add(self, finding)
    Append to self.findings

__len__(self)
    Return the number of findings (so len(report) works)

__add__(self, other)
    Create a new Report called "Merged: {self.team_name} + {other.team_name}"
    Combine both reports' findings into the new report
    Return the new report
```

### Reference

```python
# Special methods make your objects work with Python built-ins

class Box:
    def __init__(self, size):
        self.size = size

    def __eq__(self, other):        # ==
        return self.size == other.size

    def __lt__(self, other):        # < (also enables sorted())
        return self.size < other.size

    def __len__(self):              # len()
        return self.size

    def __add__(self, other):       # +
        return Box(self.size + other.size)

a = Box(3)
b = Box(5)
print(a == b)           # False
print(a < b)            # True
print(len(a))           # 3
c = a + b
print(len(c))           # 8
print(sorted([b, a]))   # sorted uses __lt__
```

### Test It

Run `python lab12_q2_starter.py`. You should see:

```
============================================================
  Q2: DUNDER METHODS
============================================================

--- Findings ---
  [HIGH] ssh.0x10.cloud — Default creds
  [LOW] blog.0x10.cloud — No HTTPS
  [MEDIUM] api.0x10.cloud — Version exposed

--- Comparing ---
  f1 == f1_copy: True
  f1 == f2: False

--- Sorting (LOW → HIGH) ---
  [LOW] blog.0x10.cloud — No HTTPS
  [MEDIUM] api.0x10.cloud — Version exposed
  [HIGH] ssh.0x10.cloud — Default creds

--- Report Length ---
  Team Alpha has 2 findings
  Team Beta has 1 findings

--- Merging Reports ---
  Merged: Team Alpha + Team Beta has 3 findings

============================================================
```

---

## Submission

- Only submit your GitHub repository link (No screenshots, no ZIP or Python files, just the link). For example:
  [https://github.com/sojoudian/COMP2152_Labs](https://github.com/sojoudian/COMP2152_Labs)
- Create a branch named **`lab_week12`**, complete your lab work in that branch, and once finished, merge it into your **`master`** branch.
