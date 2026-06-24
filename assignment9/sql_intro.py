# Task 1: Create SQLite Database
# Task 2: Define Database Structure
import sqlite3

def add_publisher(cursor, name):
    try:
        cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

def add_magazine(cursor, name, publisher_id):
    try:
        cursor.execute("INSERT INTO magazines (name, publisher_id) VALUES (?,?)", (name, publisher_id))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

def add_subscriber(cursor, name, address):
    cursor.execute("SELECT * FROM subscribers WHERE name = ? AND address = ?", (name, address))
    if len(cursor.fetchall()) > 0:
        print(f"{name} at {address} is already a subscriber.")
        return
    cursor.execute("INSERT INTO subscribers (name, address) VALUES (?,?)", (name, address))

def add_subscription(cursor, subscriber_id, magazine_id, expiration_date):
    cursor.execute("SELECT * FROM subscriptions WHERE subscriber_id = ? AND magazine_id = ?", (subscriber_id, magazine_id))
    if len(cursor.fetchall()) > 0:
        print("This subscription already exists.")
        return
    cursor.execute("INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?,?,?)", (subscriber_id, magazine_id, expiration_date))

try:
    with sqlite3.connect("../db/magazines.db") as conn:
        conn.execute("PRAGMA foreign_keys = 1")
        print("Database created and connected successfully.")
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            publisher_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS magazines (
            magazine_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            publisher_id INTEGER,
            FOREIGN KEY (publisher_id) REFERENCES publishers (publisher_id)
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            subscriber_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT NOT NULL
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            subscription_id INTEGER PRIMARY KEY,
            subscriber_id INTEGER,
            magazine_id INTEGER,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (subscriber_id) REFERENCES subscribers (subscriber_id),
            FOREIGN KEY (magazine_id) REFERENCES magazines (magazine_id)
        )
        """)

        print("Tables created successfully.")

# Task 3: Populate Tables with Data
        add_publisher(cursor, "Conde Nast")
        add_publisher(cursor, "Hearst")
        add_publisher(cursor, "Meredith")

        cursor.execute("SELECT publisher_id FROM publishers WHERE name = ?", ("Conde Nast",))
        conde_nast_id = cursor.fetchone()[0]

        cursor.execute("SELECT publisher_id FROM publishers WHERE name = ?", ("Hearst",))
        hearst_id = cursor.fetchone()[0]

        add_magazine(cursor, "Vogue", conde_nast_id)
        add_magazine(cursor, "GQ", conde_nast_id)
        add_magazine(cursor, "Cosmopolitan", hearst_id)

        add_subscriber(cursor, "Charlie Kelly", "123 Paddy's Pub St")
        add_subscriber(cursor, "Dennis Reynolds", "456 Shore Ave")
        add_subscriber(cursor, "Mac McDonald", "789 Karate Rd")

        cursor.execute("SELECT subscriber_id FROM subscribers WHERE name = ?", ("Charlie Kelly",))
        charlie_id = cursor.fetchone()[0]
        cursor.execute("SELECT magazine_id FROM magazines WHERE name = ?", ("Vogue",))
        vogue_id = cursor.fetchone()[0]

        add_subscription(cursor, charlie_id, vogue_id, "2027-01-01")

        cursor.execute("SELECT subscriber_id FROM subscribers WHERE name = ?", ("Dennis Reynolds",))
        dennis_id = cursor.fetchone()[0]
        cursor.execute("SELECT magazine_id FROM magazines WHERE name = ?", ("GQ",))
        gq_id = cursor.fetchone()[0]

        cursor.execute("SELECT subscriber_id FROM subscribers WHERE name = ?", ("Mac McDonald",))
        mac_id = cursor.fetchone()[0]
        cursor.execute("SELECT magazine_id FROM magazines WHERE name = ?", ("Cosmopolitan",))
        cosmo_id = cursor.fetchone()[0]

        add_subscription(cursor, dennis_id, gq_id, "2027-03-15")
        add_subscription(cursor, mac_id, cosmo_id, "2027-06-30")

        conn.commit()
        print("Sample data inserted successfully.")

        # Task 4: Write SQL Queries

        print("\nQuery 1: All subscribers")
        cursor.execute("SELECT * FROM subscribers")
        for row in cursor.fetchall():
            print(row)

        print("\nQuery 2: Magazines sorted by name")
        cursor.execute("SELECT * FROM magazines ORDER BY name")
        for row in cursor.fetchall():
            print(row)

        print("\nQuery 3: Magazines published by Conde Nast")
        cursor.execute("""
            SELECT magazines.name FROM magazines
            JOIN publishers ON magazines.publisher_id = publishers.publisher_id
            WHERE publishers.name = ?
        """, ("Conde Nast",))
        for row in cursor.fetchall():
            print(row)

except Exception as e:
    print(f"Error: {e}")


