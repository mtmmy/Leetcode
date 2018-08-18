class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        self.searchValidParentheses(s, 0, 0, ['(', ')'], result)
        return result
        
        
    def searchValidParentheses(self, s, last_i, last_j, p, result):        
        count = 0
        for i in range(last_i, len(s)):
            if s[i] == p[0]:
                count += 1
            elif s[i] == p[1]:
                count -= 1
            
            if count >= 0:
                continue
            
            for j in range(last_j, i + 1):
                if s[j] == p[1] and (j == last_j or s[j] != s[j - 1]):
                    self.searchValidParentheses(s[0:0 + j] + s[j + 1:], i, j, p, result)
            return

        reverse = s[::-1]
        if p[0] == '(':
            self.searchValidParentheses(reverse, 0, 0, [')', '('], result)
        else:
            result.append(reverse)
        