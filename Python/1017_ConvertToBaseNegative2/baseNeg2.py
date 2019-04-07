class Solution:
    def baseNeg2(self, N: int) -> str:
        if N == 0:
            return "0"
        result = ""
        while N != 0:
            r = N % -2
            N = N // -2
            
            if r < 0:
                r += 2
                N += 1
            result += str(r)
        return result[::-1]