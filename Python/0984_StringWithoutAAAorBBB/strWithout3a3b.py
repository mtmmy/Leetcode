class Solution:
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        result = ""
        while A + B > 0:
            if A >= B:
                if A > 2 * B:
                    result += "a" * min(2, A) + "b" * min(1, B)
                    A -= min(2, A)
                    B -= min(1, B)
                else:
                    result += "a" + "b" * min(1, B)
                    A -= 1
                    B -= min(1, B)
            else:
                if B > 2 * A:
                    result += "b" * min(2, B) + "a" * min(1, A)
                    B -= min(2, B)
                    A -= min(1, A)
                else:
                    result += "b" + "a" * min(1, A)
                    A -= min(1, A)
                    B -= 1
                
        return result