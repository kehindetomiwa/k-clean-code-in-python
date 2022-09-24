"""Clean Code in Python - Chapter 3: General Traits of Good Code
"""

import unittest

from src.exception_3 import InternalDataError, process


class TestException(unittest.TestCase):
    def test_original_exception(self):
        try:
            process({}, 6)
        except InternalDataError as e:
            print("ERROR CATCHED")
            self.assertIsInstance(e.__cause__, KeyError)
