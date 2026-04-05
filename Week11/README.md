# Week 11 Lab: Introduction to OOP (Object-Oriented Programming)

## What Are We Building?

Last week you wrote functions. This week you'll learn to organize code into **classes** — the building blocks of Object-Oriented Programming. You'll take things you already know (port scanning from Assignment 2, password checking, vulnerability reporting) and rebuild them as classes.

A class is like a blueprint. An object is a thing built from that blueprint. That's it.

Open the starter files and look for the **`# TODO`** markers.

---

## Q1: Port Scanner Class

**File:** `lab11_q1_starter.py`

In Assignment 2, you wrote a port scanner using functions. Now you'll wrap that same logic into a **class**. The scanning code doesn't change — you're just organizing it differently.

Why? Because with a class, you can create multiple scanners, each with their own target and results, without any variables getting mixed up.

The starter already has the main section that creates objects and calls methods. **Your work is building the class.**

**`class SimpleScanner:`** — a basic port scanner class:

```
__init__(self, target)
    Store target as self.target
    Create an empty list self.open_ports

scan_port(self, port)
    Use socket to check if the port is open (same code as A2)
    If open, append the port to self.open_ports
    Return True if open, False if closed

scan_range(self, start_port, end_port)
    Loop through the range and call self.scan_port() for each port

display_results(self)
    Print the target name
    Print each open port, or "No open ports found" if the list is empty
```

### Reference

```python
# This is what you already know (procedural):
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(1)
result = sock.connect_ex(("127.0.0.1", 80))
sock.close()

# The ONLY new thing is putting it inside a class:
class MyClass:
    def __init__(self, some_value):    # constructor — runs when you create an object
        self.some_value = some_value   # self. stores data IN the object

    def my_method(self):               # a method — a function that belongs to the class
        print(self.some_value)         # self. accesses data FROM the object

# Creating an object:
obj = MyClass("hello")
obj.my_method()                        # prints "hello"
```

### Test It

Run `python lab11_q1_starter.py`. You should see:

```
============================================================
  Q1: PORT SCANNER CLASS
============================================================

--- Scanner 1: localhost ---
  Scanning 127.0.0.1 ports 78-82...
  Port 80: OPEN
  Results for 127.0.0.1:
    Port 80

--- Scanner 2: different target ---
  Scanning 127.0.0.1 ports 20-25...
  Results for 127.0.0.1:
    No open ports found.

============================================================
```

---

## Q2: Password Strength Checker Class

**File:** `lab11_q2_starter.py`

For the term project, your team will be looking for weak passwords and default credentials on `0x10.cloud`. But how do you know if a password is weak? You'll build a class that checks password strength.

The starter already has the main section and test passwords. **Your work is building the class.**

**`class PasswordChecker:`** — checks if passwords are strong or weak:

```
__init__(self)
    Create a list self.common_passwords with these values:
        "admin", "password", "123456", "root", "guest", "letmein", "welcome"
    Create an empty list self.history to track checked passwords

check_common(self, password)
    Return True if the password is in self.common_passwords (case-insensitive)
    Hint: compare password.lower() against the list

check_strength(self, password)
    Check three things:
        has_length = len(password) >= 8
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in "!@#$%^&*" for c in password)
    Return a dictionary: {"length": has_length, "digit": has_digit, "special": has_special}

evaluate(self, password)
    Call check_common — if True, return "WEAK (common password)"
    Call check_strength — count how many checks are True:
        0 or 1 = return "WEAK"
        2 = return "MEDIUM"
        3 = return "STRONG"
    Append a tuple (password, result) to self.history
    Return the result string
```

### Reference

```python
# any() checks if at least one item in a sequence is True
any(c.isdigit() for c in "hello123")    # True — there are digits
any(c.isdigit() for c in "hello")       # False — no digits

# Checking characters
"a".isdigit()     # False
"5".isdigit()     # True
"!" in "!@#$%"    # True

# Counting True values in a list
checks = [True, False, True]
sum(checks)       # 2 (True counts as 1, False as 0)
```

### Test It

Run `python lab11_q2_starter.py`. You should see:

```
============================================================
  Q2: PASSWORD STRENGTH CHECKER
============================================================

--- Checking Passwords ---
  admin           → WEAK (common password)
  hello           → WEAK
  hello123        → MEDIUM
  MyP@ss99        → STRONG
  p@ssw0rd!       → STRONG
  root            → WEAK (common password)

--- Check History ---
  admin           : WEAK (common password)
  hello           : WEAK
  hello123        : MEDIUM
  MyP@ss99        : STRONG
  p@ssw0rd!       : STRONG
  root            : WEAK (common password)

============================================================
```

---

## Q3: Vulnerability Report Class

**File:** `lab11_q3_starter.py`

For the term project, each team member will find a vulnerability and write a report. You'll build a class that represents a single vulnerability finding, and a class that collects multiple findings into a report.

The starter already has the main section. **Your work is building two classes.**

**`class Finding:`** — represents one vulnerability:

```
__init__(self, subdomain, title, severity, description)
    Store all four values as self.subdomain, self.title, self.severity, self.description

__str__(self)
    Return a formatted string:
    "[SEVERITY] subdomain — title"
    Example: "[HIGH] ssh.0x10.cloud — Default credentials admin:admin"
```

**`class Report:`** — collects multiple findings:

```
__init__(self, team_name)
    Store team_name as self.team_name
    Create an empty list self.findings

add_finding(self, finding)
    Append the finding to self.findings

get_by_severity(self, severity)
    Return a list of only the findings that match the given severity
    Hint: use a list comprehension — [f for f in self.findings if ...]

summary(self)
    Print the team name
    Print the total number of findings
    Print the count for each severity level (HIGH, MEDIUM, LOW)
    Print each finding using its __str__ method
```

### Reference

```python
# The __str__ method controls what print() shows
class Dog:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Dog named {self.name}"

d = Dog("Rex")
print(d)           # "Dog named Rex"  — Python calls __str__ automatically

# List comprehension to filter
numbers = [1, 2, 3, 4, 5]
evens = [n for n in numbers if n % 2 == 0]   # [2, 4]
```

### Test It

Run `python lab11_q3_starter.py`. You should see:

```
============================================================
  Q3: VULNERABILITY REPORT
============================================================

--- Adding Findings ---
  Added: [HIGH] ssh.0x10.cloud — Default credentials admin:admin
  Added: [LOW] blog.0x10.cloud — No HTTPS (cleartext)
  Added: [HIGH] ftp.0x10.cloud — Anonymous FTP access
  Added: [MEDIUM] api.0x10.cloud — Server version exposed in headers
  Added: [LOW] cdn.0x10.cloud — Missing security headers

--- Full Report ---
  Team: CyberHunters
  Total findings: 5
  HIGH:   2
  MEDIUM: 1
  LOW:    2
  ----------------------------------------
  [HIGH] ssh.0x10.cloud — Default credentials admin:admin
  [LOW] blog.0x10.cloud — No HTTPS (cleartext)
  [HIGH] ftp.0x10.cloud — Anonymous FTP access
  [MEDIUM] api.0x10.cloud — Server version exposed in headers
  [LOW] cdn.0x10.cloud — Missing security headers

--- HIGH Severity Only ---
  [HIGH] ssh.0x10.cloud — Default credentials admin:admin
  [HIGH] ftp.0x10.cloud — Anonymous FTP access

============================================================
```

---

## Submission

- Only submit your GitHub repository link (No screenshots, no ZIP or Python files, just the link). For example:
  [https://github.com/sojoudian/COMP2152_Labs](https://github.com/sojoudian/COMP2152_Labs)
- Create a branch named **`lab_week11`**, complete your lab work in that branch, and once finished, merge it into your **`master`** branch.
