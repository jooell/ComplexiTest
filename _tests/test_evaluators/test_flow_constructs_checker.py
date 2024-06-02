"""
Tests the flow construct checker.
"""

import unittest
from extraction import extract_test_classes
from evaluators import run_flow_constructs_checker
from config import BASE_DIR


class TestFlowConstructChecker(unittest.TestCase):

    def setUp(self):
        self.test_class = extract_test_classes(f'{BASE_DIR}/_tests/_test_files')[0]

    def test_correct_assertion_counter_value(self):
        expected = 7
        flow_construct_value = run_flow_constructs_checker(self.test_class)
        self.assertEqual(expected, flow_construct_value)


if __name__ == '__main__':
    unittest.main()
