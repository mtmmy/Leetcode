class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        result, opened = "", 0
        
        for c in S:
            if c == "(" and opened > 0:
                result += c
            elif c == ")" and opened > 1:
                result += c
            opened += 1 if c == "(" else -1
        
        return result
        