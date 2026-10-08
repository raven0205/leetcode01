import pytest # type: ignore[reportMissingImports]
from src.remove_outermost_parentheses_c1021 import Solution

@pytest.mark.parametrize("strings, expected", [
    ("(()())(())", "()()()"),
    ("(()())(())(()(()))", "()()()()(())"),
    ("()", ""),
])

def test_outermost(strings,expected):
    sol = Solution()
    assert sol.removeOuterParentheses(strings) == expected