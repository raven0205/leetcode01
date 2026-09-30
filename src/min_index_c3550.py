# submission date: 24.09.2026
# difficulty level: easy
# time complexity: O(n)
# space complexity: O(1)

from typing import List

class Solution:
    def smallestIndex(self, nums: List[int])-> int:
        """
        This function takes a list of integers as input
        and returns the smallest index i such that the sum of the digits of 
        nums [i] is equal to i.
        If no such index exists, the function returns -1.
        """
        # helper function to calculate the sum of digits
        def sum_of_digits(num: int) -> int:
            total = 0
            while num > 0:
                last_digit = num % 10
                total += last_digit
                num = num // 10
            return total

        # iterate through the list and check for the condition
        min_index = -1
        for i, current in enumerate(nums):
            if sum_of_digits(current) == i and (min_index == -1 or i < min_index):
                min_index = i
        return min_index

