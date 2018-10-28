class Solution:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = {}
        visited = {}
        for c in s:
            freq[c] = freq.setdefault(c, 0) + 1
            visited[c] = False
        
        stack = []
        
        for c in s:
            freq[c] -= 1
            if visited[c]:
                continue
            while stack and c < stack[-1] and freq[stack[-1]] > 0:
                visited[stack.pop()] = False
                
            stack.append(c)
            visited[c] = True
            
        return "".join(stack)
        
        
#         if not s:
#             return s
        
#         chars = [0] * 26
        
#         for char in s:
#             chars[ord(char) - 97] += 1
            
#         pos = 0
#         for i in range(len(s)):
#             if ord(s[i]) < ord(s[pos]):
#                 pos = i
            
#             idx = ord(s[i]) - 97
#             chars[idx] -= 1
#             if chars[idx] == 0:
#                 break
                
#         return s[pos] + self.removeDuplicateLetters(s[pos + 1:].replace(s[pos], ""))
                