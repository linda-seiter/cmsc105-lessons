import unittest
from unittest.mock import patch
import io

class TestCase(unittest.TestCase):
    def run_io_test(self, input_values, expected_output):
        """Helper method to run the test for a given input and expected output format."""
        with patch('builtins.input', side_effect=input_values):
            with patch("sys.stdout", new=io.StringIO()) as mock_stdout:
                with open("unit2_task4.py", "r") as file:
                    code = file.read()
                    exec(code)  # Executes the code in unit2_task5.py
                    actual = mock_stdout.getvalue().strip()
                    self.assertEqual(expected_output, actual)

    def test1(self):
        """Test for 14.00 bill, 20% tip, 2 people."""
        input_values = ['14.00', '20', 2]
        expected_output = 'Total tip: $2.80\nTotal_bill: $16.80\nAmount per person: $8.40'
        self.run_io_test(input_values, expected_output)

    def test2(self):
        """Test for 38.95 bill, 15% tip, 3 people."""
        input_values = ['38.95', '15', '3']
        expected_output = 'Total tip: $5.84\nTotal_bill: $44.79\nAmount per person: $14.93'
        self.run_io_test(input_values, expected_output)