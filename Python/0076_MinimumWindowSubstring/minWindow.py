class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t):
            return ""
        
        left, count, minLength = 0, 0, len(s) + 1
        
        result = ""
        
        dict_t = {}
        for c in t:
            if c in dict_t:
                dict_t[c] += 1
            else:
                dict_t[c] = 1
                
        for right in range(len(s)):
            if s[right] in dict_t:
                dict_t[s[right]] -= 1
            
                if dict_t[s[right]] >= 0:
                    count += 1
                    
                while count == len(t):
                    nowLength = right - left + 1
                    if nowLength < minLength:
                        minLength = nowLength
                        result = s[left:left + minLength]
                    
                    if s[left] in dict_t:
                        dict_t[s[left]] += 1
                        if dict_t[s[left]] > 0:
                            count -= 1
                    left += 1
        
        return result
        
        