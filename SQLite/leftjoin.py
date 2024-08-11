import sqlite3
# Connect to the SQLite database
conn = sqlite3.connect('example.db')

# Create a cursor object
cursor = conn.cursor()

# Perform a left join on the customers and orders tables
cursor.execute('''
    SELECT customers.name, orders.order_date, orders.total
    FROM customers
    LEFT JOIN orders
    ON customers.customer_id = orders.customer_id
''')

# Fetch all the rows
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)