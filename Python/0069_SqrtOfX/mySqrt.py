class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        
        start, end = 0, x // 2
        
        while start <= end:
            mid = (end + start) // 2
            sqrMid = mid ** 2
            if sqrMid < x:
                start = mid + 1
            elif sqrMid > x:
                end = mid - 1
            else:
                return mid
        return end