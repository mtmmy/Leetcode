class Solution:
    def bitwiseComplement(self, N: int) -> int:
        bits = 0
        tempN = N
        while tempN > 0:
            tempN = tempN >> 1
            bits += 1        
        mask = 2 ** bits - 1 if bits else 1
        return N ^ mask