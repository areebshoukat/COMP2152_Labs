# Week 14 Lab: Web Requests & HTTP Security

## What Are We Building?

Web applications communicate over HTTP. Every time you visit a website, your browser sends a request and gets back a response with headers, status codes, and content. Security researchers inspect these responses to find misconfigurations. Today you'll use Python's `urllib` and `json` modules to interact with web services and check for security issues.

Open the starter files and look for the **`# TODO`** markers.

---

## Q1: API Explorer — Making HTTP Requests and Parsing JSON

**File:** `lab14_q1_starter.py`

Most modern web applications expose APIs that return data in JSON format. You'll build a tool that makes HTTP requests, reads JSON responses, and extracts information. This is exactly how you'd interact with `api.0x10.cloud` in the term project.

The starter has the main section and a sample API URL. **Your work is three functions.**

**`make_request(url)`** — fetch a URL and return the response:

```
Use urllib.request.urlopen(url)
Read the response body and decode it to a string
Return a dictionary: {"status": response.status, "headers": dict(response.headers), "body": body}
If any error occurs, return {"status": 0, "headers": {}, "body": "", "error": str(e)}
```

**`parse_json(body)`** — parse a JSON string:

```
Use json.loads(body) to convert JSON string to a Python dictionary
If it fails (not valid JSON), return None
```

**`check_api_info(response)`** — extract security-relevant info from the response:

```
Create a findings list
Check if "Server" is in the headers → append "Server version exposed: {value}"
Check if "X-Powered-By" is in the headers → append "Technology exposed: {value}"
Check if "Access-Control-Allow-Origin" header is "*" → append "CORS: open to all origins"
Return the findings list
```

### Reference

```python
import urllib.request
import json

# Make a request
response = urllib.request.urlopen("http://example.com/api")
body = response.read().decode()
status = response.status
headers = dict(response.headers)

# Parse JSON
data = json.loads('{"name": "test", "value": 42}')
print(data["name"])    # "test"
```

### Test It

Run `python lab14_q1_starter.py`. You should see:

```
============================================================
  Q1: API EXPLORER
============================================================

--- Requesting http://httpbin.org/headers ---
  Status: 200
  Server: gunicorn/19.9.0

--- Response Headers ---
  Content-Type    : application/json
  Server          : gunicorn/19.9.0

--- Parsed JSON Body ---
  (parsed JSON content shown here)

--- Security Findings ---
  Server version exposed: gunicorn/19.9.0

============================================================
```

---

## Q2: HTTP Security Header Checker

**File:** `lab14_q2_starter.py`

Every HTTP response includes headers. Some headers are critical for security — when they're missing, the website is vulnerable to attacks like clickjacking, XSS, and data sniffing. You'll build a tool that checks multiple URLs for missing security headers. This is directly useful for the term project — missing security headers is a real vulnerability category on `0x10.cloud`.

The starter has the list of headers to check and the main section. **Your work is two functions.**

**`check_headers(url)`** — check one URL for security headers:

```
Make a request to the URL using urllib
For each required header, check if it exists in the response
Return a list of dictionaries:
  {"header": name, "present": True/False, "value": value or "MISSING"}
```

**`generate_report(url, results)`** — display findings for one URL:

```
Print the URL
For each result:
  If present: print "  ✓ {header}: {value}"
  If missing: print "  ✗ {header}: MISSING — {explanation}"
Print the count of missing headers
```

### Reference

```python
import urllib.request

# Getting headers from a response
response = urllib.request.urlopen("http://example.com")
headers = dict(response.headers)

# Check if a header exists
if "X-Frame-Options" in headers:
    print(f"Found: {headers['X-Frame-Options']}")
else:
    print("Missing!")
```

### Test It

Run `python lab14_q2_starter.py`. You should see something like:

```
============================================================
  Q2: HTTP SECURITY HEADER CHECKER
============================================================

--- Checking http://httpbin.org ---
  ✓ Content-Type: application/json
  ✗ X-Frame-Options: MISSING — Vulnerable to clickjacking
  ✗ X-Content-Type-Options: MISSING — Vulnerable to MIME sniffing
  ✗ Strict-Transport-Security: MISSING — No HTTPS enforcement
  ✗ Content-Security-Policy: MISSING — No XSS protection policy
  ✗ X-XSS-Protection: MISSING — No XSS filter
  Missing 5 of 6 security headers!

============================================================
```

---

## Submission

- Only submit your GitHub repository link (No screenshots, no ZIP or Python files, just the link). For example:
  [https://github.com/sojoudian/COMP2152_Labs](https://github.com/sojoudian/COMP2152_Labs)
- Create a branch named **`lab_week14`**, complete your lab work in that branch, and once finished, merge it into your **`master`** branch.
