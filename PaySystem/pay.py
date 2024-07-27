import datetime
import sqlite3

class PayAssistingSystem:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS pay_data
            (date DATE PRIMARY KEY, amount REAL)
        """)
        self.conn.commit()

    def add_pay_data(self, date, amount):
        self.cursor.execute("INSERT INTO pay_data VALUES (?, ?)", (date, amount))
        self.conn.commit()

    def get_total_pay(self, start_date, end_date):
        if start_date > end_date:
            raise ValueError("Start date cannot be later than end date")
        self.cursor.execute("""
            SELECT SUM(amount) FROM pay_data
            WHERE date BETWEEN ? AND ?
        """, (start_date, end_date))
        result = self.cursor.fetchone()
        return result[0] if result[0] else 0

    def display_pay_data(self):
        self.cursor.execute("SELECT * FROM pay_data ORDER BY date")
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
            date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
            amount = float(input("Enter amount: "))
            system.add_pay_data(date, amount)
            print("Pay data added successfully.")
        elif choice == "2":
            start_date_input = input("Enter start date (YYYY-MM-DD): ")
            start_date = datetime.datetime.strptime(start_date_input, "%Y-%m-%d").date()
            end_date_input = input("Enter end date (YYYY-MM-DD): ")
            end_date = datetime.datetime.strptime(end_date_input, "%Y-%m-%d").date()
            total_pay = system.get_total_pay(start_date, end_date)
            print(f"Total pay for {start_date} to {end_date}: {total_pay}")
        elif choice == "3":
            system.display_pay_data()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()