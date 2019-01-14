class Solution:
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        remainders = {0: 1}
        total, count = 0, 0
        for x in A:
            total += x
            mod = total % K
            if mod in remainders:                
                count += remainders[mod]
            remainders[mod] = remainders.get(mod, 0) + 1
        return count