class Solution:
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        powX, powY = [], []
        
        for i in range(bound):
            tmp = x ** i
            if tmp <= bound:
                powX.append(tmp)
            else:
                break
        
        for i in range(bound):
            tmp = y ** i
            if tmp <= bound:
                powY.append(tmp)
            else:
                break
                
        result = set()
        
        for num1 in powX:
            for num2 in powY:
                if num1 + num2 <= bound:
                    result.add(num1 + num2)
        
        return list(result)