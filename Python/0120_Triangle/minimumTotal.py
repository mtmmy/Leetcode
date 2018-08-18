class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        sumTri = []
        for i in range(len(triangle)):
            sumTri.append([])
            for j in range(len(triangle[i])):
                if i == 0 and j == 0:
                    sumTri[i].append(triangle[i][j])
                else:
                    if i > 0:                        
                        if j == 0:
                            sumTri[i].append(sumTri[i - 1][j] + triangle[i][j])
                        elif j == len(triangle[i]) - 1:
                            sumTri[i].append(sumTri[i - 1][j - 1] + triangle[i][j])
                        else:
                            sumTri[i].append(min(sumTri[i - 1][j - 1], sumTri[i - 1][j]) + triangle[i][j])            
        return min(sumTri[-1])