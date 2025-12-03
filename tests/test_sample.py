# pylint: disable-all

import unittest


class TestSample(unittest.TestCase):
    def test_sample(self):
        # We are simply checking whether 42==42!
        self.assertEqual(42, 42)  # raises an error if false

        # your_result = your_function()
        # self.assertEqual(your_result, correct_answer)
