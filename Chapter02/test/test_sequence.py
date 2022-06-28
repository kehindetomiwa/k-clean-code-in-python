import unittest
from src.sequence import MyItems


class TestSequence(unittest.TestCase):

    def test_items(self):
        items = MyItems(1, 2, 3, 4, 5)
        self.assertEqual(items[-1], 5)
        self.assertEqual(items[0], 1)
        self.assertEqual(len(items), 5)


if __name__ == "__main__":
    unittest.main()