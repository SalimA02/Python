import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('example.db')

# Create a cursor object
cursor = conn.cursor()

# Drop the existing tables
cursor.execute('DROP TABLE IF EXISTS customers')
cursor.execute('DROP TABLE IF EXISTS orders')

# Create the customers table
cursor.execute('''
    CREATE TABLE customers (
        customer_id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT
    )
''')

# Create the orders table
cursor.execute('''
    CREATE TABLE orders (
        order_id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        order_date DATE,
        total REAL,
        FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
    )
''')

# Insert some data into the customers table
customers = [
    (1, 'John Doe', 'john@example.com'),
    (2, 'Jane Smith', 'jane@example.com'),
    (3, 'Bob Johnson', 'bob@example.com'),
    (4, 'Alice Brown', 'alice@example.com')  # This customer has no orders
]
cursor.executemany('INSERT INTO customers VALUES (?, ?, ?)', customers)

# Insert some data into the orders table
orders = [
    (1, 1, '2022-01-01', 100.00),
    (2, 1, '2022-01-15', 200.00),
    (3, 2, '2022-02-01', 50.00),
    (4, 3, '2022-03-01', 300.00),
    (5, None, '2022-04-01', 400.00)  # This order has no customer
]
cursor.executemany('INSERT INTO orders VALUES (?, ?, ?, ?)', orders)

# Commit the changes
conn.commit()