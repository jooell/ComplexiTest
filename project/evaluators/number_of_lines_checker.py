import re
import support
from extraction import TestClass

ignore_strings = ("assertNotEquals|assertNotNull|assertNotSame|assertNull|assertSame|"
                  "assertTimeout|assertTimeoutPreemptively|assertTrue|assertFalse|assertThrows|fail|"
                  "assertArrayEquals|assertEquals|assertIterableEquals|assertLinesMatch|"
                  "assertThat|assertAll|verify|Validate")
ignore_strings2 = "public|void|@Test|@ParameterizedTest"


def run_number_of_lines_checker(test_class: TestClass):
    total_points = 0
    for test in test_class.test_cases:
        processed_test = support.support.preprocess_test(test)

        total_points += line_counter(processed_test)

    return total_points


def line_counter(test):
    """
    Counts lines of a test. Does not count brackets, comments and asserts.
    """
    count = 0
    assert_brackets = False
    for line in test:
        escaped_strings = '|'.join(re.escape(s) for s in ignore_strings.split('|'))
        pattern = re.compile(r'\b(?:' + escaped_strings + r')\b')

        escaped_strings2 = '|'.join(re.escape(s) for s in ignore_strings2.split('|'))
        pattern2 = re.compile(r'\b(?:' + escaped_strings2 + r')\b')
        specials = re.compile(r'^[\(\)\{\}\]\[;]+$')

        line = support.support.preprocess_line(line)
        if pattern.search(line):
            if str(line).endswith("{"):
                assert_brackets = True
                continue
        if assert_brackets:
            if str(line).endswith("});"):
                assert_brackets = False
        else:
            if not pattern.search(line) and not pattern2.search(line) and not specials.search(line):
                if not support.support.is_row_comment(line):
                    if line.strip():
                        count = count + 1

    count = count - 3
    if count <= 0:
        count = 0
    return count
