"""
Test case class.
"""


class TestCase:
    """
    An encapsulated test case.
    """
    def __init__(self, name: str, raw: list[str]):
        self.name = name
        self.raw = raw
        self.tokens = []
