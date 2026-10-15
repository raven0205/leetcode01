# Date: 2026-10-15
# Difficulty: Easy
# Time Complexity: O(n^2)
# Space Complexity: O(n)
from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        # nested loop (outer loop)
        for i in range(n):
            # initialize a set for each position's set of combination
            s = set()

            # nested loop (inner loop)
            for j in range(i,n):
                s.add(nums[j])

                # then calculate the square of the distinct count
                total += len(s)**2

        return total

