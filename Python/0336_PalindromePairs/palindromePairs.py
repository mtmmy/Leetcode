import unittest
from collections import deque

class Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def isPalindrome(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1                
            return True

        result = []
        pos = {}
        wLength = set()
        n = len(words)

        for i in range(n):
            pos[words[i]] = i
            wLength.add(len(words[i]))
        
        for i in range(n):
            s = words[i]
            sLen = len(s)
            s = s[::-1]
            if s in pos and pos[s] != i:
                result.append([i, pos[s]])
            
            listLen = sorted(list(wLength))
            for d in listLen:
                if d == sLen:
                    break
                if isPalindrome(s, 0, sLen - d - 1) and s[sLen - d:] in pos:
                    result.append([i, pos[s[sLen - d:]]])
                if isPalindrome(s, d, sLen - 1) and s[:d] in pos:
                    result.append([pos[s[:d]], i])

        return result
        

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        self.assertEqual([[0,1],[1,0],[3,2],[2,4]], target.palindromePairs(["abcd","dcba","lls","s","sssll"]))
        self.assertEqual([], target.palindromePairs(["abaabbbaaabbbaababbbbabaabbbabb","aaa","aab","aabbabaababbaaaaabaabaaaabaaaabababbbbbbbabbaaabbbbabaaa","abbaaaaaabaaabbbbbbababbabbaababbbbbaaabababaabbbaabbbbbaabbaaabbaaaabaabbaaaaabbababaabbbbaabaabbbbbbbabbbaaabbbaaabababaaaaa","abbababbabaabab","baaabbbaaaaabbabaabbaabbaaababbbaabbbabbbababbaababaabbbbaaaaabbbbabbbbbbbbaabbbbbbaaaababbbaabbaaaababbababbbabababbaaabbbbbabaaabbaaabaaabbaaaaaabababbababaabbbaaabbba","bbabaabbbaaabaabaaabbaaabbababbabbaaaabbaabababbbabaabbbbbaababaaabbabbaaabaabbbabbbbaabbbabbaabaaabbbbaabbbaabbbbbbababbabbaabbbabbaabbbbabaababaaab","bbaaabaabbaaabbaabbbabaababbaaabbbabaabbbaabbbbbabbbaaaaaaabaaaaaaabaabaaaaaaabbbbbbbbbaabaaabbbabaabba","baaaabaababbabbbabbaaabababaa","babbabbabbbabbbaaabbaabbbabaaabaabbbbbabaabbbbbababbabbabaababaaaaaababbaaababbbabbababbbbababaabbaabaaabaaaa","baaaabbbababbbabbbbabbaabaaaabbaaababaabbbbbbabbbbbaaabbbaaabababbaabaabaaaabbbaaaaabbbbaaabaaaaabbaabbababbbbabbbbbababbabaababababbbaa","baabbbbbbbbbaabbbabbbaabbbaabbbaabbabbbbbbababaabbaababbbabbbababbb","abaabbaaaabaabbababababababbbbbbbbbbabbbbaabaabbbbababababbbabbbbbabbababbbaabaaaabbbbabbbbbbababbbbbbbaabbbbabaaabababaaaaaabbbababaaabbabbababbbabbababbaaaabaab","abaabaaaabbabbaaabaabababbbbabbababbbabbabbbabbaaabaabbaabaa","baabbbbaaaaabbaaababaabbaabbabbaaaabbbaaababbbbaababbbaaababbbbaaabbbbbbababbabaaababbabababaababbaabbabbbabababaabbaaababaaa","aabaabbababbaaaabbbbbbbaaaababbbbaababbbbaabbbabbaaaabbaabbabaabaabbbbabb","aaaababaabbbababbaabbbaababbbbaaabbababbaaaaaaaabbbbaaabbbbbaababbbaaabbbabbabbbabbabbbaaaaaabbbabaabaaaabbbbbabbbbaaaabaabbababbabbbbbbb","bbbbabbbbaabbabbbaaaaabbabbaabbaababbbabbbbaaaaabababbbbaabbaabaabaabbbbabaabbabaaaabbaaaaaaababaabbbabaaabababbbaabbbaaabbaabbaaababaabbbbbabb","bbbbaabbbaaababaabaabaaabbbbbbabbbaabbbbaabaaaaababaababaaaaabbaababbbabbbbaabbbbbbbabbaababbbbaabbabbbbaaababbbabbbabbabbabbaababababbbabababbbabaabbabaaababababbbaaabababababaaabaaabbb","abbbababbaabaaaaabbbbaabaaababbbabbbab","aaababbaabbbbbaaababbbbaabaaaabbaabbbbabbaaaabababbbaabbbaaabbbabbbaaaaaabbaabbaabaabbaabaaaabbbbabaaaabababaabaababbabbaababbabbbabbbbaabbaaba","abbbabaabbaaabbabaababaababbbbababaabbaabbbabababbbababbbabaabbbababaaaababbaabaabababaaaabaababababbbbabaaabaaabbbbaabaaababababbbbbaababbbaababababbaa","abbabababbbbabbbbabbabbabbabaababbaab","bbbabaabababababbbbbaabb","aaabbaabbabababaababbabbaaaaabbbaaaabbaaaaaaaaaaabbbbaaaabababbabaaabaabaabbbbaabababbaabaaaaaaaaabaaabbbabaaababbbabbababaaababbbaabbaaabbbbaab","babbabbbbbabaabbbaabbaaabaabaabaaaababbbbbbbbbbbbaaabbaabbbbaababbaaaababaabaabbababbaaabaaaababbabbbbaaabaababbaababaaabaabaaababbabbbaaabbabb","bababbbabaabaaaaaaabbababbbabaaaaabbaabbaaabbaabababaaaabaaaabaaaabbb","baabbbbabaababababbaaabbaaababbababaabaabaabbabbbbabbbbbab","bbbbaaabbabbabbaabbabbaaaabbabbbbaabbaababbbabaabbbbbaaaaaabbaabbbbbaabaabaaababaabbbaababbbbbaababaaba","bbaabbaabbaabbbaabbabbaabbbbbabaaaababbbaaaaaababbabbbababaaaabaabbbbaabaabaaabbbabbbabbaababaaababaabbabba","abbaababaaaabbaaaabaaaaba","bbbaaaabaaaabbbaababbabbaaaaaaa","bbabaaaaaababaabbabaabaabbabbaabbbbbabbbabbbbaabababaabbbbaaababaa","aabbababaaaaaaaaaabaabbababbaaabaaaaabbaaabaababbbbabaabaabbaabaaaabbbbbbbaabaaabbabbabaaaababbbbababababaabaababaaaabbabab","baabbbbaabbaaabbaaaababbaabbbbaaabbaabbabababbababbaaaabbbbbbbabaaabbaaabbbaaaabbabaaabaababbabbbbabbbaaabaaaabbababbbabaabbaaabb","aabbbabbabaaaabbbabbbbaaba","aabbbaabababbabbbbbbababbbbbaaaababbabaaaabbabbbaaaaabbababbbbaaaabbaababaaababbabaaabbbbababbabbbabaaaabbabbabbabbabababaabaabbabbabbbbbbbabbbabaaaaaaba","babaabbaaaabbaabbbbabbbabbbbabbbbbaaababbbbaaababbaabbaaabaabaaaabbaabbbaabababbba","aaaaabbbbbabbababbbaaabaaabbababaaaabbabaababbabbbbbabbbbbaabaabbaababb","bbbbaaaaabbbbaaaabaabbbabaabaabbabbbbabbbbaabbabbbababbbabaabbaabbbbabbabaabbbaabbaaaabaaabababbabbabaaabaaaabaaabaaabbbbbaaaabbaabbbbbababbbbbbabababbaaababaaabbbabaabaaab","aaaaabaaabbababbaaabbaababbabbabbabbbbaaabaabaababbabbbbabaaaaabbabaaabbbbbbaaaaaaaabbbaabaabaabaaabbabbaabaabbaabbbabbaaaabbbbabaaababaaabbbbabaaabbababbbbaabaaaabbaaaaba","abaaaabbbbababba","babbaabbbaabbbbbbbbbbbaabbbbaaabbbabbbbbbbbaabbbabbababaabbbbabaaabbbabbbaabbaabbbaaaaabbbabaaabbaabaabaabababbaababaaaaababbbbabbabaaaabbabaaaababaabaaaaabbabbabababbbaabbbaababbabbbabbbabab","babbbbbaaaabbabbaaaababbbabaabbaaabbabbbbbaabbbbbbaabbbbbabaabaababbbaabbaa","babbaaaaabbbbbbabaaaabbbbabbbbbabaaabbaaaaaabbbbaababbaababbaaabbabbbbaaaaaaababbbbbabababbaaaaaabbbbbaaababbaabaabbaaaababbbbaaaababaababbaaabbababbabbbababbbababbabababaababababbababa","bbaaaabaaaaabbbbbbabaaaabaaaaabbabbbbbbaab","aabaaabbabaabbaababbabbbabbaabaabbbaababb","bbbababababbbababbabbbbaaaaabbbabababbaaaaababaabbbaabaaaaababaaabaaaaabbbabababbbaaaaababaaabbabaabbababbabbbbaaababaaaaabbabba","baabbbaaaababababaabbabbaaabaabbbabbbaaabbbbbbbaaabbbaabaaabbbaababababbabbabaaababababbbaababaaaaaaabaaabbbabbabbabbaabbaaabaabababababbaaabbbabaaaaabbab"]))

if __name__ == '__main__':
    unittest.main()
        