from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = Counter(s)
        visited, stack = set(), []
        
        for c in s:
            freq[c] -= 1
            if c not in visited:                
                while stack and c < stack[-1] and freq[stack[-1]] > 0:
                    visited.remove(stack.pop())
                stack.append(c)
                visited.add(c)
            
        return "".join(stack)