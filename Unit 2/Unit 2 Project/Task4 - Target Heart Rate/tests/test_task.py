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
                    exec(code)  # Executes the code in unit1_task5.py
                    actual = mock_stdout.getvalue().strip()
                    self.assertEqual(expected_output, actual)

    def test_28(self):
        """Test for 28 years old"""
        input_values = ['28']
        expected_output = 'For Age = 28 years,\nMaximum heart rate = 192 bpm\nTarget for moderate activity = 96 to 134 bpm\nTarget for intense activity = 134 to 163 bpm'
        self.run_io_test(input_values, expected_output)

    def test_40(self):
        """Test for 40 years old"""
        input_values = ['40']
        expected_output = 'For Age = 40 years,\nMaximum heart rate = 180 bpm\nTarget for moderate activity = 90 to 125 bpm\nTarget for intense activity = 125 to 153 bpm'
        self.run_io_test(input_values, expected_output)
