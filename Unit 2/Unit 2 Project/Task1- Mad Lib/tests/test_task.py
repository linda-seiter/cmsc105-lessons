import unittest
from unittest.mock import patch
import io
import re

class TestCase(unittest.TestCase):
    def run_io_test(self, input_values, expected_output):
        """Helper method to run the test for a given input and expected output format."""
        with patch('builtins.input', side_effect=input_values):
            with patch("sys.stdout", new=io.StringIO()) as mock_stdout:
                with open("unit2_task5.py", "r") as file:
                    code = file.read()
                    regex = r'print\(\s*[Ff]["\']'
                    if re.search(regex, code) is None:
                        raise self.failureException('<br>Use an f-string as an argument to the print() function')

                    exec(code)  # Executes the code in unit2_task5.py
                    actual = mock_stdout.getvalue().strip()
                    self.assertEqual(expected_output, actual)

    def test_sleepy_apple_swim(self):
        """Test for sleepy, apple, swim"""
        input_values = ['sleepy', 'apple', 'swim']
        expected_output = 'The sleepy apple likes to swim every day.'
        self.run_io_test(input_values, expected_output)

    def test_fluffy_pencil_yodel(self):
        """Test for fluffy_pencil_yodel"""
        input_values = ['fluffy', 'pencil', 'yodel']
        expected_output = 'The fluffy pencil likes to yodel every day.'
        self.run_io_test(input_values, expected_output)
