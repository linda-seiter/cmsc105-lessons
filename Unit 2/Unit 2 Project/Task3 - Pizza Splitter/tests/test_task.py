import unittest
from unittest.mock import patch
import io

class TestCase(unittest.TestCase):
    def run_io_test(self, input_values, expected_output):
        """Helper method to run the test for a given input and expected output format."""
        with patch('builtins.input', side_effect=input_values):
            with patch("sys.stdout", new=io.StringIO()) as mock_stdout:
                with open("unit2_task5.py", "r") as file:
                    code = file.read()
                    exec(code)  # Executes the code in unit2_task5.py
                    actual = mock_stdout.getvalue().strip()
                    self.assertEqual(expected_output, actual)

    def test_17_5(self):
        """Test for 17 slices and 5 people =  3 slices per person and 2 slices leftover"""
        input_values = ['17', '5']
        expected_output = 'Each person gets 3 slices.\nThere are 2 slices leftover.'
        self.run_io_test(input_values, expected_output)

    def test_12_2(self):
        """Test for 12 slices and 2 people =  6 slices per person and 0 slices leftover"""
        input_values = ['12', '2']
        expected_output = 'Each person gets 6 slices.\nThere are 0 slices leftover.'
        self.run_io_test(input_values, expected_output)
