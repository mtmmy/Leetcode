from collections import deque
class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """        
        def searchValidParentheses(s, last_i, last_j, p, result):        
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
                        searchValidParentheses(s[:0 + j] + s[j + 1:], i, j, p, result)
                return

            reverse = s[::-1]
            if p[0] == '(':
                searchValidParentheses(reverse, 0, 0, [')', '('], result)
            else:
                result.append(reverse)
        result = []
        searchValidParentheses(s, 0, 0, ['(', ')'], result)
        return result
    
    def removeInvalidParenthesesBFS(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValid(s1):
            count = 0
            for c in s1:
                if c == "(":
                    count += 1
                elif c == ")":
                    count -= 1
                    if count < 0:
                        return False
            return count == 0
        
        result, queue, visited, found = [], deque([s]), set(), False
        
        while queue:
            curStr = queue.popleft()
            if isValid(curStr):
                result.append(curStr)
                found = True
            if not found:
                for i in range(len(curStr)):
                    c = curStr[i]
                    if c == "(" or c == ")":
                        tempStr = curStr[:i] + curStr[i + 1:]
                        if tempStr not in visited:
                            queue.append(tempStr)
                            visited.add(tempStr)
        return result
        
target = Solution()
target.removeInvalidParentheses("()")