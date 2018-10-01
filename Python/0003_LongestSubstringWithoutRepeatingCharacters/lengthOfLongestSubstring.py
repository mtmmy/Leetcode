import string
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        characters = dict.fromkeys(string.printable, 0)
        start, longest = 0, 0
        for i in range(len(s)):
            c = s[i]
            start = max(characters[c] + 1, start)
            characters[c] = i
            longest = max(longest, i - start + 1)
        
        return longest

if __name__ == "__main__":
    target = Solution()
    target.lengthOfLongestSubstring("abcabcbb")