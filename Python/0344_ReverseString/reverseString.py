class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        #return s[::-1]
        i, j = 0, len(s) - 1
        listS = list(s)
        
        while i < j:
            listS[i], listS[j] = listS[j], listS[i]
            i += 1
            j -= 1
            
        return "".join(listS)