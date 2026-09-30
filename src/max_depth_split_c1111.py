# date: 30.09.2026
# difficulty level: medium
# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        """
        Splits a valid parentheses string into two groups (0 and 1) 
        to minimize the maximum nesting depth of both groups.
        """
        ans = []
        
        for i, s in enumerate(seq):
            if s == "(": 
                ans.append(i % 2)
                
            else:
                ans.append(1-i % 2)
                
        return ans