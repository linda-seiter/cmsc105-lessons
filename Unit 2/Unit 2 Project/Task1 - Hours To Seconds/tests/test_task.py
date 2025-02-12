import unittest
from unittest.mock import patch
import io

class TestCase(unittest.TestCase):
    def run_io_test(self, input_values, expected_output):
        """Helper method to run the test for a given input and expected output format."""
        with patch('builtins.input', side_effect=input_values):
            with patch("sys.stdout", new=io.StringIO()) as mock_stdout:
                with open("unit2_task1.py", "r") as file:
                    code = file.read()
                    exec(code)  # Executes the code in unit1_task4.py
                    actual = mock_stdout.getvalue().strip()
                    self.assertEqual(expected_output, actual)

    def test_3_hours_10_minutes_7_seconds(self):
        """Test for 3 hours 10 minutes 7 seconds = 11407 total seconds"""
        input_values = ['3', '10', '7']
        expected_output = '3 hours, 10 minutes, and 7 seconds is equal to 11407 total seconds.'
        self.run_io_test(input_values, expected_output)

    def test_1_hour(self):
        """Test for 1 hour = 3600 total seconds"""
        input_values = ['1', '0', '0']
        expected_output = '1 hours, 0 minutes, and 0 seconds is equal to 3600 total seconds.'
        self.run_io_test(input_values, expected_output)

    def test_1_minute(self):
        """Test for 0 hours 1 minute 0 seconds = 60 total seconds"""
        input_values = ['0', '1', '0']
        expected_output = '0 hours, 1 minutes, and 0 seconds is equal to 60 total seconds.'
        self.run_io_test(input_values, expected_output)

    def test_1_second(self):
        """Test for 0 hours 0 minutes 1 second = 1 total seconds"""
        input_values = ['0', '0', '1']
        expected_output = '0 hours, 0 minutes, and 1 seconds is equal to 1 total seconds.'
        self.run_io_test(input_values, expected_output)
