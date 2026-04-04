import sqlite3
from datetime import datetime

DB_NAME = "login_attempts.db"


def setup_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS login_attempts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            success BOOLEAN NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def record_attempt(username, success):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO login_attempts (username, success, timestamp) VALUES (?, ?, ?)",
        (username, success, datetime.now())
    )

    conn.commit()
    conn.close()


def get_failed_attempts(username):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT username, success, timestamp FROM login_attempts WHERE username = ? AND success = 0",
        (username,)
    )
    rows = cursor.fetchall()

    conn.close()
    return rows


def count_failures_per_user():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT username, COUNT(*) FROM login_attempts WHERE success = 0 GROUP BY username"
    )
    rows = cursor.fetchall()

    conn.close()
    return rows


def delete_old_attempts(username):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM login_attempts WHERE username = ?", (username,))
    deleted = cursor.rowcount

    conn.commit()
    conn.close()
    return deleted


def display_attempts(rows):
    if not rows:
        print("  (no results)")
        return

    for username, success, timestamp in rows:
        status = "success" if success else "FAILED"
        print(f"  {username:<8} | {status:<7} | {timestamp}")


def display_failure_counts(rows):
    if not rows:
        print("  (no failed attempts)")
        return

    for username, count in rows:
        if username == "root" and count >= 4:
            print(f"  {username:<10} {count} failed attempts  ⚠ root has {count} failed attempts — possible brute-force!")
        else:
            print(f"  {username:<10} {count} failed attempts")


if __name__ == "__main__":
    setup_database()

    print("=" * 60)
    print("  LOGIN ATTEMPT TRACKER")
    print("=" * 60)

    print("\n--- Recording Login Attempts ---")
    record_attempt("admin", True)
    print("  Recorded: admin (success)")

    record_attempt("admin", False)
    print("  Recorded: admin (FAILED)")

    record_attempt("admin", False)
    print("  Recorded: admin (FAILED)")

    record_attempt("admin", False)
    print("  Recorded: admin (FAILED)")

    record_attempt("guest", True)
    print("  Recorded: guest (success)")

    record_attempt("guest", False)
    print("  Recorded: guest (FAILED)")

    record_attempt("root", False)
    print("  Recorded: root (FAILED)")

    record_attempt("root", False)
    print("  Recorded: root (FAILED)")

    record_attempt("root", False)
    print("  Recorded: root (FAILED)")

    record_attempt("root", False)
    print("  Recorded: root (FAILED)")

    print("\n--- Failed Attempts for 'admin' ---")
    admin_failed = get_failed_attempts("admin")
    display_attempts(admin_failed)

    print("\n--- Failure Counts ---")
    failure_counts = count_failures_per_user()
    display_failure_counts(failure_counts)

    print("\n--- Reset 'root' account (delete all attempts) ---")
    deleted = delete_old_attempts("root")
    print(f"  Deleted {deleted} records for root")

    print("\n--- Failure Counts (after reset) ---")
    failure_counts = count_failures_per_user()
    display_failure_counts(failure_counts)

    print("\n" + "=" * 60)