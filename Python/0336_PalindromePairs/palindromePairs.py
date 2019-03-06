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

        result, n = [], len(words)
        pos, length = {}, set()
        
        for i in range(n):
            pos[words[i]] = i
            length.add(len(words[i]))
            
        sortedLength = sorted(list(length))
        for i in range(n):
            rWord = words[i][::-1]
            if rWord in pos and pos[rWord] != i:
                result.append([i, pos[rWord]])
            
            wLen = len(rWord)
            for l in sortedLength:
                if l == wLen:
                    break
                if isPalindrome(rWord, 0, wLen - l - 1) and rWord[wLen - l:] in pos:
                    result.append([i, pos[rWord[wLen - l:]]])
                if isPalindrome(rWord, l, wLen - 1) and rWord[:l] in pos:
                    result.append([pos[rWord[:l]], i])

        return result
        
class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        self.assertEqual([[0,1],[1,0],[3,2],[2,4]], target.palindromePairs(["abcd","dcba","lls","s","sssll"]))
        self.assertEqual([], target.palindromePairs(["abaabbbaaabbbaababbbbabaabbbabb","aaa","aab","aabbabaababbaaaaabaabaaaabaaaabababbbbbbbabbaaabbbbabaaa","abbaaaaaabaaabbbbbbababbabbaababbbbbaaabababaabbbaabbbbbaabbaaabbaaaabaabbaaaaabbababaabbbbaabaabbbbbbbabbbaaabbbaaabababaaaaa","abbababbabaabab","baaabbbaaaaabbabaabbaabbaaababbbaabbbabbbababbaababaabbbbaaaaabbbbabbbbbbbbaabbbbbbaaaababbbaabbaaaababbababbbabababbaaabbbbbabaaabbaaabaaabbaaaaaabababbababaabbbaaabbba","bbabaabbbaaabaabaaabbaaabbababbabbaaaabbaabababbbabaabbbbbaababaaabbabbaaabaabbbabbbbaabbbabbaabaaabbbbaabbbaabbbbbbababbabbaabbbabbaabbbbabaababaaab","bbaaabaabbaaabbaabbbabaababbaaabbbabaabbbaabbbbbabbbaaaaaaabaaaaaaabaabaaaaaaabbbbbbbbbaabaaabbbabaabba","baaaabaababbabbbabbaaabababaa","babbabbabbbabbbaaabbaabbbabaaabaabbbbbabaabbbbbababbabbabaababaaaaaababbaaababbbabbababbbbababaabbaabaaabaaaa","baaaabbbababbbabbbbabbaabaaaabbaaababaabbbbbbabbbbbaaabbbaaabababbaabaabaaaabbbaaaaabbbbaaabaaaaabbaabbababbbbabbbbbababbabaababababbbaa","baabbbbbbbbbaabbbabbbaabbbaabbbaabbabbbbbbababaabbaababbbabbbababbb","abaabbaaaabaabbababababababbbbbbbbbbabbbbaabaabbbbababababbbabbbbbabbababbbaabaaaabbbbabbbbbbababbbbbbbaabbbbabaaabababaaaaaabbbababaaabbabbababbbabbababbaaaabaab","abaabaaaabbabbaaabaabababbbbabbababbbabbabbbabbaaabaabbaabaa","baabbbbaaaaabbaaababaabbaabbabbaaaabbbaaababbbbaababbbaaababbbbaaabbbbbbababbabaaababbabababaababbaabbabbbabababaabbaaababaaa","aabaabbababbaaaabbbbbbbaaaababbbbaababbbbaabbbabbaaaabbaabbabaabaabbbbabb","aaaababaabbbababbaabbbaababbbbaaabbababbaaaaaaaabbbbaaabbbbbaababbbaaabbbabbabbbabbabbbaaaaaabbbabaabaaaabbbbbabbbbaaaabaabbababbabbbbbbb","bbbbabbbbaabbabbbaaaaabbabbaabbaababbbabbbbaaaaabababbbbaabbaabaabaabbbbabaabbabaaaabbaaaaaaababaabbbabaaabababbbaabbbaaabbaabbaaababaabbbbbabb","bbbbaabbbaaababaabaabaaabbbbbbabbbaabbbbaabaaaaababaababaaaaabbaababbbabbbbaabbbbbbbabbaababbbbaabbabbbbaaababbbabbbabbabbabbaababababbbabababbbabaabbabaaababababbbaaabababababaaabaaabbb","abbbababbaabaaaaabbbbaabaaababbbabbbab","aaababbaabbbbbaaababbbbaabaaaabbaabbbbabbaaaabababbbaabbbaaabbbabbbaaaaaabbaabbaabaabbaabaaaabbbbabaaaabababaabaababbabbaababbabbbabbbbaabbaaba","abbbabaabbaaabbabaababaababbbbababaabbaabbbabababbbababbbabaabbbababaaaababbaabaabababaaaabaababababbbbabaaabaaabbbbaabaaababababbbbbaababbbaababababbaa","abbabababbbbabbbbabbabbabbabaababbaab","bbbabaabababababbbbbaabb","aaabbaabbabababaababbabbaaaaabbbaaaabbaaaaaaaaaaabbbbaaaabababbabaaabaabaabbbbaabababbaabaaaaaaaaabaaabbbabaaababbbabbababaaababbbaabbaaabbbbaab","babbabbbbbabaabbbaabbaaabaabaabaaaababbbbbbbbbbbbaaabbaabbbbaababbaaaababaabaabbababbaaabaaaababbabbbbaaabaababbaababaaabaabaaababbabbbaaabbabb","bababbbabaabaaaaaaabbababbbabaaaaabbaabbaaabbaabababaaaabaaaabaaaabbb","baabbbbabaababababbaaabbaaababbababaabaabaabbabbbbabbbbbab","bbbbaaabbabbabbaabbabbaaaabbabbbbaabbaababbbabaabbbbbaaaaaabbaabbbbbaabaabaaababaabbbaababbbbbaababaaba","bbaabbaabbaabbbaabbabbaabbbbbabaaaababbbaaaaaababbabbbababaaaabaabbbbaabaabaaabbbabbbabbaababaaababaabbabba","abbaababaaaabbaaaabaaaaba","bbbaaaabaaaabbbaababbabbaaaaaaa","bbabaaaaaababaabbabaabaabbabbaabbbbbabbbabbbbaabababaabbbbaaababaa","aabbababaaaaaaaaaabaabbababbaaabaaaaabbaaabaababbbbabaabaabbaabaaaabbbbbbbaabaaabbabbabaaaababbbbababababaabaababaaaabbabab","baabbbbaabbaaabbaaaababbaabbbbaaabbaabbabababbababbaaaabbbbbbbabaaabbaaabbbaaaabbabaaabaababbabbbbabbbaaabaaaabbababbbabaabbaaabb","aabbbabbabaaaabbbabbbbaaba","aabbbaabababbabbbbbbababbbbbaaaababbabaaaabbabbbaaaaabbababbbbaaaabbaababaaababbabaaabbbbababbabbbabaaaabbabbabbabbabababaabaabbabbabbbbbbbabbbabaaaaaaba","babaabbaaaabbaabbbbabbbabbbbabbbbbaaababbbbaaababbaabbaaabaabaaaabbaabbbaabababbba","aaaaabbbbbabbababbbaaabaaabbababaaaabbabaababbabbbbbabbbbbaabaabbaababb","bbbbaaaaabbbbaaaabaabbbabaabaabbabbbbabbbbaabbabbbababbbabaabbaabbbbabbabaabbbaabbaaaabaaabababbabbabaaabaaaabaaabaaabbbbbaaaabbaabbbbbababbbbbbabababbaaababaaabbbabaabaaab","aaaaabaaabbababbaaabbaababbabbabbabbbbaaabaabaababbabbbbabaaaaabbabaaabbbbbbaaaaaaaabbbaabaabaabaaabbabbaabaabbaabbbabbaaaabbbbabaaababaaabbbbabaaabbababbbbaabaaaabbaaaaba","abaaaabbbbababba","babbaabbbaabbbbbbbbbbbaabbbbaaabbbabbbbbbbbaabbbabbababaabbbbabaaabbbabbbaabbaabbbaaaaabbbabaaabbaabaabaabababbaababaaaaababbbbabbabaaaabbabaaaababaabaaaaabbabbabababbbaabbbaababbabbbabbbabab","babbbbbaaaabbabbaaaababbbabaabbaaabbabbbbbaabbbbbbaabbbbbabaabaababbbaabbaa","babbaaaaabbbbbbabaaaabbbbabbbbbabaaabbaaaaaabbbbaababbaababbaaabbabbbbaaaaaaababbbbbabababbaaaaaabbbbbaaababbaabaabbaaaababbbbaaaababaababbaaabbababbabbbababbbababbabababaababababbababa","bbaaaabaaaaabbbbbbabaaaabaaaaabbabbbbbbaab","aabaaabbabaabbaababbabbbabbaabaabbbaababb","bbbababababbbababbabbbbaaaaabbbabababbaaaaababaabbbaabaaaaababaaabaaaaabbbabababbbaaaaababaaabbabaabbababbabbbbaaababaaaaabbabba","baabbbaaaababababaabbabbaaabaabbbabbbaaabbbbbbbaaabbbaabaaabbbaababababbabbabaaababababbbaababaaaaaaabaaabbbabbabbabbaabbaaabaabababababbaaabbbabaaaaabbab"]))

if __name__ == '__main__':
    unittest.main()
        