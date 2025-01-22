import unittest
from unittest.mock import patch
import io

class TestCase(unittest.TestCase):
    def test_output(self):
        with patch("sys.stdout", new=io.StringIO()) as mock_stdout:
            with open("task1.py", "r") as file:
                code = file.read()
                exec(code)
                actual_output = mock_stdout.getvalue()
                line_count = len(actual_output.splitlines())
                self.assertGreaterEqual(line_count , 4, '<br>You need to print at least 4 lines of output.')
