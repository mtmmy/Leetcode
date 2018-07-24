class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = [[0] * n for _ in range(n)]
        nowWidth = n
        nowHeight = n
        x = 0
        y = 0
        num = 1
        while nowWidth > 0 and nowHeight > 0:
            if nowWidth == 1:
                result[x][y] = num                
            for i in range(nowWidth - 1):
                result[x][y] = num
                y += 1
                num += 1
            for i in range(nowHeight - 1):
                result[x][y] = num
                x += 1
                num += 1
            for i in range(nowWidth - 1):
                result[x][y] = num
                y -= 1
                num += 1
            for i in range(nowHeight - 1):
                result[x][y] = num
                x -= 1
                num += 1
            
            nowWidth -= 2
            nowHeight -= 2
            x += 1
            y += 1
        return result

if __name__ == "__main__":
    target = Solution()
    result = target.generateMatrix(1)