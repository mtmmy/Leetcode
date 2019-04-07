class Solution:
    def queryString(self, S: str, N: int) -> bool:        
        for i in range(1, N + 1):
            numStr = ""
            x = i
            while x != 0:
                numStr += str(x % 2)
                x //= 2
            if numStr[::-1] not in S:
                return False
        return True