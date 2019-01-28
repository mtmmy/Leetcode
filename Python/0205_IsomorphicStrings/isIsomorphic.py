import string
class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dictS = dict.fromkeys(string.printable, -1)
        dictT = dict.fromkeys(string.printable, -1)
        
        for i in range(len(s)):            
            if dictS[s[i]] != dictT[t[i]]:
                return False
            dictS[s[i]] = i
            dictT[t[i]] = i
        
        return True