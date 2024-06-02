"""
Tests extraction.
"""

import unittest
from extraction import extract_test_classes
from config import BASE_DIR


class TestExtraction(unittest.TestCase):

    def setUp(self):
        self.test_class = extract_test_classes(f'{BASE_DIR}/_tests/_test_files')[0]

    def test_correct_class_name(self):
        expected = "TestFile1Test"
        self.assertEqual(expected, self.test_class.name)

    def test_correct_number_of_test_cases(self):
        expected = 2
        test_cases = self.test_class.test_cases
        self.assertEqual(expected, len(test_cases))

    def test_correct_test_case_names(self):
        expected = ("test_valid_number_of_samples", "test_valid_number_of_samples")
        test_cases = self.test_class.test_cases
        for i in range(2):
            self.assertEqual(expected[i], test_cases[i].name)


if __name__ == '__main__':
    unittest.main()
