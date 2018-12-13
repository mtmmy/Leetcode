class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        nums = [n for n in range(len(S) + 1)]
        idxI = 0
        idxD = len(S)
        
        perm = []
        
        for c in S:
            if c == "I":
                perm.append(nums[idxI])
                idxI += 1
            else:
                perm.append(nums[idxD])
                idxD -= 1
        perm.append(idxI)
        return perm