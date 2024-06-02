"""
Tests the assertion counter.
"""

import unittest
from extraction import extract_test_classes
from evaluators import run_count_assertions
from config import BASE_DIR


class TestAssertionCounter(unittest.TestCase):

    def setUp(self):
        self.test_class = extract_test_classes(f'{BASE_DIR}/_tests/_test_files')[0]

    def test_correct_assertion_counter_value(self):
        expected = 1
        assertion_counter_value = run_count_assertions(self.test_class)
        self.assertEqual(expected, assertion_counter_value)


if __name__ == '__main__':
    unittest.main()
