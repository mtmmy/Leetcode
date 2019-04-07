from typing import List
import collections
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:        
        pairs = 0
        mapping = collections.defaultdict(int)
        for num in time:
            key = (num + 60) % 60
            mapping[key] += 1
            
        for num in time:
            match = 60 - (num % 60)
            match = 0 if match == 60 else match
            if num % 30 == 0:
                if mapping[match] > 0:
                    mapping[match] -= 1
                    pairs += mapping[match]
            else:
                pairs += mapping[match]
                mapping[(num + 60) % 60] -= 1
        return pairs