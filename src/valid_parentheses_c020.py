# Date: 2026-10-01
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def isValid(self, s:str)-> bool:
        """
        to check if an input s is valid:
        1. open brackets must be closed by same type;
        2. open brackets must be closed in correct order;
        3. every close bracket has a corresponding open bracket;
        """
        d = []
        for char in s:
            # append the corresponding closing bracket
            if char == "(":
                d.append(")")
            elif char == "{":
                d.append("}")
            elif char == "[":
                d.append("]")
            # for closing brackets
            else:
                # first char is closing bracket
                # or not the corresponding closing bracket
                if not d or char != d.pop():
                    return False
            
        # check if the stack is empty (all brackets are matched)
        return not d