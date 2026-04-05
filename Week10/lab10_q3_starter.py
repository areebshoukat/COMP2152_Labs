import sqlite3
import unittest

DB_NAME = "security_audit.db"


def setup_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS audit_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_type TEXT NOT NULL,
            severity TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)

    cursor.execute("DELETE FROM audit_log")

    sample_data = [
        ("Failed login", "HIGH", "2026-03-16 08:30:00"),
        ("Firewall rule changed", "MEDIUM", "2026-03-16 09:00:00"),
        ("Malware detected", "HIGH", "2026-03-16 09:30:00"),
        ("User added", "LOW", "2026-03-16 10:00:00"),
        ("Suspicious IP blocked", "HIGH", "2026-03-16 10:30:00"),
        ("Password changed", "LOW", "2026-03-16 11:00:00"),
        ("System scan completed", "MEDIUM", "2026-03-16 11:30:00"),
    ]

    cursor.executemany(
        "INSERT INTO audit_log (event_type, severity, timestamp) VALUES (?, ?, ?)",
        sample_data
    )

    conn.commit()
    conn.close()


def get_events_by_severity(severity):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM audit_log WHERE severity = ?", (severity,))
    rows = cursor.fetchall()
    conn.close()
    return rows


def get_recent_events(limit):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM audit_log ORDER BY timestamp DESC LIMIT ?",
        (limit,)
    )
    rows = cursor.fetchall()
    conn.close()
    return rows


def count_by_severity():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT severity, COUNT(*) FROM audit_log GROUP BY severity ORDER BY COUNT(*) DESC"
    )
    rows = cursor.fetchall()
    conn.close()
    return rows


def safe_query(query):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    finally:
        conn.close()


def display_events(rows):
    if not rows:
        print("  (no results)")
        return

    for row in rows:
        event_id, event_type, severity, timestamp = row
        print(f"  {event_id:<2} | {event_type:<22} | {severity:<6} | {timestamp}")


class TestAuditLog(unittest.TestCase):

    def test_high_severity(self):
        rows = get_events_by_severity("HIGH")
        self.assertEqual(len(rows), 3)

    def test_recent_events(self):
        rows = get_recent_events(5)
        self.assertEqual(len(rows), 5)

    def test_count(self):
        results = count_by_severity()
        self.assertIn(("HIGH", 3), results)

    def test_safe_bad_query(self):
        result = safe_query("SELECT * FROM fake_table")
        self.assertEqual(result, [])


if __name__ == "__main__":
    setup_database()

    print("=" * 60)
    print("  SECURITY AUDIT LOG")
    print("=" * 60)

    print("\n--- HIGH Severity Events ---")
    display_events(get_events_by_severity("HIGH"))

    print("\n--- 5 Most Recent Events ---")
    display_events(get_recent_events(5))

    print("\n--- Event Counts by Severity ---")
    for severity, count in count_by_severity():
        print(f"  {severity:<6} | {count}")

    print("\n--- Running Unit Tests ---")
    unittest.main(argv=['first-arg-is-ignored'], exit=False)