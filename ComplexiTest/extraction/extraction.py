"""
Using javalang to extract test classes and cases.
"""

import os
import javalang
from extraction import TestClass, TestCase

CompilationUnit = javalang.parser.tree.CompilationUnit
MethodInvocation = javalang.parser.tree.MethodInvocation
BinaryOperation = javalang.parser.tree.BinaryOperation
Literal = javalang.parser.tree.Literal
Annotation = javalang.parser.tree.Annotation

TEST_CASE_ANNOTATIONS = ["Test", "ParameterizedTest"]


def extract_test_classes(directory: str) -> list[TestClass]:
    """
    Used to retrieve the test files.
    :return: a list of test files.
    """
    test_classes = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".java"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    tmp = f.readlines()
                    lines = []
                    for line in tmp:
                        lines.append(line.strip())
                    test_class = _extract_test_class(lines)
                    if test_class is not None:
                        test_classes.append(test_class)

    return test_classes


def _extract_test_class(code: list[str]) -> TestClass or None:
    code_joined = "\n".join(code)
    tree = javalang.parse.parse(code_joined)
    test_class: TestClass or None = None
    for path, node in tree:
        if isinstance(node, javalang.parser.tree.ClassDeclaration):
            test_class = TestClass(node.name, code)
            break
    if test_class is None:
        return None
    test_class.test_cases = _extract_test_cases(code)
    return None if len(test_class.test_cases) == 0 else test_class


def _extract_test_cases(code: list[str]) -> list[TestCase]:
    code_joined = "\n".join(code)
    tree = javalang.parse.parse(code_joined)
    test_cases = []
    for path, node in tree:
        if isinstance(node, javalang.parser.tree.MethodDeclaration):
            if not _is_test_case(node.annotations):
                continue
            start_line = node.position.line - 1
            end_line = _get_end_line(code, start_line)
            body = "\n".join(code[start_line:end_line])
            test_case = TestCase(node.name, code[start_line:end_line])
            tokenizer = javalang.tokenizer.tokenize(body)
            for token in tokenizer:
                test_case.tokens.append(token)
            test_cases.append(test_case)
    return test_cases


def _is_test_case(annotations: list[Annotation]) -> bool:
    for annotation in annotations:
        if annotation.name in TEST_CASE_ANNOTATIONS:
            return True
    return False


def _get_end_line(code: list[str], start_pos: int) -> int:
    opening_bracket_found = False
    bracket_sum = 0
    pos = start_pos
    while True:
        for char in list(code[pos]):
            if char == '{':
                opening_bracket_found = True
                bracket_sum += 1
            elif char == '}':
                bracket_sum -= 1
            if bracket_sum == 0 and opening_bracket_found:
                return pos + 1
        pos += 1


