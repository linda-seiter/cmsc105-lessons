import unittest
from unittest.mock import patch
import io

class TestCase(unittest.TestCase):
    def run_io_test(self, input_values, expected_output):
        """Helper method to run the test for a given input and expected output."""
        with patch('builtins.input', side_effect=input_values):
            with patch("sys.stdout", new=io.StringIO()) as mock_stdout:
                with open("io_challenge.py", "r") as file:
                    code = file.read()
                    exec(code)
                    actual_output = mock_stdout.getvalue().strip()
                    self.assertEqual(expected_output, actual_output, 'Actual and expected output should match.')

    def test_amir_england(self):
        """Test Amir from England"""
        input_values = ['Amir', 'England']
        expected_output = "Hi Amir from England!"
        self.run_io_test(input_values, expected_output)

    def test_siena_france(self):
        """Test for Siena from France"""
        input_values = ['Siena', 'France']
        expected_output = "Hi Siena from France!"
        self.run_io_test(input_values, expected_output)

