from typing import List
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        if not queries or not pattern:
            return []
        
        def compare(q):
            i, j = 0, 0
            while i < len(pattern) and j < len(q):
                if pattern[i] == q[j]:
                    i += 1
                    j += 1
                else:
                    if q[j].isupper():
                        return False
                    if q[j].islower():
                        j += 1
            if i != len(pattern):
                return False
            while j < len(q):
                if q[j].isupper():
                    return False
                j += 1
            return True
        
        return [compare(q) for q in queries]