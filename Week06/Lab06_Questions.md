# Week 06 Lab: Network Diagnostic Logger

## What Are We Building?

Today we're building a **Network Diagnostic Logger** — a real tool that pings servers, looks up DNS records, reads your MAC address, and scans devices on your local network. Every result gets saved to log files so you can track your network activity over time.

This is the kind of tool that sysadmins and network engineers actually use. You're going to write the part that handles saving and reading data from files.

Open **`lab06_starter.py`** and follow along.

---

## Before You Start

Take a minute to scroll through the starter code. Notice the 6 sections (A through F). Sections A, B, and F are already written — they handle running commands, parsing output, and the menu system. **Your work is in Sections C, D, and E** — the file I/O.

---

## Task 1: Save and Read Text Logs

**Where:** Section C — `write_to_log()` and `read_log()` (look for `*** TASK 1 ***`)

When we ping a server, we want to save the full output to a text file — with a timestamp, so we know when each test happened. The log file should **grow over time** (every run adds to it, nothing gets erased).

**`write_to_log(filename, entry)`**
- Open the file in **append mode** (`"a"`) using a `with` statement
- Write the `entry` followed by `"\n"`

**`read_log(filename)`**
- Open the file in **read mode** (`"r"`) using a `with` statement
- Return the full contents with `file.read()`

### Reference

```python
# Append mode — adds to the end, never overwrites
with open("myfile.txt", "a") as file:
    file.write("new line here\n")

# Read mode — reads everything back
with open("myfile.txt", "r") as file:
    content = file.read()
```

### Test It

```python
write_to_log("test_log.txt", "First ping test - Success")
write_to_log("test_log.txt", "Second ping test - Failed")
print(read_log("test_log.txt"))
```

You should see:
```
First ping test - Success
Second ping test - Failed
```

---

## Task 2: Log Results to CSV

**Where:** Section D — `log_to_csv()` and `read_csv_log()` (look for `*** TASK 2 ***`)

Text files are fine for raw output, but for structured data we need CSV. Each row in our CSV log will have 5 columns: **timestamp, command, target, result, status**. This makes it easy to analyze later (how many pings failed? which domains did we look up?).

**`log_to_csv(filename, command, target, result, status)`**
- The timestamp is already created for you on the line above
- Open the file in append mode (`"a"`) with `newline=""`
- Create a `csv.writer(file)`
- Write one row: `[timestamp, command, target, result, status]`

**`read_csv_log(filename)`**
- Open the file in read mode (`"r"`) with `newline=""`
- Create a `csv.reader(file)`
- Loop through the rows and print each one joined by `" | "`

### Reference

```python
import csv

# Writing one CSV row
with open("data.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["value1", "value2", "value3"])

# Reading CSV rows
with open("data.csv", "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(" | ".join(row))
```

### Test It

```python
log_to_csv("test.csv", "ping", "google.com", "12.5", "Success")
log_to_csv("test.csv", "nslookup", "github.com", "140.82.121.4", "Success")
read_csv_log("test.csv")
```

You should see something like:
```
2026-02-17 14:30:45 | ping | google.com | 12.5 | Success
2026-02-17 14:30:45 | nslookup | github.com | 140.82.121.4 | Success
```

---

## Task 3: Handle Missing Files

**Where:** Section E — `safe_read_log()` (look for `*** TASK 3 ***`)

The first time someone runs this program, there's no log file yet. If we try to open a file that doesn't exist, Python crashes with a `FileNotFoundError`. We need to handle that gracefully using `try`/`except`.

**`safe_read_log(filename)`**

- `try:` open the file and read its content
  - If content is empty: print `"Log file is empty."` and return `""`
  - Otherwise: return the content
- `except FileNotFoundError:` print `"No log file found. Run a diagnostic first."` and return `""`
- `finally:` print `"Log read attempt completed."` (this runs no matter what)

### Reference

```python
try:
    with open("file.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    print("This always runs — success or failure.")
```

### Test It

```python
content = safe_read_log("does_not_exist.txt")
```

You should see:
```
No log file found. Run a diagnostic first.
Log read attempt completed.
```

---

## Run the Full Program

Once all 3 tasks are done, go to the bottom of the file and **uncomment `main()`**. Run the program and try these:

1. **Ping** `google.com` — watch it log the result
2. **DNS Lookup** on `github.com` — see the resolved IP
3. **Show Network Info** — find your MAC and IP address
4. **Show ARP Table** — see all devices on your local network
5. **View the log** — see everything you just did, with timestamps
6. **Analyze the log** — get a summary of commands and results
7. **Quit**

Run the program a second time and do a few more diagnostics. Notice how the log file **keeps growing** — that's your append mode at work.

---

## Submit

- Your GitHub repository URL with the completed `lab06_starter.py` and the `diagnostics.csv` file generated by running the program (at least 3 entries)
- Screenshots of the Git branch, add, commit, push, and merge with the master branch, and git log
