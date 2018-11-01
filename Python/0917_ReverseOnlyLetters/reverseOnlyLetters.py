class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """

        counts = []
        stack = []
        
        count = 0
        for c in S:
            if c.isalpha():
                count += 1
                stack.append(c)
            else:
                counts.append((count, c))
                count = 0
        
        if not counts:
            return S[::-1]
        
        result, i, charCount = "", 0, counts[0][0]
        while stack:            
            if charCount == 0:
                notLetter = counts[i]
                result += notLetter[1]
                i += 1
                if i < len(counts):
                    charCount = counts[i][0]
                else:
                    break
            else:
                charCount -= 1
                result += stack.pop()
                
        while stack:
            result += stack.pop()
        
        while i < len(counts):
            result += counts[i][1]
            i += 1
        
        return result
                
        