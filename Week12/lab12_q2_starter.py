# Finding class
class Finding:
    def __init__(self, severity):
        self.severity = severity

    def __eq__(self, other):
        return self.severity == other.severity

    def __lt__(self, other):
        return self.severity < other.severity

    def __str__(self):
        return f"Finding({self.severity})"


# Report class
class Report:
    def __init__(self, findings):
        self.findings = findings

    def __len__(self):
        return len(self.findings)

    def __add__(self, other):
        return Report(self.findings + other.findings)

    def __str__(self):
        return f"Report with {len(self)} findings"


# MAIN
if __name__ == "__main__":
    f1 = Finding(3)
    f2 = Finding(1)
    f3 = Finding(5)

    # Compare
    print(f1 == f2)

    # Sort
    findings = [f1, f2, f3]
    findings_sorted = sorted(findings)
    print([f.severity for f in findings_sorted])

    # Reports
    r1 = Report([f1, f2])
    r2 = Report([f3])

    print(len(r1))

    r3 = r1 + r2
    print(len(r3))