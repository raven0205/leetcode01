class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        stack = []

        for char in s:
            if char == ")":
                stack.pop()
                if stack:
                    res.append(char)
                
            elif char == "(":
                if stack:
                    res.append(char)
                stack.append(char)
        
        return "".join(res)
