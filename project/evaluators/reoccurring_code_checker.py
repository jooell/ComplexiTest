import re
import support.support
from extraction import TestClass

ignore_strings = ("assertNotEquals|assertNotNull|assertNotSame|assertNull|assertSame|"
                  "assertTimeout|assertTimeoutPreemptively|assertTrue|assertFalse|assertThrows|fail|"
                  "assertArrayEquals|assertEquals|assertIterableEquals|assertLinesMatch|"
                  "assertThat|assertAll|public|void|@Test|@ParameterizedTest|verify|Validate|while|if|else "
                  "if|else|try|catch|finally|switch|case")


def run_reoccurring_code_checker(test_class: TestClass):
    """
    Finds common code through tests for each class.
    Two or more identical lines, in two or more tests, can be placed in fixtures/setups
    To avoid repeating code
    """
    total_points = 0
    common_strings_grouped = []
    for test in test_class.test_cases:
        common_strings_grouped.append(get_code_samples_one(test, test.name))
    total_points += get_code_samples_two(common_strings_grouped)
    return total_points


def get_code_samples_one(test, test_name):
    """
    Finds valid lines and returns dict representing each test
    """
    extracted_lines = {}
    lines = []
    for line in test.raw:
        escaped_strings = '|'.join(re.escape(s) for s in ignore_strings.split('|'))
        pattern = re.compile(r'\b(?:' + escaped_strings + r')\b')
        specials = re.compile(r'^[\(\)\{\}\]\[;]+$')

        if not pattern.search(line):
            if not specials.search(line):
                if not support.support.is_row_comment(line):
                    if not line.isspace():
                        if not len(line) == 0:
                            lines.append(line)
    extracted_lines[test_name] = lines
    return extracted_lines


def get_code_samples_two(reference_list):
    """
    Loops through and checks lines between the different code blocks
    """
    points = 0
    # Tracked code blocks representing a single test
    processed_code_blocks = set()

    for first_idx, code_block in enumerate(reference_list):
        # already checked blocks
        if first_idx in processed_code_blocks:
            continue

        item_name = list(code_block.keys())[0]
        code_lines = set(code_block[item_name])

        for second_idx, other_item_dict in enumerate(reference_list):
            if first_idx != second_idx and second_idx not in processed_code_blocks:
                other_item_name = list(other_item_dict.keys())[0]
                other_item_lines = set(other_item_dict[other_item_name])

                # find common lines
                common_lines = code_lines.intersection(other_item_lines)

                # if two common lines for two code blocks
                if len(common_lines) >= 2:
                    common_lines_str = ", ".join(common_lines)
                    # print(f"{item_name} and {other_item_name} have common lines: {common_lines_str}")
                    points = points + 1

                # add both to processed
                processed_code_blocks.add(first_idx)
                processed_code_blocks.add(second_idx)
    return points
