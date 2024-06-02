import re
import support
from extraction import TestClass


def run_count_assertions(test_class: TestClass):
    total_points = 0

    for test in test_class.test_cases:
        assertions = find_assertions(test)
        total_points = total_points + assertions
    return total_points


def find_assertions(test):
    assertAll_assertions = 0
    positive_assertions = 0
    negative_assertions = 0
    equal_assertions = 0
    mocking_assertions = 0

    assertAll_pattern = re.compile("assertAll")
    positive_pattern = re.compile("assertNotEquals|assertNotNull|assertNotSame|assertNull|assertSame|"
                                  "assertTimeout|assertTimeoutPreemptively|assertTrue")
    negative_pattern = re.compile("assertFalse|assertThrows|fail")
    equal_pattern = re.compile("assertArrayEquals|assertEquals|assertIterableEquals|assertLinesMatch|assertThat")
    mocking_pattern = re.compile(".*(?:verify|Validate)\(")

    for line in test.raw:
        line = support.support.preprocess_line(line)
        if not support.support.is_row_comment(line):
            # if assertAll_pattern.search(str(line)):
            # equal_assertions += 1
            if positive_pattern.search(str(line)):
                positive_assertions += 1
            if negative_pattern.search(str(line)):
                negative_assertions += 1
            if equal_pattern.search(str(line)):
                equal_assertions += 1
            if mocking_pattern.search(str(line)):
                mocking_assertions += 1

    # scores = [assertAll_assertions, positive_assertions, negative_assertions, equal_assertions, mocking_assertions]
    scores = positive_assertions + negative_assertions + equal_assertions + mocking_assertions - 1
    if scores <= 0:
        scores = 0
    return scores
