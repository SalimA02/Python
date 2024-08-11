import unittest
from unittest.mock import Mock
from innerjoin import inner_join

class TestInnerJoin(unittest.TestCase):
    def setUp(self):
        self.conn = Mock()
        self.cursor = self.conn.cursor.return_value

    def test_inner_join(self):
        # Set up the mock data
        customers = [
            (1, 'John Doe', 'john@example.com'),
            (2, 'Jane Smith', 'jane@example.com')
        ]
        orders = [
            (1, 1, '2022-01-01', 100.00),
            (2, 1, '2022-01-15', 200.00),
            (3, 2, '2022-02-01', 50.00)
        ]

        # Set up the mock cursor to return the data
        self.cursor.execute.return_value = customers + orders

        # Call the inner_join function
        result = inner_join(self.conn)

        # Verify the expected results
        expected_result = [
            ('John Doe', '2022-01-01', 100.0),
            ('John Doe', '2022-01-15', 200.0),
            ('Jane Smith', '2022-02-01', 50.0)
        ]
        self.assertEqual(result, expected_result)