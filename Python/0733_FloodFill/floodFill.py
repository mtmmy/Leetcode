class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if image[sr][sc] == newColor:
            return image
        
        m, n = len(image), len(image[0])
        
        def fill(i, j, oldColor):
            if image[i][j] == oldColor:
                image[i][j] = newColor
                if i > 0:
                    fill(i - 1, j, oldColor)
                if i < m - 1:
                    fill(i + 1, j, oldColor)
                if j > 0:
                    fill(i, j - 1, oldColor)
                if j < n - 1:
                    fill(i, j + 1, oldColor)
        
        fill(sr, sc, image[sr][sc])
        return image