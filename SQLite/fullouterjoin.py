import sqlite3
# Connect to the SQLite database
conn = sqlite3.connect('example.db')

# Create a cursor object
cursor = conn.cursor()

# Perform a full outer join on the customers and orders tables
cursor.execute('''
    SELECT customers.name, orders.order_date, orders.total
    FROM customers
    LEFT JOIN orders
    ON customers.customer_id = orders.customer_id
    UNION ALL
    SELECT customers.name, orders.order_date, orders.total
    FROM orders
    LEFT JOIN customers
    ON orders.customer_id = customers.customer_id
    WHERE customers.customer_id IS NULL
''')

# Fetch all the rows
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)