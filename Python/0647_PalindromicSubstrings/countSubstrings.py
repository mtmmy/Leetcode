class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            for j in range(min(i + 1, len(s) - i)):
                if s[i - j] == s[i + j]: result += 1
                else: break
            for j in range(min(i + 1, len(s) - i - 1)):
                if s[i - j] == s[i + j + 1]: result += 1
                else: break
        return result

target = Solution()
target.countSubstrings("aaaaa")