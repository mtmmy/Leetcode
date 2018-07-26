class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        des = path.split("/")
        stack = []
        for s in des:
            if s == "..":
                if len(stack) > 0:
                    stack.pop()
            elif s == "." or s == "":
                continue
            else:
                stack.append(s)
        return "/" + "/".join(stack)
            
        
if __name__ == "__main__":
    target = Solution()
    result = target.simplifyPath("/a/./b/../../c/")
    print(result)
    result = target.simplifyPath("/home/")
    print(result)
    result = target.simplifyPath("/home//foo/")
    print(result)
    result = target.simplifyPath("/home/foo/.ssh/../.ssh2/authorized_keys/")
    print(result)
    result = target.simplifyPath("/..")
    print(result)
    result = target.simplifyPath("/../../../../../../")
    print(result)
    result = target.simplifyPath("/../../../../../../a/b/c")
    print(result)