import unittest

from garden import take_until_trees


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_trees(self):
        self.assertEqual(take_until_trees(["🌹🌹", "🌷🌷", "🌻🌻🌻"]), ["🌹🌹", "🌷🌷", "🌻🌻🌻"])
        #assert_equal(take_until_trees(["🌹🌹", "🌷🌷", "🌳", "🌻🌻🌻"]), ["🌹🌹", "🌷🌷"])
        #assert_equal(take_until_trees(["🌳", "🌸", "🌺🌺🌺🌺"]), [])
        #assert_equal(take_until_trees([]), [])
        #assert_equal(take_until_trees(["🌳🌳🌳"]), [])