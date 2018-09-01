import unittest

class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.replace("-", "").upper()
        rem = len(S) % K

        return "-".join([S[:rem]] + [S[i:i+K] for i in range(rem, len(S), K)]).strip("-")

        # S = S.upper()
        # i, kCounter = len(S) - 1, 0

        # while i >= 0:
        #     if S[i] == "-":                    
        #         S = S[:i] + S[i + 1:]
        #         i -= 1
        #         continue                
        #     else:
        #         if kCounter == K:
        #             kCounter = 0
        #             S = S[:i + 1] + "-" + S[i + 1:]                
        #         kCounter += 1
        #     i -= 1
        # return S

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        #self.assertEqual("2-5G-3J", target.licenseKeyFormatting("2-5g-3-J", 2))
        self.assertEqual("5F3Z-2E9W", target.licenseKeyFormatting("5F3Z-2e-9-w", 4))
        #self.assertEqual("5F-3Z2-E9W", target.licenseKeyFormatting("5F3Z-2e-9-w", 3))
        self.assertEqual("AA-AA", target.licenseKeyFormatting("--a-a-a-a--", 2))

if __name__ == '__main__':
    unittest.main()
        