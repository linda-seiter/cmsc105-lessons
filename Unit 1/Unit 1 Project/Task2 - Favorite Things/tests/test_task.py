import unittest
from unittest.mock import patch
import io
import re

class TestCase(unittest.TestCase):
    def test_output(self):
        with patch("sys.stdout", new=io.StringIO()) as mock_stdout:
            with open("unit1_task2.py", "r") as file:
                code = file.read()
                if re.search(r'favorite_food\s+=', code) is None:
                    raise self.failureException('<br>Assign a variable named favorite_food.')
                exec(code)
                actual_output = mock_stdout.getvalue()
                if re.search(r'print([^)]*favorite_food[^)]*)', code) is None:
                    raise self.failureException('<br>Print the value of the favorite_food variable.')