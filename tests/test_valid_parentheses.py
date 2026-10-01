# tests/test_valid_parentheses.py
import pytest  # type: ignore[reportMissingImports]
from src.valid_parentheses_c020 import Solution


@pytest.mark.parametrize("strings, expected", [
    ("()[]{}", True),
    ("(]", False),
    ("([])", True),
    (")()", False),
])
def test_valid_parentheses(strings,expected):
    sol = Solution()
    assert sol.isValid(strings) == expected