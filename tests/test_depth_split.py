# tests/test_depth_split.py

import pytest #type:[ignoreMissingReports]
from src.max_depth_split_c1111 import Solution

@pytest.mark.parametrize("strings, expected", [
    ("(()())", [0, 1, 1, 1, 1, 0]),
    ("()(())()", [0, 0, 0, 1, 1, 0, 0, 0]),
])

def test_depth_split(strings, expected):
    sol = Solution()
    assert sol.maxDepthAfterSplit(strings) == expected