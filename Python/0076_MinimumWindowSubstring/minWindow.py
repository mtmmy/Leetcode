class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t):
            return ""
        
        left, count, minLength, result, counter = 0, 0, len(s) + 1, "", {}
        
        for c in t:
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1
                
        for right in range(len(s)):
            if s[right] in counter:
                counter[s[right]] -= 1
            
                if counter[s[right]] >= 0:
                    count += 1
                    
                while count == len(t):
                    nowLength = right - left + 1
                    if nowLength < minLength:
                        minLength = nowLength
                        result = s[left:left + minLength]
                    
                    if s[left] in counter:
                        counter[s[left]] += 1
                        if counter[s[left]] > 0:
                            count -= 1
                    left += 1
        
        return result
        
        