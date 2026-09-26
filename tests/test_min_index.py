# tests/test_min_index.py

import pytest  # type: ignore[reportMissingImports]
from src.min_index_c3550 import Solution 

@pytest.mark.parametrize("nums, expected", [
    ([1, 3, 2], 2),
    ([1, 10, 11], 1),
    ([1, 2, 3], -1),
])
def test_smallest_index(nums, expected):
    sol = Solution()
    assert sol.smallestIndex(nums) == expected