import unittest
from unittest.mock import patch
import io

class TestCase(unittest.TestCase):
    def run_io_test(self, input_values, expected_output):
        """Helper method to run the test for a given input and expected output."""
        with patch('builtins.input', side_effect=input_values):
            with patch("sys.stdout", new=io.StringIO()) as mock_stdout:
                with open("unit1_task3.py", "r") as file:
                    code = file.read()
                    exec(code)
                    actual_output = mock_stdout.getvalue().strip()
                    self.assertEqual(expected_output, actual_output, 'Actual and expected output should match.')

    def test_cs(self):
        """Test for Computer Science input."""
        input_values = ['Computer Science']
        expected_output = "Computer Science is a great major!"
        self.run_io_test(input_values, expected_output)

    def test_cyber(self):
        """Test for Cybersecurity Technology input."""
        input_values = ['Cybersecurity Technology']
        expected_output = "Cybersecurity Technology is a great major!"
        self.run_io_test(input_values, expected_output)

    def test_web(self):
        """Test for Web and Digital Design input."""
        input_values = ['Web and Digital Design']
        expected_output = "Web and Digital Design is a great major!"
        self.run_io_test(input_values, expected_output)