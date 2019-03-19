from collections import Counter
class Solution:
    def threeSumMulti(self, A, target: int) -> int:
        setA = list(set(A))
        counter = Counter(A)
        result = 0
        setA.sort()        
        for x in range(len(setA)):
            for y in range(x, len(setA)):
                i, j = setA[x], setA[y]
                k = target - i - j
                if k == i == j:
                    result += counter[k] * (counter[k] - 1) * (counter[k] - 2) // 6
                elif i == j != k:
                    result += counter[i] * (counter[i] - 1) // 2 * counter[k]
                elif k > i and k > j:
                    result += counter[k] * counter[i] * counter[j]
        return result % (10 ** 9 + 7)