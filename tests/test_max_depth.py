# tests/test_max_depth.py

import pytest  # type: ignore[reportMissingImports]
from src.max_depth_parentheses_c1614 import Solution 

@pytest.mark.parametrize("strings, expected", [
    ("(1+(2*3)+((8)/(4))+1)", 3),
    ("(1)+((2))+(((3)))", 3),
    ("()(())((()()))", 3),
])
def test_depth_str(strings, expected):
    sol = Solution()
    assert sol.maxDepth(strings) == expected