import datetime
import sqlite3

class PayAssistingSystem:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS pay_data
            (date DATE PRIMARY KEY, amount REAL, employee_id INTEGER)
        """)
        self.conn.commit()

    def add_pay_data(self, date, amount, employee_id):
        try:
            self.cursor.execute("INSERT INTO pay_data VALUES (?, ?, ?)", (date, amount, employee_id))
            self.conn.commit()
        except sqlite3.IntegrityError:
            print("Error: Date already exists in the database.")

    def get_total_pay(self, start_date, end_date, employee_id):
        if start_date > end_date:
            raise ValueError("Start date cannot be later than end date")
        self.cursor.execute("""
            SELECT SUM(amount) FROM pay_data
            WHERE date BETWEEN ? AND ? AND employee_id = ?
        """, (start_date, end_date, employee_id))
        result = self.cursor.fetchone()
        return result[0] if result[0] else 0

    def display_pay_data(self, employee_id):
        self.cursor.execute("SELECT * FROM pay_data WHERE employee_id = ? ORDER BY date", (employee_id,))
        rows = self.cursor.fetchall()
        if rows:
            print("All Pay:")
            for row in rows:
                print(f"{row[0]}: {row[1]}")
        else:
            print("No pay data available.")

def main():
    system = PayAssistingSystem("pay_data.db")

    while True:
        print("\nPay Assisting System Menu:")
        print("1. Add pay data")
        print("2. Get total pay for a date range")
        print("3. Display all pay data")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date_input = input("Enter date (YYYY-MM-DD): ")
            try:
                date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
            except ValueError:
                print("Invalid date format. Please try again.")
                continue
            amount = float(input("Enter amount: "))
            employee_id = int(input("Enter employee ID: "))
            system.add_pay_data(date, amount, employee_id)
            print("Pay data added successfully.")
        elif choice == "2":
            start_date_input = input("Enter start date (YYYY-MM-DD): ")
            try:
                start_date = datetime.datetime.strptime(start_date_input, "%Y-%m-%d").date()
            except ValueError:
                print("Invalid date format. Please try again.")
                continue
            end_date_input = input("Enter end date (YYYY-MM-DD): ")
            try:
                end_date = datetime.datetime.strptime(end_date_input, "%Y-%m-%d").date()
            except ValueError:
                print("Invalid date format. Please try again.")
                continue
            employee_id = int(input("Enter employee ID: "))
            total_pay = system.get_total_pay(start_date, end_date, employee_id)
            print(f"Total pay for {start_date} to {end_date}: {total_pay}")
        elif choice == "3":
            employee_id = int(input("Enter employee ID: "))
            system.display_pay_data(employee_id)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()