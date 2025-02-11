import unittest
from unittest.mock import patch
import io

class TestCase(unittest.TestCase):
    def run_io_test(self, input_values, expected_output):
        """Helper method to run the test for a given input and expected output format."""
        with patch('builtins.input', side_effect=input_values):
            with patch("sys.stdout", new=io.StringIO()) as mock_stdout:
                with open("unit1_task4.py", "r") as file:
                    code = file.read()
                    exec(code)  # Executes the code in unit1_task5.py
                    actual = mock_stdout.getvalue().strip()
                    self.assertEqual(expected_output, actual)

    def test_sleepy_apple_swim(self):
        """Test for sleepy, apple, swim"""
        input_values = ['sleepy', 'apple', 'swim']
        expected_output = 'The sleepy apple likes to swim everyday.'
        self.run_io_test(input_values, expected_output)

    def test_fluffy_pencil_yodel(self):
        """Test for fluffy_pencil_yodel"""
        input_values = ['fluffy', 'pencil', 'yodel']
        expected_output = 'The fluffy pencil likes to yodel everyday.'
        self.run_io_test(input_values, expected_output)
