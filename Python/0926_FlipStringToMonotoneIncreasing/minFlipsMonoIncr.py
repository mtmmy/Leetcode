class Solution:
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        
        count1, countflip = 0, 0
        
        for c in S:
            if c == '0':
                if count1 > 0:
                    countflip += 1
                else:
                    continue
            else:
                count1 += 1
                met1 = True
            if countflip > count1:
                countflip = count1
        return countflip