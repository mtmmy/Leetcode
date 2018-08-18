class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        if len(s) <= 16:
            out = ""
            self.findIP(result, s, out, 4)
        return result

    def findIP(self, result, s, out, count):
        if count == 0 and len(s) == 0:
            result.append(out)
        else:
            for i in range(1, 4):
                subS = s[0:i]
                if len(s) >= i and self.isValid(subS):
                    if count == 1:
                        self.findIP(result, s[i:], out + subS, count - 1)
                    else:
                        self.findIP(result, s[i:], out + subS + ".", count - 1)

    def isValid(self, s):
        if s == "" or len(s) > 3 or (len(s) > 1 and s[0] == "0"):
            return False
        else:
            return int(s) < 256 and int(s) >= 0
        

if __name__ == "__main__":
    target = Solution()
    result = target.restoreIpAddresses("10001")
    print(result)
    result = target.restoreIpAddresses("25525511135")
    print(result)