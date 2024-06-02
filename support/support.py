"""
Support functions.
"""

import re
import javalang


def is_row_comment(line):
    prefixes = ["//", "/*", "*", "*/"]
    multiline_start = ["/*", "/**"]
    line.strip()
    line = str(line)
    if any(line.startswith(prefix) for prefix in prefixes):
        return True
    else:
        return False


def preprocess_test(test):
    prefixes_start = ["/**", "/*"]
    prefix_end = "*/"
    prefix_single = "//"
    in_multiline_comment = False
    processed_lines = []

    for line in test.raw:
        stripped_line = line.strip()

        if not in_multiline_comment:
            if any(stripped_line.startswith(prefix) for prefix in prefixes_start):
                # Start of a multiline comment
                in_multiline_comment = True
                # Check if the same line ends the comment
                if prefix_end in stripped_line:
                    in_multiline_comment = False
                continue  # Skip the line with the start of the comment
            elif stripped_line.startswith(prefix_single):
                # Skip single line comment
                continue
        else:
            # We are inside a multiline comment
            if prefix_end in stripped_line:
                # End of a multiline comment
                in_multiline_comment = False
            continue  # Skip all lines inside the comment block

        # Add non-comment lines to the processed list
        processed_lines.append(line)

    # Update the test object with the processed lines
    return processed_lines


def preprocess_line(line):
    """
    Remove quotes that may interfere with regex
    """
    inside_string = False
    processed_line = ''
    for char in line:
        if char in ('"', "'"):
            line = line.replace(char, ' ')
    #     inside_string = not inside_string
    # if inside_string and char in ('{', '}'):
    #    processed_line += ' '
    # else:
    #    processed_line += char
    return line
