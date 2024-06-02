"""
Test file class.
"""
from extraction import TestCase


class TestClass:
    """
    An encapsulated test file.
    """
    def __init__(self, name: str, raw: list[str]):
        self.name = name
        self.raw = raw
        self.test_cases: list[TestCase] = []
