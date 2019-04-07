class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        low = max(weights)
        high = sum(weights)
        
        while low < high:
            cap, load, day = (low + high) // 2, 0, 1
            
            for w in weights:
                if w + load > cap:
                    load = w
                    day += 1
                else:
                    load += w
            if day > D:
                low = cap + 1
            else:
                high = cap
        return low
                