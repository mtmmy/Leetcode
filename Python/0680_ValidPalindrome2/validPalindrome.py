# class Solution:
#     def validPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         left = 0
#         right = len(s) - 1
#         oneChance = False
        
#         while left < right:
#             if s[left] == s[right]:
#                 left += 1
#                 right -= 1
#             elif not oneChance:
#                 oneChance = True
#                 result1 = self.validPalindromeSolid(s[left + 1 : right + 1])
#                 result2 = self.validPalindromeSolid(s[left : right])
#                 return result1 or result2
#         return True
                
#     def validPalindromeSolid(self, s):
#         left = 0
#         right = len(s) - 1
#         while left < right:
#             if s[left] == s[right]:
#                 left += 1
#                 right -= 1
#             else:
#                 return False
#         return True
class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == s[::-1]:
            return True
        
        left = 0
        right = len(s) - 1
        oneChance = False
        
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            elif not oneChance:
                oneChance = True
                return s[left + 1 : right + 1] == s[left + 1 : right + 1][::-1] or s[left : right] == s[left : right][::-1]
        return True