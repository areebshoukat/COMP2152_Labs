# ============================================================
#  WEEK 13 LAB — Q2: ASCII DASHBOARD
#  COMP2152 — [Areeb Shoukat]
# ============================================================

from lab13_q1_starter import load_findings, count_by_field

# Print a bar chart in terminal
def bar_chart(data, title, max_width=30):
    print(f"\n{title}")

    max_value = max(data.values())

    for key, value in data.items():
        bar_length = int((value / max_value) * max_width)
        bar = "█" * bar_length
        print(f"{key:15} | {bar} ({value})")


# Return severity summary (HIGH first)
def severity_summary(findings):
    counts = count_by_field(findings, "severity")

    ordered = {}
    for key in ["HIGH", "MEDIUM", "LOW"]:
        if key in counts:
            ordered[key] = counts[key]

    return ordered


# Count findings by date (sorted)
def timeline(findings):
    counts = count_by_field(findings, "date")
    return dict(sorted(counts.items()))


# ===== MAIN TEST =====
if __name__ == "__main__":
    findings = load_findings("findings.csv")

    bar_chart(severity_summary(findings), "Severity Breakdown")
    bar_chart(timeline(findings), "Findings by Date")
    bar_chart(count_by_field(findings, "type"), "Vulnerability Types")