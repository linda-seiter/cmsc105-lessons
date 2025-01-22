import unittest
from unittest.mock import patch
import io

class TestCase(unittest.TestCase):
    def run_io_test(self, input_value, expected_output):
        """Helper method to run the test for a given input and expected output."""
        with patch('builtins.input', return_value=input_value):
            with patch("sys.stdout", new=io.StringIO()) as mock_stdout:
                with open("task3.py", "r") as file:
                    code = file.read()
                    exec(code)
                    actual_output = mock_stdout.getvalue().strip()
                    self.assertEqual(expected_output, actual_output, 'Actual and expected output should match.')

    def test_cs(self):
        """Test for Computer Science input."""
        self.run_io_test('Computer Science', "Computer Science is a great major!")

    def test_cyber(self):
        """Test for Cybersecurity Technology input."""
        self.run_io_test('Cybersecurity Technology', "Cybersecurity Technology is a great major!")

    def test_web(self):
        """Test for Web and Digital Design input."""
        self.run_io_test('Web and Digital Design', "Web and Digital Design is a great major!")