
import sqlite3
import os

# Create database folder
os.makedirs("database", exist_ok=True)


# Connect to database
def connect_db():
    conn = sqlite3.connect("database/hotel.db")
    return conn


# Create database tables
def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS rooms (
            room_id INTEGER PRIMARY KEY AUTOINCREMENT,
            room_number INTEGER UNIQUE,
            room_type TEXT,
            price REAL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reservations (
            reservation_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,
            room_id INTEGER,
            check_in TEXT,
            check_out TEXT,
            status TEXT,
            FOREIGN KEY(customer_id) REFERENCES customers(customer_id),
            FOREIGN KEY(room_id) REFERENCES rooms(room_id)
        )
    """)

    conn.commit()
    conn.close()

    print("Database and tables created successfully!")


# Add hotel rooms
def insert_rooms():
    conn = connect_db()
    cursor = conn.cursor()

    rooms = [
        (101, "Single", 1500),
        (102, "Single", 1500),
        (201, "Double", 2500),
        (202, "Double", 2500),
        (301, "Deluxe", 4000),
        (302, "Deluxe", 4000)
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO rooms
        (room_number, room_type, price)
        VALUES (?, ?, ?)
    """, rooms)

    conn.commit()
    conn.close()

    print("Hotel rooms added successfully!")


# Display hotel rooms
def get_rooms():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM rooms")

    rooms = cursor.fetchall()

    conn.close()

    return rooms


# Register a new customer
def add_customer(name, phone, email):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO customers (name, phone, email)
        VALUES (?, ?, ?)
    """, (name, phone, email))

    conn.commit()
    conn.close()

    print("Customer registered successfully!")