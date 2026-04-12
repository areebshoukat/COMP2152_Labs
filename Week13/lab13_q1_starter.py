# ============================================================
#  WEEK 13 LAB — Q1: SCAN DATA ANALYSIS
#  COMP2152 — [Areeb Shoukat]
# ============================================================

import csv

# Load findings from CSV file
def load_findings(filename):
    with open(filename, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

# Count occurrences by a specific field
def count_by_field(findings, field):
    counts = {}
    for row in findings:
        key = row[field]
        counts[key] = counts.get(key, 0) + 1
    return counts

# Filter findings by field and value
def filter_findings(findings, field, value):
    return [row for row in findings if row[field] == value]

# Get top N subdomains with most findings
def top_subdomains(findings, n):
    counts = {}
    for row in findings:
        sub = row["subdomain"]
        counts[sub] = counts.get(sub, 0) + 1

    # Sort descending by count
    sorted_subs = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_subs[:n]


# ===== MAIN TEST =====
if __name__ == "__main__":
    findings = load_findings("findings.csv")

    print("\n--- Severity Counts ---")
    print(count_by_field(findings, "severity"))

    print("\n--- Type Counts ---")
    print(count_by_field(findings, "type"))

    print("\n--- HIGH Severity Findings ---")
    high = filter_findings(findings, "severity", "HIGH")
    for f in high:
        print(f)

    print("\n--- Top 3 Subdomains ---")
    print(top_subdomains(findings, 3))