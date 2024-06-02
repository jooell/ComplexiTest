"""
Tests the number of lines checker.
"""

import unittest
from extraction import extract_test_classes
from evaluators import run_number_of_lines_checker
from config import BASE_DIR


class TestNumberOfLinesChecker(unittest.TestCase):

    def setUp(self):
        self.test_class = extract_test_classes(f'{BASE_DIR}/_tests/_test_files')[0]

    def test_correct_assertion_counter_value(self):
        expected = 4
        number_of_lines_value = run_number_of_lines_checker(self.test_class)
        self.assertEqual(expected, number_of_lines_value)


if __name__ == '__main__':
    unittest.main()