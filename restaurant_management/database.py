# database.py
import sqlite3

def connect_db():
    return sqlite3.connect("restaurant.db")

def create_tables():
    conn = connect_db()
    cur = conn.cursor()
    
    # Create menu table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS menu (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    # Create orders table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_id INTEGER,
            quantity INTEGER,
            total_price REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()

def add_menu_item(item_id, name, price):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT OR REPLACE INTO menu (id, name, price) VALUES (?, ?, ?)", (item_id, name, price))
    conn.commit()
    conn.close()

def get_menu():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM menu")
    items = cur.fetchall()
    conn.close()
    return items

def save_order(item_id, quantity, total_price):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO orders (item_id, quantity, total_price) VALUES (?, ?, ?)", (item_id, quantity, total_price))
    conn.commit()
    conn.close()
