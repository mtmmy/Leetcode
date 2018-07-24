class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for i in range (1, n + 1, 1):
            mod3 = i % 3
            mod5 = i % 5
            if mod3 == 0 and mod5 == 0:
                result.append("FizzBuzz")
            elif mod3 == 0:
                result.append("Fizz")
            elif mod5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result
        
if __name__ == "__main__":
    target = Solution()
    result = target.fizzBuzz(15)