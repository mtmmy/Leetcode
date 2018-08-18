class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        isDec = False
        isSci = False
        nrSeen = False
        nrAfterE = False
        s= s.strip()
        i = 0
        while i < len(s):
            if s[i] == '-' or s[i] == "+":
                if i > 0 and s[i - 1] != 'e':
                    return False
                
            elif s[i] == 'e':
                if isSci or not nrSeen:
                    return False
                isSci = True
                nrAfterE = False
            elif s[i] == '.':
                if isSci or isDec:
                    return False
                isDec =True
            
            elif s[i].isdigit():
                nrSeen = True
                nrAfterE = True
            else:
                return False
            i += 1
        
                     
        return nrSeen and nrAfterE