import unittest
from unittest.mock import patch
from pay import PayAssistingSystem
import sqlite3

class TestPayAssistingSystem(unittest.TestCase):
    def setUp(self):
        self.system = PayAssistingSystem(":memory:")

    def test_add_pay_data(self):
        date = "2024-06-11"
        amount = 100.0
        self.system.add_pay_data(date, amount)
        self.system.cursor.execute("SELECT * FROM pay_data WHERE date = ?", (date,))
        result = self.system.cursor.fetchone()
        self.assertEqual(result, (date, amount))

    def test_get_total_pay(self):
        self.system.add_pay_data("2024-06-10", 100.0)
        self.system.add_pay_data("2024-06-11", 200.0)
        total_pay = self.system.get_total_pay("2024-06-10", "2024-06-11")
        self.assertEqual(total_pay, 300.0)

    def test_get_total_pay_no_data(self):
        total_pay = self.system.get_total_pay("2024-06-10", "2024-06-11")
        self.assertEqual(total_pay, 0)

    def test_display_pay_data(self):
        self.system.add_pay_data("2024-06-10", 100.0)
        self.system.add_pay_data("2024-06-11", 200.0)
        with patch('builtins.print') as mock_print:
            self.system.display_pay_data()
            mock_print.assert_any_call("All Pay:")
            mock_print.assert_any_call("2024-06-10: 100.0")
            mock_print.assert_any_call("2024-06-11: 200.0")

    def test_display_pay_data_no_data(self):
        with patch('builtins.print') as mock_print:
            self.system.display_pay_data()
            mock_print.assert_called_once_with("No pay data available.")

    def tearDown(self):
        self.system.conn.close()

if __name__ == "__main__":
    unittest.main()