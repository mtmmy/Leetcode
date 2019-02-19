import string
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #return sorted(s) == sorted(t)
        
        d = dict.fromkeys(string.ascii_lowercase, 0)
        
        for c in s:
            d[c] += 1
        
        for c in t:
            d[c] -= 1
            
        for val in d.values():
            if val != 0:
                return False
            
        return True
            
            