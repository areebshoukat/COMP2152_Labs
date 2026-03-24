# Week 13 Lab: Data Analysis for Security

## What Are We Building?

Security teams don't just find vulnerabilities — they need to **analyze** patterns in their findings. Which subdomains have the most issues? What severity level dominates? Are there trends? Today you'll use Python's built-in `csv` module to import scan data and generate useful reports.

Open the starter files and look for the **`# TODO`** markers.

---

## Q1: Import and Analyze Scan Results

**File:** `lab13_q1_starter.py`

Your team has been scanning `0x10.cloud` for weeks and has a CSV file of all findings. You'll write functions to load that data, filter it, and answer questions about it.

The starter creates a sample CSV file and has the main section. **Your work is four functions.**

**`load_findings(filename)`** — read the CSV file:

```
Open the CSV file using csv.DictReader
Return a list of dictionaries (one per row)
```

**`count_by_field(findings, field)`** — count occurrences of a field:

```
Loop through findings, count how many times each unique value of the field appears
Return a dictionary like {"HIGH": 5, "MEDIUM": 3, "LOW": 8}
```

**`filter_findings(findings, field, value)`** — filter by a field value:

```
Use a list comprehension to return only findings where finding[field] == value
```

**`top_subdomains(findings, n)`** — find the most targeted subdomains:

```
Count findings per subdomain
Sort by count (descending)
Return the top n as a list of (subdomain, count) tuples
```

### Test It

Run `python lab13_q1_starter.py`. You should see:

```
============================================================
  Q1: SCAN DATA ANALYSIS
============================================================

--- Loaded 12 findings ---

--- By Severity ---
  HIGH     : 4
  MEDIUM   : 3
  LOW      : 5

--- By Type ---
  default_creds   : 3
  open_port       : 3
  missing_header  : 3
  exposed_file    : 2
  no_https        : 1

--- HIGH Severity Findings ---
  ssh.0x10.cloud    | default_creds  | HIGH
  ftp.0x10.cloud    | default_creds  | HIGH
  db.0x10.cloud     | open_port      | HIGH
  admin.0x10.cloud  | exposed_file   | HIGH

--- Top 3 Subdomains ---
  1. ssh.0x10.cloud     (2)
  2. api.0x10.cloud     (2)
  3. blog.0x10.cloud    (2)

============================================================
```

---

## Q2: ASCII Dashboard

**File:** `lab13_q2_starter.py`

Instead of just printing numbers, you'll create a simple visual dashboard using ASCII characters. This is how many command-line security tools present data.

The starter has the sample data and main section. **Your work is three functions.**

**`bar_chart(data, title, max_width=30)`** — draw a horizontal bar chart:

```
Print the title
Find the maximum value in data (for scaling)
For each (label, count): print a bar using "█" characters
Scale bars so the largest value fills max_width characters
```

**`severity_summary(findings)`** — summarize findings by severity:

```
Count findings per severity (HIGH, MEDIUM, LOW)
Return as a list of (severity, count) tuples, sorted HIGH first
```

**`timeline(findings)`** — show findings over time:

```
Count findings per date (use the "date" field)
Return as a list of (date, count) tuples, sorted by date
```

### Test It

Run `python lab13_q2_starter.py`. You should see:

```
============================================================
  Q2: ASCII DASHBOARD
============================================================

  SEVERITY BREAKDOWN
  HIGH     ████████████████████████████▌  4
  MEDIUM   █████████████████████▍         3
  LOW      ██████████████████████████████ 5

  FINDINGS BY DATE
  2026-03-10 ██████████████████████████████ 5
  2026-03-11 ██████████████████             3
  2026-03-12 ████████████████████████       4

  VULNERABILITY TYPES
  default_creds  ██████████████████████████████ 3
  open_port      ██████████████████████████████ 3
  missing_header ██████████████████████████████ 3
  exposed_file   ████████████████████           2
  no_https       ██████████                     1

============================================================
```

---

## Submission

- Only submit your GitHub repository link (No screenshots, no ZIP or Python files, just the link). For example:
  [https://github.com/sojoudian/COMP2152_Labs](https://github.com/sojoudian/COMP2152_Labs)
- Create a branch named **`lab_week13`**, complete your lab work in that branch, and once finished, merge it into your **`master`** branch.
