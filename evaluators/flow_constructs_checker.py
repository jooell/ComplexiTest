"""
Checks flow construct complexity.
"""

from extraction import TestClass, TestCase

flow_constructs_keywords = ["while", "do", "for", "if", "else", "else if",
                            "switch", "try", "catch", "finally"]


def run_flow_constructs_checker(test_class: TestClass) -> int:
    total_points = 0
    for test in test_class.test_cases:
        total_points += get_nesting_points(test)
        # indents = find_indentations(test)
        # for i in range(len(indents)):
        #     total_points[i] += indents[i]

    return total_points


def get_nesting_points(test_case: TestCase) -> int:
    nesting_points = 0
    nesting_level = 0
    nesting_stack = []
    for token in test_case.tokens:
        value = token.value

        if value in flow_constructs_keywords:
            nesting_stack.append(nesting_level)
            nesting_points += nesting_level
        elif value == "{":

            nesting_level += 1
        elif value == "}":

            nesting_level -= 1
            if len(nesting_stack) > 0 and nesting_stack[len(nesting_stack) - 1] == nesting_level:
                nesting_stack.pop()

    return nesting_points


