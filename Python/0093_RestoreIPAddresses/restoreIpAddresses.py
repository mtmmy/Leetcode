class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        if len(s) <= 12:
            self.findIP(result, s, "", 4)
        return result

    def findIP(self, result, s, out, count):
        if count == 0 and not s:
            result.append(out[:-1])
        else:
            for i in range(1, min(4, len(s) + 1)):
                num = s[0:i]
                if i == 1:
                    self.findIP(result, s[i:], out + num + ".", count - 1)
                elif i == 2 and s[0] != "0":
                    self.findIP(result, s[i:], out + num + ".", count - 1)
                elif i == 3 and s[0] != "0" and int(num) < 256:
                    self.findIP(result, s[i:], out + num + ".", count - 1)
        

if __name__ == "__main__":
    target = Solution()
    result = target.restoreIpAddresses("10001")
    print(result)
    result = target.restoreIpAddresses("25525511135")
    print(result)