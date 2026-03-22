import sqlite3

DB_NAME = "password_vault.db"


def setup_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vault (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            website TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def add_credential(website, username, password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO vault (website, username, password) VALUES (?, ?, ?)",
        (website, username, password)
    )

    conn.commit()
    conn.close()


def get_all_credentials():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT website, username, password FROM vault ORDER BY website ASC")
    rows = cursor.fetchall()

    conn.close()
    return rows


def find_credential(website):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT website, username, password FROM vault WHERE website = ?",
        (website,)
    )
    rows = cursor.fetchall()

    conn.close()
    return rows


def display_credentials(rows):
    if not rows:
        print("  (no results)")
        return

    for website, username, password in rows:
        print(f"  {website:<14} | {username:<12} | {password}")


if __name__ == "__main__":
    setup_database()

    print("=" * 60)
    print("  PASSWORD VAULT")
    print("=" * 60)

    print("\n--- Adding Credentials ---")
    add_credential("github.com", "admin", "s3cur3P@ss")
    print("  Saved: github.com")

    add_credential("google.com", "maziar@gmail", "MyP@ssw0rd")
    print("  Saved: google.com")

    add_credential("netflix.com", "maziar", "N3tfl1x!")
    print("  Saved: netflix.com")

    add_credential("github.com", "work_user", "W0rkP@ss!")
    print("  Saved: github.com (work)")

    print("\n--- All Credentials ---")
    all_rows = get_all_credentials()
    display_credentials(all_rows)

    print("\n--- Search for 'github.com' ---")
    github_rows = find_credential("github.com")
    display_credentials(github_rows)

    print("\n--- Search for 'spotify.com' ---")
    spotify_rows = find_credential("spotify.com")
    display_credentials(spotify_rows)

    print("\n" + "=" * 60)