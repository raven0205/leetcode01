# tests/reverse_str.py

import pytest  # type: ignore[reportMissingImports]
from src.reverse_str_c1190 import Solution 

@pytest.mark.parametrize("strings, expected", [
    ("(abcd)", "dcba"),
    ("(u(love)i)", "iloveu"),
    ("(ed(et(oc))el)", "leetcode"),
])
def test_reverse_str(strings, expected):
    sol = Solution()
    assert sol.reverseParentheses(strings) == expected