import pytest  # type: ignore[reportMissingImports]
from src.subarray_c2913 import Solution

@pytest.mark.parametrize(
    "nums, expected",
    [([1, 2, 1], 15),
    ([1, 1], 3),   
    ]
)
def test_subarray_c(nums, expected):
    sol = Solution()
    assert sol.sumCounts(nums) == expected