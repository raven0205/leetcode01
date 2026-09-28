# Date: 2026-09-28
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def maxDepth(self, s:str):
        recursive_stack = []
        ans = 0 # max depth seen so far

        for char in s:  # read the string from left to right
            if char == "(":
                recursive_stack.append(char) # one more parentheses is open
                current_depth = len(recursive_stack)
                # keep the larger depth
                ans = max(ans,current_depth)

            elif char == ")":
                # check if the recursive stack contains parentheses
                if recursive_stack:
                    recursive_stack.pop()
        
        return ans

