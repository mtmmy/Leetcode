import string
class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dictS = dict.fromkeys(string.printable, 0)
        dictT = dict.fromkeys(string.printable, 0)
        
        for i in range(len(s)):            
            if dictS[s[i]] != dictT[t[i]]:
                return False
            dictS[s[i]] = i + 1
            dictT[t[i]] = i + 1
        
        return True