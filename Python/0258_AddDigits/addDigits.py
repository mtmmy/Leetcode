class Solution:
    def addDigits(self, num: int) -> int:
        return 1 + (num - 1) % 9 if num else 0
        # while num > 9:
        #     num = sum(list(map(int, str(num))))
        # return num