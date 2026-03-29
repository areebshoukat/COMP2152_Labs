class Finding:

    def __init__(self, subdomain, title, severity, description):
        self.subdomain = subdomain
        self.title = title
        self.severity = severity
        self.description = description

    def __str__(self):
        return f"[{self.severity}] {self.subdomain} — {self.title}"


class Report:

    def __init__(self, team_name):
        self.team_name = team_name
        self.findings = []

    def add_finding(self, finding):
        self.findings.append(finding)

    def get_by_severity(self, severity):
        return [f for f in self.findings if f.severity == severity]

    def summary(self):
        print(f"  Team: {self.team_name}")
        print(f"  Total findings: {len(self.findings)}")
        print(f"  HIGH:   {len(self.get_by_severity('HIGH'))}")
        print(f"  MEDIUM: {len(self.get_by_severity('MEDIUM'))}")
        print(f"  LOW:    {len(self.get_by_severity('LOW'))}")
        print("  ----------------------------------------")
        for f in self.findings:
            print(f"  {f}")


if __name__ == "__main__":
    print("=" * 60)
    print("  Q3: VULNERABILITY REPORT")
    print("=" * 60)

    findings_data = [
        ("ssh.0x10.cloud",  "Default credentials admin:admin",      "HIGH",   "SSH server accepts admin:admin"),
        ("blog.0x10.cloud", "No HTTPS (cleartext)",                 "LOW",    "Blog served over HTTP"),
        ("ftp.0x10.cloud",  "Anonymous FTP access",                 "HIGH",   "FTP allows anonymous login"),
        ("api.0x10.cloud",  "Server version exposed in headers",    "MEDIUM", "API leaks version"),
        ("cdn.0x10.cloud",  "Missing security headers",             "LOW",    "No security headers"),
    ]

    print("\n--- Adding Findings ---")
    report = Report("CyberHunters")
    for sub, title, sev, desc in findings_data:
        f = Finding(sub, title, sev, desc)
        report.add_finding(f)
        print(f"  Added: {f}")

    print("\n--- Full Report ---")
    report.summary()

    print("\n--- HIGH Severity Only ---")
    high = report.get_by_severity("HIGH")
    if high:
        for f in high:
            print(f"  {f}")
    else:
        print("  (none)")

    print("\n" + "=" * 60)