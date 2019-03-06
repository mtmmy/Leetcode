class Solution:
    def isValid(self, S: str) -> bool:
        if not S:
            return True
        if len(S) < 3:
            return False
        stack = [S[0], S[1]]
        for c in S[2:]:
            if c == 'a' or c == 'b':
                stack.append(c)
            else:
                if (len(stack) < 2):
                    return False
                string = stack.pop() + stack.pop()
                if string != "ba":
                    return False
        return False if stack else True