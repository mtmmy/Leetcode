import string

class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        m, n = len(s), len(p)
        
        if m == 0:
            return []
        
        result = []
        
        ds = dict.fromkeys(string.ascii_lowercase, 0)
        dp = dict.fromkeys(string.ascii_lowercase, 0)
        
        for i in range(len(p)):
            if i < m:
                ds[s[i]] += 1
            
            if i < n:
                dp[p[i]] += 1                
        
        if ds == dp:
            result.append(0)
        
        for i in range(n, m):
            ds[s[i]] += 1
            ds[s[i - n]] -= 1
            if ds == dp:
                result.append(i - n + 1)
        
        return result
        
if __name__ == "__main__":
    target = Solution()
    result = target.findAnagrams("cbaebabacd", "abc")
    print(result)