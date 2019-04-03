from typing import List
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total = sum(A)
        if total % 3 != 0:
            return False
        
        divSum = total // 3
        sums = [divSum * 2, divSum]
        counter = 0
        for i in range(len(A)):
            counter += A[i]
            if counter == sums[-1]:
                sums.pop()
            if not sums:
                return True
        return False