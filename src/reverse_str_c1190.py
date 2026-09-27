# Date: 2026-09-27
# Difficulty: Medium
# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Solution:
    def reverseParentheses(self, s: str) -> str:
        """
        Args:
            s (str): The input string containing nested parentheses.
        Returns:
            str: The final string with all parentheses removed and substrings within parentheses reversed.
        """
        layers = [""]

        for char in s:
            if char == "(":
                # Open a new nesting level
                layers.append("")
            elif char == ")":
                # Close the current level: pop, reverse, and merge into the parent level
                inner_text = layers.pop()
                layers[-1] += inner_text[::-1]
            else:
                # Append standard letters to the active nesting level
                layers[-1] += char

        return layers[0]