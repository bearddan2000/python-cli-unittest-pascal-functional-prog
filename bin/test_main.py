from io import StringIO
from unittest.mock import patch
import unittest

import main

class TestMain(unittest.TestCase):
    """docstring for TestMain."""

    def test_col(self):
        with patch('sys.stdout', new = StringIO()) as captured:
            main.col(0, 1)
            self.assertEqual(captured.getvalue(), "1, \n1, 1, \n")

    def test_row(self):
        with patch('sys.stdout', new = StringIO()) as captured:
            main.row(0, 1, 1)
            self.assertEqual(captured.getvalue(), "1, 1, ")
