from random import randint
from bisect import bisect_left
class Solution:

    def __init__(self, w):
        self.w = []
        self.total = 0
        for num in w:
            self.total += num
            self.w.append(self.total)

    def pickIndex(self) -> int:
        return bisect_left(self.w, randint(1, self.total))


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()