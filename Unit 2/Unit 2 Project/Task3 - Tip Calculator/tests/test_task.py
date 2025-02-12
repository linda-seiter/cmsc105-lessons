import unittest
from unittest.mock import patch
import io

class TestCase(unittest.TestCase):
    def run_io_test(self, input_values, expected_output):
        """Helper method to run the test for a given input and expected output format."""
        with patch('builtins.input', side_effect=input_values):
            with patch("sys.stdout", new=io.StringIO()) as mock_stdout:
                with open("unit2_task3.py", "r") as file:
                    code = file.read()
                    exec(code)  # Executes the code in unit1_task4.py
                    actual = mock_stdout.getvalue().strip()
                    self.assertEqual(expected_output, actual)

    def test1(self):
        """Test for 14.00 bill and 20% tip =  The tip should be $2.80."""
        input_values = ['14.00', '20']
        expected_output = 'The tip should be $2.80.'
        self.run_io_test(input_values, expected_output)

    def test2(self):
        """Test for 8.95 bill and 10% tip =  The tip should be $0.90."""
        input_values = ['8.95', '10']
        expected_output = 'The tip should be $0.90.'
        self.run_io_test(input_values, expected_output)