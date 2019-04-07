from typing import List
class Solution:
    def prefixesDivBy5prefixesDivBy5(self, A: List[int]) -> List[bool]:
        result = []
        cur = 0
        for num in A:
            cur = cur * 2 + num    
            result.append(cur % 5 == 0)
        return result
            
            