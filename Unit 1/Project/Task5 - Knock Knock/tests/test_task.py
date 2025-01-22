import unittest
from unittest.mock import patch
import io

class TestCase(unittest.TestCase):
    def run_io_test(self, input_values, expected_output):
        """Helper method to run the test for a given input and expected output format."""
        with patch('builtins.input', side_effect=input_values):
            with patch("sys.stdout", new=io.StringIO()) as mock_stdout:
                with open("task5.py", "r") as file:
                    code = file.read()
                    exec(code)  # Executes the code in task5.py
                    actual_output = mock_stdout.getvalue().strip()
                    self.assertEqual(expected_output, actual_output, 'Actual and expected output should match.')

    def test_boo(self):
        """Test for Boo, Don't cry!"""
        input_values = ['Boo', "Don't cry!"]
        expected_output = "Knock-knock.\nWho's there?\nBoo\nBoo who?\nDon't cry!"
        self.run_io_test(input_values, expected_output)

    def test_java_nice_day(self):
        """Test for Java, Java nice day!"""
        input_values = ['Java', 'Java nice day!']
        expected_output = "Knock-knock.\nWho's there?\nJava\nJava who?\nJava nice day!"
        self.run_io_test(input_values, expected_output)
