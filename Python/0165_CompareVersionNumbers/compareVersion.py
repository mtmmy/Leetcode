class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        ver1 = list(map(int, version1.split(".")))
        ver2 = list(map(int, version2.split(".")))
        n = min(len(ver1), len(ver2))
        
        i = 0
        
        while i < n:
            if ver1[i] > ver2[i]:
                return 1
            elif ver1[i] < ver2[i]:
                return -1
            else:
                i += 1
                
        if i < len(ver1):
            for j in range(i, len(ver1)):
                if ver1[j] > 0:
                    return 1
        
        if i < len(ver2):
            for j in range(i, len(ver2)):
                if ver2[j] > 0:
                    return -1
                
        return 0
        